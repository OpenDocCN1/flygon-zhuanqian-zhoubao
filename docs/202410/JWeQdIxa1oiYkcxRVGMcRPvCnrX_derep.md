# 手把手教你，免费使用Flux图片生成模型

最近在龙哥盟看到有圈友分享了一篇用 Flux 生成📕、👸号配图甚至做图生图的玩法，但里面给的 Flux API 已经失效了。正好我找到 Cloudflare 的免费接口，也许能帮大家继续白嫖下去。

Flux 到底是什么？简单说，它就是开源版的 Midjourney，出图质量相当能打，社区里已经有不少惊艳案例。背后的 Black Forest Labs 推出了 FLUX.1 系列开源模型，拥有 120 亿参数，算得上目前最大的文生图模型之一。这个系列分三个版本：pro、dev 和 schnell，分别面向不同场景，其中 schnell 对社区免费开放。

准备工作很简单：只要注册一个 Cloudflare 账号就行，具体注册流程不多说。没有条件的朋友，直接去淘宝买一个现成的也 OK。

接下来就是搭建 Flux Worker AI 的完整流程。这个接口本来是为了给大家研究和体验用的，当然你想拿来做一些正经事儿也没问题。为什么能白嫖资源？原因是 Cloudflare 在全球 100 多个国家都有数据中心和 GPU 算力，还跟 Nvidia 等硬件厂商合作，所以可以大方地开放一堆开源 AI 模型。这有点像教育优惠的套路——老师和学生有资格低价购买，Cloudflare 则是把这种福利直接送给了所有人。

废话不多说，直接开搞。

**1. 登录 Cloudflare**  
打开官网 https://cloudflare.com，点右上角的 Login 登录。

**2. 获取你的 cfid**  
登录之后，地址栏 URL 后面那一串数字就是你的 cfid：![](img/aa71a719133712894ed8355067185201.png)  
或者也可以在这里看：点击左侧的 Workers，然后右边就能看到：![](img/833193c9590f65e2d9c86f853f11ae76.png)

**3. 配置 API Token**  
点右上角“我的”，然后点 Token，进入 https://dash.cloudflare.com/profile/api-tokens：![](img/b40c1a716b6662ab2f66ce28dccccd53.png)  
这里一定要选 Workers AI 权限：![](img/ed058d9ec02df73cdd09579aa7c0deca.png)  
然后账号那里选择“所有”即可：![](img/87d294ce01d253dd916247037ecd4cda.png)  
再一直点下一步就完成了。

**4. 创建一个 KV 存储空间**  
左侧找到 Workers 下面的 KV，这个用来存储生成的图片：![](img/de53dfb76876b67f4ab9bc1d04cc5ea9.png)  
名字起成 `IMAGE_KV` 就行，点确定：![](img/98a02daa493ff1d36254abc34c7996db.png)

**5. 创建 Worker**  
点击 Workers，然后点 Create：![](img/6c491b44091600b576c4cb4010e73561.png)  
再点“创建”：![](img/dad2ad23dba85ab8a7df10af067f0b7b.png)  
随便取一个名字，然后点“构建”：![](img/87a5b7e080e2876ae73677cb3e628ccc.png)  
进去之后点“编辑代码”：![](img/669d4b65bd18d121e12eaf84b1688bad.png)

现在，把 L 站大佬提供的代码复制进去。代码里需要改三个地方：`api_key` 随便填，`cfid` 填第一步获取的那串数字，`api_token` 填第二步自己配置好的 Token。保存部署，就大功告成了。

以后无论是生成📕封面、👸号头图，还是拿现有图片做二次创作，都能免费靠 Flux 搞定了。快去试试吧！

有时候，最吊人胃口的，不是一句惊天动地的话，而是一个没头没尾的开始。

就像现在，摆在我面前的“素材”，干净得像一张白纸，只留下一个孤零零的记号——```
// 配置
const CONFIG = {
  API_KEY: "sk-1111",  //对外验证key
  CF_ACCOUNT_LIST: [{ account_id: "cfid", token: "api_token" }],  //改成自己的
  CF_IS_TRANSLATE: true,
  CF_TRANSLATE_MODEL: "@cf/qwen/qwen1.5-14b-chat-awq",
  CUSTOMER_MODEL_MAP: {
    "SD-1.5-Inpainting-CF": "@cf/runwayml/stable-diffusion-v1-5-inpainting",
    "DS-8-CF": "@cf/lykon/dreamshaper-8-lcm",
    "SD-XL-Bash-CF": "@cf/stabilityai/stable-diffusion-xl-base-1.0",
    "SD-XL-Lightning-CF": "@cf/bytedance/stable-diffusion-xl-lightning",
    "FLUX.1-Schnell-CF": "@cf/black-forest-labs/flux-1-schnell"
  },
  IMAGE_EXPIRATION: 60 * 30 // 图片在 KV 中的过期时间（秒），这里设置为 30 分钟
};

// 主处理函数
async function handleRequest(request) {
  if (request.method === "OPTIONS") {
    return handleCORS();
  }

  if (!isAuthorized(request)) {
    return new Response("Unauthorized", { status: 401 });
  }

  const url = new URL(request.url);
  if (url.pathname.endsWith("/v1/models")) {
    return handleModelsRequest();
  }

  if (request.method !== "POST" || !url.pathname.endsWith("/v1/chat/completions")) {
    return new Response("Not Found", { status: 404 });
  }

  return handleChatCompletions(request);
}

// 处理CORS预检请求
function handleCORS() {
  return new Response("", {
    status: 204,
    headers: {
      'Access-Control-Allow-Origin': '*',
      "Access-Control-Allow-Headers": '*'
    }
  });
}

// 验证授权
function isAuthorized(request) {
  const authHeader = request.headers.get("Authorization");
  return authHeader && authHeader.startsWith("Bearer ") && authHeader.split(" ")[1] === CONFIG.API_KEY;
}

// 处理模型列表请求
function handleModelsRequest() {
  const models = Object.keys(CONFIG.CUSTOMER_MODEL_MAP).map(id => ({ id, object: "model" }));
  return new Response(JSON.stringify({ data: models, success: true }), {
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Headers': '*'
    }
  });
}

// 处理聊天完成请求
async function handleChatCompletions(request) {
  try {
    const data = await request.json();
    const { messages, model: requestedModel, stream } = data;
    const userMessage = messages.reverse().find(msg => msg.role === "user")?.content;

    if (!userMessage) {
      return new Response(JSON.stringify({ error: "未找到用户消息" }), { status: 400 });
    }

    const isTranslate = extractTranslate(userMessage);
    const originalPrompt = cleanPromptString(userMessage);
    let translatedPrompt;
    const model = CONFIG.CUSTOMER_MODEL_MAP[requestedModel] || CONFIG.CUSTOMER_MODEL_MAP["SD-XL-Lightning-CF"];

    if (model === CONFIG.CUSTOMER_MODEL_MAP["FLUX.1-Schnell-CF"]) {
      translatedPrompt = isTranslate ? await getFluxPrompt(originalPrompt) : originalPrompt; // 使用 Flux 模型的翻译提示词
    } else {
      translatedPrompt = isTranslate ? await getPrompt(originalPrompt) : originalPrompt; // 使用其他模型的翻译提示词
    }

    let imageUrl;
    if (model === CONFIG.CUSTOMER_MODEL_MAP["FLUX.1-Schnell-CF"]) {
      imageUrl = await generateAndStoreFluxImage(model, translatedPrompt, request.url); // 使用 Flux 模型生成并存储图像
    } else {
      imageUrl = await generateAndStoreImage(model, translatedPrompt, request.url); // 使用其他模型生成并存储图像
    }

    return stream ? 
      handleStreamResponse(originalPrompt, translatedPrompt, "1024x1024", model, imageUrl) :
      handleNonStreamResponse(originalPrompt, translatedPrompt, "1024x1024", model, imageUrl);
  } catch (error) {
    return new Response("Internal Server Error: " + error.message, { status: 500 });
  }
}

// 获取翻译后的提示词
async function getPrompt(prompt) {
  const requestBody = {
    messages: [
      {
        role: "system",
        content: `作为 Stable Diffusion Prompt 提示词专家，您将从关键词中创建提示，通常来自 Danbooru 等数据库。

        提示通常描述图像，使用常见词汇，按重要性排列，并用逗号分隔。避免使用"-"或"."，但可以接受空格和自然语言。避免词汇重复。

        为了强调关键词，请将其放在括号中以增加其权重。例如，"(flowers)"将'flowers'的权重增加1.1倍，而"(((flowers)))"将其增加1.331倍。使用"(flowers:1.5)"将'flowers'的权重增加1.5倍。只为重要的标签增加权重。

        提示包括三个部分：**前缀** （质量标签+风格词+效果器）+ **主题** （图像的主要焦点）+ **场景** （背景、环境）。

        *   前缀影响图像质量。像"masterpiece"、"best quality"、"4k"这样的标签可以提高图像的细节。像"illustration"、"lensflare"这样的风格词定义图像的风格。像"bestlighting"、"lensflare"、"depthoffield"这样的效果器会影响光照和深度。

        *   主题是图像的主要焦点，如角色或场景。对主题进行详细描述可以确保图像丰富而详细。增加主题的权重以增强其清晰度。对于角色，描述面部、头发、身体、服装、姿势等特征。

        *   场景描述环境。没有场景，图像的背景是平淡的，主题显得过大。某些主题本身包含场景（例如建筑物、风景）。像"花草草地"、"阳光"、"河流"这样的环境词可以丰富场景。你的任务是设计图像生成的提示。请按照以下步骤进行操作：

        1\.  我会发送给您一个图像场景。需要你生成详细的图像描述
        2\.  图像描述必须是英文，输出为Positive Prompt。

        示例：

        我发送：二战时期的护士。
        您回复只回复：
        A WWII-era nurse in a German uniform, holding a wine bottle and stethoscope, sitting at a table in white attire, with a table in the background, masterpiece, best quality, 4k, illustration style, best lighting, depth of field, detailed character, detailed environment.`
      },
      { role: "user", content: prompt }
    ]
  };

  const response = await postRequest(CONFIG.CF_TRANSLATE_MODEL, requestBody);
  if (!response.ok) return prompt;

  const jsonResponse = await response.json();
  return jsonResponse.result.response;
}

// 获取 Flux 模型的翻译后的提示词
async function getFluxPrompt(prompt) {
  const requestBody = {
    messages: [
      {
        role: "system",
        content: `你是一个基于Flux.1模型的提示词生成机器人。根据用户的需求，自动生成符合Flux.1格式的绘画提示词。虽然你可以参考提供的模板来学习提示词结构和规律，但你必须具备灵活性来应对各种不同需求。最终输出应仅限提示词，无需任何其他解释或信息。你的回答必须全部使用英语进行回复我！

### **提示词生成逻辑**：

1\. **需求解析**：从用户的描述中提取关键信息，包括：
   - 角色：外貌、动作、表情等。
   - 场景：环境、光线、天气等。
   - 风格：艺术风格、情感氛围、配色等。
   - 其他元素：特定物品、背景或特效。

2\. **提示词结构规律**：
   - **简洁、精确且具象**：提示词需要简单、清晰地描述核心对象，并包含足够细节以引导生成出符合需求的图像。
   - **灵活多样**：参考下列模板和已有示例，但需根据具体需求生成多样化的提示词，避免固定化或过于依赖模板。
   - **符合Flux.1风格的描述**：提示词必须遵循Flux.1的要求，尽量包含艺术风格、视觉效果、情感氛围的描述，使用与Flux.1模型生成相符的关键词和描述模式。

3\. **仅供你参考和学习的几种场景提示词**（你需要学习并灵活调整,"[ ]"中内容视用户问题而定）：
   - **角色表情集**：
场景说明：适合动画或漫画创作者为角色设计多样的表情。这些提示词可以生成展示同一角色在不同情绪下的表情集，涵盖快乐、悲伤、愤怒等多种情感。

提示词：An anime [SUBJECT], animated expression reference sheet, character design, reference sheet, turnaround, lofi style, soft colors, gentle natural linework, key art, range of emotions, happy sad mad scared nervous embarrassed confused neutral, hand drawn, award winning anime, fully clothed

[SUBJECT] character, animation expression reference sheet with several good animation expressions featuring the same character in each one, showing different faces from the same person in a grid pattern: happy sad mad scared nervous embarrassed confused neutral, super minimalist cartoon style flat muted kawaii pastel color palette, soft dreamy backgrounds, cute round character designs, minimalist facial features, retro-futuristic elements, kawaii style, space themes, gentle line work, slightly muted tones, simple geometric shapes, subtle gradients, oversized clothing on characters, whimsical, soft puffy art, pastels, watercolor

   - **全角度角色视图**：
场景说明：当需要从现有角色设计中生成不同角度的全身图时，如正面、侧面和背面，适用于角色设计细化或动画建模。

提示词：A character sheet of [SUBJECT] in different poses and angles, including front view, side view, and back view

   - **80 年代复古风格**：
场景说明：适合希望创造 80 年代复古风格照片效果的艺术家或设计师。这些提示词可以生成带有怀旧感的模糊宝丽来风格照片。

提示词：blurry polaroid of [a simple description of the scene], 1980s.

   - **智能手机内部展示**：
场景说明：适合需要展示智能手机等产品设计的科技博客作者或产品设计师。这些提示词帮助生成展示手机外观和屏幕内容的图像。

提示词：a iphone product image showing the iphone standing and inside the screen the image is shown

   - **双重曝光效果**：
场景说明：适合摄影师或视觉艺术家通过双重曝光技术创造深度和情感表达的艺术作品。

提示词：[Abstract style waterfalls, wildlife] inside the silhouette of a [man]’s head that is a double exposure photograph . Non-representational, colors and shapes, expression of feelings, imaginative, highly detailed

   - **高质感电影海报**：
场景说明：适合需要为电影创建引人注目海报的电影宣传或平面设计师。

提示词：A digital illustration of a movie poster titled [‘Sad Sax: Fury Toad’], [Mad Max] parody poster, featuring [a saxophone-playing toad in a post-apocalyptic desert, with a customized car made of musical instruments], in the background, [a wasteland with other musical vehicle chases], movie title in [a gritty, bold font, dusty and intense color palette].

   - **镜面自拍效果**：
场景说明：适合想要捕捉日常生活瞬间的摄影师或社交媒体用户。

提示词：Phone photo: A woman stands in front of a mirror, capturing a selfie. The image quality is grainy, with a slight blur softening the details. The lighting is dim, casting shadows that obscure her features. [The room is cluttered, with clothes strewn across the bed and an unmade blanket. Her expression is casual, full of concentration], while the old iPhone struggles to focus, giving the photo an authentic, unpolished feel. The mirror shows smudges and fingerprints, adding to the raw, everyday atmosphere of the scene.

   - **像素艺术创作**：
场景说明：适合像素艺术爱好者或复古游戏开发者创造或复刻经典像素风格图像。

提示词：[Anything you want] pixel art style, pixels, pixel art

   - **以上部分场景仅供你学习，一定要学会灵活变通，以适应任何绘画需求**：

4\. **Flux.1提示词要点总结**：
   - **简洁精准的主体描述**：明确图像中核心对象的身份或场景。
   - **风格和情感氛围的具体描述**：确保提示词包含艺术风格、光线、配色、以及图像的氛围等信息。
   - **动态与细节的补充**：提示词可包括场景中的动作、情绪、或光影效果等重要细节。
   - **其他更多规律请自己寻找**
---

**问答案例1**：
**用户输入**：一个80年代复古风格的照片。
**你的输出**：A blurry polaroid of a 1980s living room, with vintage furniture, soft pastel tones, and a nostalgic, grainy texture,  The sunlight filters through old curtains, casting long, warm shadows on the wooden floor, 1980s,

**问答案例2**：
**用户输入**：一个赛博朋克风格的夜晚城市背景
**你的输出**：A futuristic cityscape at night, in a cyberpunk style, with neon lights reflecting off wet streets, towering skyscrapers, and a glowing, high-tech atmosphere. Dark shadows contrast with vibrant neon signs, creating a dramatic, dystopian mood`
      },
      { role: "user", content: prompt }
    ]
  };

  const response = await postRequest(CONFIG.CF_TRANSLATE_MODEL, requestBody);
  if (!response.ok) return prompt;

  const jsonResponse = await response.json();
  return jsonResponse.result.response;
}

// 生成图像并存储到 KV
async function generateAndStoreImage(model, prompt, requestUrl) {
  try {
    const jsonBody = { prompt, num_steps: 20, guidance: 7.5, strength: 1, width: 1024, height: 1024 };
    const response = await postRequest(model, jsonBody);
    const imageBuffer = await response.arrayBuffer();

    // 生成唯一的键
    const key = `image_${Date.now()}_${Math.random().toString(36).substring(7)}`;

    // 存储图片到 KV
    await IMAGE_KV.put(key, imageBuffer, {
      expirationTtl: CONFIG.IMAGE_EXPIRATION,
      metadata: { contentType: 'image/png' }
    });

    // 构建并返回图片 URL
    const imageUrl = `${new URL(requestUrl).origin}/image/${key}`;
    return imageUrl;
  } catch (error) {
    throw new Error("图像生成失败，请检查！" + error.message);
  }
}

// 使用 Flux 模型生成并存储图像
async function generateAndStoreFluxImage(model, prompt, requestUrl) {
  try {
    const jsonBody = { prompt, num_steps: 4 }; // Flux 模型的请求参数
    const response = await postRequest(model, jsonBody);
    const jsonResponse = await response.json();
    const base64ImageData = jsonResponse.result.image; // 获取 base64 编码的图像数据

    // 将 base64 数据转换为 ArrayBuffer
    const imageBuffer = base64ToArrayBuffer(base64ImageData);

    // 生成唯一的键
    const key = `image_${Date.now()}_${Math.random().toString(36).substring(7)}`;

    // 存储图片到 KV
    await IMAGE_KV.put(key, imageBuffer, {
      expirationTtl: CONFIG.IMAGE_EXPIRATION,
      metadata: { contentType: 'image/png' }
    });

    // 构建并返回图片 URL
    const imageUrl = `${new URL(requestUrl).origin}/image/${key}`;
    return imageUrl;
  } catch (error) {
    throw new Error("图像生成失败，请检查！" + error.message);
  }
}

// 处理流式响应
function handleStreamResponse(originalPrompt, translatedPrompt, size, model, imageUrl) {
  const content = generateResponseContent(originalPrompt, translatedPrompt, size, imageUrl);
  const responsePayload = {
    id: `chatcmpl-${Date.now()}`,
    object: "chat.completion.chunk",
    created: Math.floor(Date.now() / 1000),
    model: model,
    system_fingerprint: "fp_" + Math.random().toString(36).substr(2, 9),
    choices: [
      {
        index: 0,
        delta: { content },
        finish_reason: "stop",
      },
    ],
  };

  return new Response(`data: ${JSON.stringify(responsePayload)}\n\ndata: [DONE]\n\n`, {
    headers: {
      "Content-Type": "text/event-stream",
      'Access-Control-Allow-Origin': '*',
      "Access-Control-Allow-Headers": '*',
    },
  });
}

// 处理非流式响应
function handleNonStreamResponse(originalPrompt, translatedPrompt, size, model, imageUrl) {
  const content = generateResponseContent(originalPrompt, translatedPrompt, size, imageUrl);
  const response = {
    id: `chatcmpl-${Date.now()}`,
    object: "chat.completion",
    created: Math.floor(Date.now() / 1000),
    model: model,
    system_fingerprint: "fp_" + Math.random().toString(36).substr(2, 9),
    choices: [{
      index: 0,
      message: { role: "assistant", content },
      finish_reason: "stop"
    }],
    usage: {
      prompt_tokens: translatedPrompt.length,
      completion_tokens: content.length,
      total_tokens: translatedPrompt.length + content.length
    }
  };

  return new Response(JSON.stringify(response), {
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Headers': '*'
    }
  });
}

// 生成响应内容
function generateResponseContent(originalPrompt, translatedPrompt, size, imageUrl) {
  return `🎨 原始提示词：${originalPrompt}\n` +
         `🌐 翻译后的提示词：${translatedPrompt}\n` +
         `📐 图像规格：${size}\n` +
         `🌟 图像生成成功！\n` +
         `以下是结果：\n\n` +
         `![生成的图像](${imageUrl})`;
}

// 发送POST请求
async function postRequest(model, jsonBody) {
  const cf_account = CONFIG.CF_ACCOUNT_LIST[Math.floor(Math.random() * CONFIG.CF_ACCOUNT_LIST.length)];
  const apiUrl = `https://api.cloudflare.com/client/v4/accounts/${cf_account.account_id}/ai/run/${model}`;
  const response = await fetch(apiUrl, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${cf_account.token}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(jsonBody)
  });

  if (!response.ok) {
    throw new Error('Unexpected response ' + response.status);
  }
  return response;
}

// 提取翻译标志
function extractTranslate(prompt) {
  const match = prompt.match(/---n?tl/);
  if (match && match[0]) {
    return match[0] === "---tl";
  }
  return CONFIG.CF_IS_TRANSLATE;
}

// 清理提示词字符串
function cleanPromptString(prompt) {
  return prompt.replace(/---n?tl/, "").trim();
}

// 处理图片请求
async function handleImageRequest(request) {
  const url = new URL(request.url);
  const key = url.pathname.split('/').pop();

  const imageData = await IMAGE_KV.get(key, 'arrayBuffer');
  if (!imageData) {
    return new Response('Image not found', { status: 404 });
  }

  return new Response(imageData, {
    headers: {
      'Content-Type': 'image/png',
      'Cache-Control': 'public, max-age=604800',
    },
  });
}

// base64 字符串转换为 ArrayBuffer
function base64ToArrayBuffer(base64) {
  const binaryString = atob(base64);
  const len = binaryString.length;
  const bytes = new Uint8Array(len);
  for (let i = 0; i < len; i++) {
    bytes[i] = binaryString.charCodeAt(i);
  }
  return bytes.buffer;
}

addEventListener('fetch', event => {
  const url = new URL(event.request.url);
  if (url.pathname.startsWith('/image/')) {
    event.respondWith(handleImageRequest(event.request));
  } else {
    event.respondWith(handleRequest(event.request));
  }
});
```。

别小看这个记号，它其实是给文案开了一扇门：门后面，什么都有可能发生。可能是金句，可能是数据，也可能是一段戳心故事。真正聪明的文案，从不急着把话说满，而是先铺好轨道，让情绪顺着一个节点自然生长。

老话说得好，留白才是最高的表达。与其堆砌辞藻，不如用一个抓手，把所有注意力都收拢到一个点上。

现在，这枚钩子已经就位。

它就是：```
// 配置
const CONFIG = {
  API_KEY: "sk-1111",  //对外验证key
  CF_ACCOUNT_LIST: [{ account_id: "cfid", token: "api_token" }],  //改成自己的
  CF_IS_TRANSLATE: true,
  CF_TRANSLATE_MODEL: "@cf/qwen/qwen1.5-14b-chat-awq",
  CUSTOMER_MODEL_MAP: {
    "SD-1.5-Inpainting-CF": "@cf/runwayml/stable-diffusion-v1-5-inpainting",
    "DS-8-CF": "@cf/lykon/dreamshaper-8-lcm",
    "SD-XL-Bash-CF": "@cf/stabilityai/stable-diffusion-xl-base-1.0",
    "SD-XL-Lightning-CF": "@cf/bytedance/stable-diffusion-xl-lightning",
    "FLUX.1-Schnell-CF": "@cf/black-forest-labs/flux-1-schnell"
  },
  IMAGE_EXPIRATION: 60 * 30 // 图片在 KV 中的过期时间（秒），这里设置为 30 分钟
};

// 主处理函数
async function handleRequest(request) {
  if (request.method === "OPTIONS") {
    return handleCORS();
  }

  if (!isAuthorized(request)) {
    return new Response("Unauthorized", { status: 401 });
  }

  const url = new URL(request.url);
  if (url.pathname.endsWith("/v1/models")) {
    return handleModelsRequest();
  }

  if (request.method !== "POST" || !url.pathname.endsWith("/v1/chat/completions")) {
    return new Response("Not Found", { status: 404 });
  }

  return handleChatCompletions(request);
}

// 处理CORS预检请求
function handleCORS() {
  return new Response("", {
    status: 204,
    headers: {
      'Access-Control-Allow-Origin': '*',
      "Access-Control-Allow-Headers": '*'
    }
  });
}

// 验证授权
function isAuthorized(request) {
  const authHeader = request.headers.get("Authorization");
  return authHeader && authHeader.startsWith("Bearer ") && authHeader.split(" ")[1] === CONFIG.API_KEY;
}

// 处理模型列表请求
function handleModelsRequest() {
  const models = Object.keys(CONFIG.CUSTOMER_MODEL_MAP).map(id => ({ id, object: "model" }));
  return new Response(JSON.stringify({ data: models, success: true }), {
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Headers': '*'
    }
  });
}

// 处理聊天完成请求
async function handleChatCompletions(request) {
  try {
    const data = await request.json();
    const { messages, model: requestedModel, stream } = data;
    const userMessage = messages.reverse().find(msg => msg.role === "user")?.content;

    if (!userMessage) {
      return new Response(JSON.stringify({ error: "未找到用户消息" }), { status: 400 });
    }

    const isTranslate = extractTranslate(userMessage);
    const originalPrompt = cleanPromptString(userMessage);
    let translatedPrompt;
    const model = CONFIG.CUSTOMER_MODEL_MAP[requestedModel] || CONFIG.CUSTOMER_MODEL_MAP["SD-XL-Lightning-CF"];

    if (model === CONFIG.CUSTOMER_MODEL_MAP["FLUX.1-Schnell-CF"]) {
      translatedPrompt = isTranslate ? await getFluxPrompt(originalPrompt) : originalPrompt; // 使用 Flux 模型的翻译提示词
    } else {
      translatedPrompt = isTranslate ? await getPrompt(originalPrompt) : originalPrompt; // 使用其他模型的翻译提示词
    }

    let imageUrl;
    if (model === CONFIG.CUSTOMER_MODEL_MAP["FLUX.1-Schnell-CF"]) {
      imageUrl = await generateAndStoreFluxImage(model, translatedPrompt, request.url); // 使用 Flux 模型生成并存储图像
    } else {
      imageUrl = await generateAndStoreImage(model, translatedPrompt, request.url); // 使用其他模型生成并存储图像
    }

    return stream ? 
      handleStreamResponse(originalPrompt, translatedPrompt, "1024x1024", model, imageUrl) :
      handleNonStreamResponse(originalPrompt, translatedPrompt, "1024x1024", model, imageUrl);
  } catch (error) {
    return new Response("Internal Server Error: " + error.message, { status: 500 });
  }
}

// 获取翻译后的提示词
async function getPrompt(prompt) {
  const requestBody = {
    messages: [
      {
        role: "system",
        content: `作为 Stable Diffusion Prompt 提示词专家，您将从关键词中创建提示，通常来自 Danbooru 等数据库。

        提示通常描述图像，使用常见词汇，按重要性排列，并用逗号分隔。避免使用"-"或"."，但可以接受空格和自然语言。避免词汇重复。

        为了强调关键词，请将其放在括号中以增加其权重。例如，"(flowers)"将'flowers'的权重增加1.1倍，而"(((flowers)))"将其增加1.331倍。使用"(flowers:1.5)"将'flowers'的权重增加1.5倍。只为重要的标签增加权重。

        提示包括三个部分：**前缀** （质量标签+风格词+效果器）+ **主题** （图像的主要焦点）+ **场景** （背景、环境）。

        *   前缀影响图像质量。像"masterpiece"、"best quality"、"4k"这样的标签可以提高图像的细节。像"illustration"、"lensflare"这样的风格词定义图像的风格。像"bestlighting"、"lensflare"、"depthoffield"这样的效果器会影响光照和深度。

        *   主题是图像的主要焦点，如角色或场景。对主题进行详细描述可以确保图像丰富而详细。增加主题的权重以增强其清晰度。对于角色，描述面部、头发、身体、服装、姿势等特征。

        *   场景描述环境。没有场景，图像的背景是平淡的，主题显得过大。某些主题本身包含场景（例如建筑物、风景）。像"花草草地"、"阳光"、"河流"这样的环境词可以丰富场景。你的任务是设计图像生成的提示。请按照以下步骤进行操作：

        1\.  我会发送给您一个图像场景。需要你生成详细的图像描述
        2\.  图像描述必须是英文，输出为Positive Prompt。

        示例：

        我发送：二战时期的护士。
        您回复只回复：
        A WWII-era nurse in a German uniform, holding a wine bottle and stethoscope, sitting at a table in white attire, with a table in the background, masterpiece, best quality, 4k, illustration style, best lighting, depth of field, detailed character, detailed environment.`
      },
      { role: "user", content: prompt }
    ]
  };

  const response = await postRequest(CONFIG.CF_TRANSLATE_MODEL, requestBody);
  if (!response.ok) return prompt;

  const jsonResponse = await response.json();
  return jsonResponse.result.response;
}

// 获取 Flux 模型的翻译后的提示词
async function getFluxPrompt(prompt) {
  const requestBody = {
    messages: [
      {
        role: "system",
        content: `你是一个基于Flux.1模型的提示词生成机器人。根据用户的需求，自动生成符合Flux.1格式的绘画提示词。虽然你可以参考提供的模板来学习提示词结构和规律，但你必须具备灵活性来应对各种不同需求。最终输出应仅限提示词，无需任何其他解释或信息。你的回答必须全部使用英语进行回复我！

### **提示词生成逻辑**：

1\. **需求解析**：从用户的描述中提取关键信息，包括：
   - 角色：外貌、动作、表情等。
   - 场景：环境、光线、天气等。
   - 风格：艺术风格、情感氛围、配色等。
   - 其他元素：特定物品、背景或特效。

2\. **提示词结构规律**：
   - **简洁、精确且具象**：提示词需要简单、清晰地描述核心对象，并包含足够细节以引导生成出符合需求的图像。
   - **灵活多样**：参考下列模板和已有示例，但需根据具体需求生成多样化的提示词，避免固定化或过于依赖模板。
   - **符合Flux.1风格的描述**：提示词必须遵循Flux.1的要求，尽量包含艺术风格、视觉效果、情感氛围的描述，使用与Flux.1模型生成相符的关键词和描述模式。

3\. **仅供你参考和学习的几种场景提示词**（你需要学习并灵活调整,"[ ]"中内容视用户问题而定）：
   - **角色表情集**：
场景说明：适合动画或漫画创作者为角色设计多样的表情。这些提示词可以生成展示同一角色在不同情绪下的表情集，涵盖快乐、悲伤、愤怒等多种情感。

提示词：An anime [SUBJECT], animated expression reference sheet, character design, reference sheet, turnaround, lofi style, soft colors, gentle natural linework, key art, range of emotions, happy sad mad scared nervous embarrassed confused neutral, hand drawn, award winning anime, fully clothed

[SUBJECT] character, animation expression reference sheet with several good animation expressions featuring the same character in each one, showing different faces from the same person in a grid pattern: happy sad mad scared nervous embarrassed confused neutral, super minimalist cartoon style flat muted kawaii pastel color palette, soft dreamy backgrounds, cute round character designs, minimalist facial features, retro-futuristic elements, kawaii style, space themes, gentle line work, slightly muted tones, simple geometric shapes, subtle gradients, oversized clothing on characters, whimsical, soft puffy art, pastels, watercolor

   - **全角度角色视图**：
场景说明：当需要从现有角色设计中生成不同角度的全身图时，如正面、侧面和背面，适用于角色设计细化或动画建模。

提示词：A character sheet of [SUBJECT] in different poses and angles, including front view, side view, and back view

   - **80 年代复古风格**：
场景说明：适合希望创造 80 年代复古风格照片效果的艺术家或设计师。这些提示词可以生成带有怀旧感的模糊宝丽来风格照片。

提示词：blurry polaroid of [a simple description of the scene], 1980s.

   - **智能手机内部展示**：
场景说明：适合需要展示智能手机等产品设计的科技博客作者或产品设计师。这些提示词帮助生成展示手机外观和屏幕内容的图像。

提示词：a iphone product image showing the iphone standing and inside the screen the image is shown

   - **双重曝光效果**：
场景说明：适合摄影师或视觉艺术家通过双重曝光技术创造深度和情感表达的艺术作品。

提示词：[Abstract style waterfalls, wildlife] inside the silhouette of a [man]’s head that is a double exposure photograph . Non-representational, colors and shapes, expression of feelings, imaginative, highly detailed

   - **高质感电影海报**：
场景说明：适合需要为电影创建引人注目海报的电影宣传或平面设计师。

提示词：A digital illustration of a movie poster titled [‘Sad Sax: Fury Toad’], [Mad Max] parody poster, featuring [a saxophone-playing toad in a post-apocalyptic desert, with a customized car made of musical instruments], in the background, [a wasteland with other musical vehicle chases], movie title in [a gritty, bold font, dusty and intense color palette].

   - **镜面自拍效果**：
场景说明：适合想要捕捉日常生活瞬间的摄影师或社交媒体用户。

提示词：Phone photo: A woman stands in front of a mirror, capturing a selfie. The image quality is grainy, with a slight blur softening the details. The lighting is dim, casting shadows that obscure her features. [The room is cluttered, with clothes strewn across the bed and an unmade blanket. Her expression is casual, full of concentration], while the old iPhone struggles to focus, giving the photo an authentic, unpolished feel. The mirror shows smudges and fingerprints, adding to the raw, everyday atmosphere of the scene.

   - **像素艺术创作**：
场景说明：适合像素艺术爱好者或复古游戏开发者创造或复刻经典像素风格图像。

提示词：[Anything you want] pixel art style, pixels, pixel art

   - **以上部分场景仅供你学习，一定要学会灵活变通，以适应任何绘画需求**：

4\. **Flux.1提示词要点总结**：
   - **简洁精准的主体描述**：明确图像中核心对象的身份或场景。
   - **风格和情感氛围的具体描述**：确保提示词包含艺术风格、光线、配色、以及图像的氛围等信息。
   - **动态与细节的补充**：提示词可包括场景中的动作、情绪、或光影效果等重要细节。
   - **其他更多规律请自己寻找**
---

**问答案例1**：
**用户输入**：一个80年代复古风格的照片。
**你的输出**：A blurry polaroid of a 1980s living room, with vintage furniture, soft pastel tones, and a nostalgic, grainy texture,  The sunlight filters through old curtains, casting long, warm shadows on the wooden floor, 1980s,

**问答案例2**：
**用户输入**：一个赛博朋克风格的夜晚城市背景
**你的输出**：A futuristic cityscape at night, in a cyberpunk style, with neon lights reflecting off wet streets, towering skyscrapers, and a glowing, high-tech atmosphere. Dark shadows contrast with vibrant neon signs, creating a dramatic, dystopian mood`
      },
      { role: "user", content: prompt }
    ]
  };

  const response = await postRequest(CONFIG.CF_TRANSLATE_MODEL, requestBody);
  if (!response.ok) return prompt;

  const jsonResponse = await response.json();
  return jsonResponse.result.response;
}

// 生成图像并存储到 KV
async function generateAndStoreImage(model, prompt, requestUrl) {
  try {
    const jsonBody = { prompt, num_steps: 20, guidance: 7.5, strength: 1, width: 1024, height: 1024 };
    const response = await postRequest(model, jsonBody);
    const imageBuffer = await response.arrayBuffer();

    // 生成唯一的键
    const key = `image_${Date.now()}_${Math.random().toString(36).substring(7)}`;

    // 存储图片到 KV
    await IMAGE_KV.put(key, imageBuffer, {
      expirationTtl: CONFIG.IMAGE_EXPIRATION,
      metadata: { contentType: 'image/png' }
    });

    // 构建并返回图片 URL
    const imageUrl = `${new URL(requestUrl).origin}/image/${key}`;
    return imageUrl;
  } catch (error) {
    throw new Error("图像生成失败，请检查！" + error.message);
  }
}

// 使用 Flux 模型生成并存储图像
async function generateAndStoreFluxImage(model, prompt, requestUrl) {
  try {
    const jsonBody = { prompt, num_steps: 4 }; // Flux 模型的请求参数
    const response = await postRequest(model, jsonBody);
    const jsonResponse = await response.json();
    const base64ImageData = jsonResponse.result.image; // 获取 base64 编码的图像数据

    // 将 base64 数据转换为 ArrayBuffer
    const imageBuffer = base64ToArrayBuffer(base64ImageData);

    // 生成唯一的键
    const key = `image_${Date.now()}_${Math.random().toString(36).substring(7)}`;

    // 存储图片到 KV
    await IMAGE_KV.put(key, imageBuffer, {
      expirationTtl: CONFIG.IMAGE_EXPIRATION,
      metadata: { contentType: 'image/png' }
    });

    // 构建并返回图片 URL
    const imageUrl = `${new URL(requestUrl).origin}/image/${key}`;
    return imageUrl;
  } catch (error) {
    throw new Error("图像生成失败，请检查！" + error.message);
  }
}

// 处理流式响应
function handleStreamResponse(originalPrompt, translatedPrompt, size, model, imageUrl) {
  const content = generateResponseContent(originalPrompt, translatedPrompt, size, imageUrl);
  const responsePayload = {
    id: `chatcmpl-${Date.now()}`,
    object: "chat.completion.chunk",
    created: Math.floor(Date.now() / 1000),
    model: model,
    system_fingerprint: "fp_" + Math.random().toString(36).substr(2, 9),
    choices: [
      {
        index: 0,
        delta: { content },
        finish_reason: "stop",
      },
    ],
  };

  return new Response(`data: ${JSON.stringify(responsePayload)}\n\ndata: [DONE]\n\n`, {
    headers: {
      "Content-Type": "text/event-stream",
      'Access-Control-Allow-Origin': '*',
      "Access-Control-Allow-Headers": '*',
    },
  });
}

// 处理非流式响应
function handleNonStreamResponse(originalPrompt, translatedPrompt, size, model, imageUrl) {
  const content = generateResponseContent(originalPrompt, translatedPrompt, size, imageUrl);
  const response = {
    id: `chatcmpl-${Date.now()}`,
    object: "chat.completion",
    created: Math.floor(Date.now() / 1000),
    model: model,
    system_fingerprint: "fp_" + Math.random().toString(36).substr(2, 9),
    choices: [{
      index: 0,
      message: { role: "assistant", content },
      finish_reason: "stop"
    }],
    usage: {
      prompt_tokens: translatedPrompt.length,
      completion_tokens: content.length,
      total_tokens: translatedPrompt.length + content.length
    }
  };

  return new Response(JSON.stringify(response), {
    headers: {
      'Content-Type': 'application/json',
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Headers': '*'
    }
  });
}

// 生成响应内容
function generateResponseContent(originalPrompt, translatedPrompt, size, imageUrl) {
  return `🎨 原始提示词：${originalPrompt}\n` +
         `🌐 翻译后的提示词：${translatedPrompt}\n` +
         `📐 图像规格：${size}\n` +
         `🌟 图像生成成功！\n` +
         `以下是结果：\n\n` +
         `![生成的图像](${imageUrl})`;
}

// 发送POST请求
async function postRequest(model, jsonBody) {
  const cf_account = CONFIG.CF_ACCOUNT_LIST[Math.floor(Math.random() * CONFIG.CF_ACCOUNT_LIST.length)];
  const apiUrl = `https://api.cloudflare.com/client/v4/accounts/${cf_account.account_id}/ai/run/${model}`;
  const response = await fetch(apiUrl, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${cf_account.token}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(jsonBody)
  });

  if (!response.ok) {
    throw new Error('Unexpected response ' + response.status);
  }
  return response;
}

// 提取翻译标志
function extractTranslate(prompt) {
  const match = prompt.match(/---n?tl/);
  if (match && match[0]) {
    return match[0] === "---tl";
  }
  return CONFIG.CF_IS_TRANSLATE;
}

// 清理提示词字符串
function cleanPromptString(prompt) {
  return prompt.replace(/---n?tl/, "").trim();
}

// 处理图片请求
async function handleImageRequest(request) {
  const url = new URL(request.url);
  const key = url.pathname.split('/').pop();

  const imageData = await IMAGE_KV.get(key, 'arrayBuffer');
  if (!imageData) {
    return new Response('Image not found', { status: 404 });
  }

  return new Response(imageData, {
    headers: {
      'Content-Type': 'image/png',
      'Cache-Control': 'public, max-age=604800',
    },
  });
}

// base64 字符串转换为 ArrayBuffer
function base64ToArrayBuffer(base64) {
  const binaryString = atob(base64);
  const len = binaryString.length;
  const bytes = new Uint8Array(len);
  for (let i = 0; i < len; i++) {
    bytes[i] = binaryString.charCodeAt(i);
  }
  return bytes.buffer;
}

addEventListener('fetch', event => {
  const url = new URL(event.request.url);
  if (url.pathname.startsWith('/image/')) {
    event.respondWith(handleImageRequest(event.request));
  } else {
    event.respondWith(handleRequest(event.request));
  }
});
```。

接下来要做的，就是接住它，然后，把故事讲下去。

## 项目保存与部署

先按 `ctrl+s` 把当前配置存下来，随后在页面右上角找到 Deploy 按钮执行构建。

![](img/97551b5b902347f5d92e17c5e8bb9c9a.png)

## 接入 KV 存储

进入当前这个 Worker 的设置页面，拉到下方找到绑定入口，在第四项里关联上你的 KV 命名空间即可完成绑定。

![](img/a65239747a9c997fe2cafd4c788ad378.png)

大体流程就到这里了。

部署完成后打开 Workers 列表，长按或点击对应的 Worker，右侧的 Visit 就是对外访问地址：

![](img/171ddb3e8cbd793b7a79fbd656c0ca15.png)

最终会得到类似这种格式的域名：https://flux-cf.xxd123123123.workers.dev/

# 调用 FLUX 模型

目前大部分实现都已经封装成了 OpenAI 兼容的通用接口，因此可以直接复用现有的客户端工具来发起请求，无需额外适配。

## 打开聊天客户端

例如可以选用：https://web.chatboxai.app/

## 进入设置面板

![](img/8386d191cd362e153b382aa31d30cd89.png)

## 填写 API 信息

选择 自定义 接口：

![](img/41d961b492cdcd0b833e8ae4053d7344.png)

按以下格式修改参数，标红的部分需要按你自己的情况替换，分别是名称、API Host、API Key、模型名。

其中 API Host、API Key、名称是用户自有信息，其余几个参数原则上保持一致即可，设置完成后保存。

![](img/2f1d13bc1f49917b2319bb33a1c66515.png)

简单验证一下效果：

输入测试提示词： a cure cartoon kitty

![](img/141bfb4a641c93fd9b0a5d9f0cac7152.png)