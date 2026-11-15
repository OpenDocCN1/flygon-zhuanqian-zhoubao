# 别猜了！用AI把小红书评论区变成你的“客户心声解码器”
你好，我是龙哥
“客户葫芦里到底卖的什么药？”“聊得好好的，怎么一到掏钱就沉默？”“凭什么是我们？”
干项目的人，十有八九都卡在同一个地方——看不透用户。嘴上说的和心里想的，经常是两码事。嫌价格贵，说不定是怕买了不值；说再想想，往往是没戳到那个让他心动的点。
哆元这些年见到不少老板，连用户最在意的痛点都说不明白，更别提找到让用户下单的理由了，全链路做得糊里糊涂。
那到底有没有一条路，能帮我们把用户的心思摸透？想通了这一点，前段投放、内容获客就有了方向。
今天给大家的这套玩法，就是要解决这个事儿，全程分两条路：
一、先用AI把小红书评论区拆了再分析产出
二、全程交给AI直接干
# 一、先用AI把小红书评论区拆了再分析产出
一条笔记，很多人只盯着图、标题、正文，却忽略了评论区这座金矿。评论区能干啥？
1、拉新的入口：把人引到私信、群聊、评论互动、主页参观
2、抢客的战场：私信截流、冒充用户在评论区拦人
3、素材的宝库：把精彩评论截下来当封面、当配图、当信任背书
4、选题的雷达：从热聊话题找到新钩子
5、需求的探测器：发现那些用户自己都没意识到的潜在诉求
## 把评论区内容先批量抓下来，第三招最狠
没有数据就别谈分析。下面三招，门槛都不高，复杂的代码工具直接跳过——越麻烦越没人愿意碰。如果你有更好用的，也可以直接用，跳到分析部分就行。
### 1、Kimi总结助手插件，适合评论不多的场景
这是浏览器拓展商店里的一个小工具，Chrome支持。别小看它，玩法很多，以后我再专门展开聊。
![](img/zhuanqian_a6a61f98500e9dabdeda4bd7e09ca004.png)
在浏览器里找到扩展程序入口
![](img/zhuanqian_c348d5494674eb50df200241fa8219d3.png)
点进扩展程序管理页
![](img/zhuanqian_b3528ac2dd9725359b830159c849462f.png)
把开发者模式打开，再进应用商店。谷歌浏览器得先搞定网络环境，搜“kimi网页”就行
![](img/zhuanqian_9ba0c3fd6632ba938d300736d9013271.png)
选好之后点添加
![](img/zhuanqian_68b75a58f90ea89b005ebd558810db7a.png)
![](img/zhuanqian_315c0905d1925d80aa457976df43e4fc.png)
装完就是可用状态了
要用的时候，再去扩展程序那边
![](img/zhuanqian_46b0c6e4abd4177bd562e7bd22a63f6f.png)
点一下这个插件图标
![](img/zhuanqian_6bb8891941def8599b1e393cc6082fc5.png)
头一回用要用kimi账号登录，登一下就完事
点击之后它会读取页面，不过这次的重点是，咱们能提前在插件里塞好提示词
![](img/zhuanqian_e987f5d6e814803b365fe00666fe4203.png)
里面有个可以输入提示词的入口
![](img/zhuanqian_ced94a56db451860fd9790330df0a6c0.png)
默认是初始状态，可以改成自己想要的
提示词参考这段：
读取网页中评论区的所有信息，只需要评论区的内容，不要作者昵称和其他数据，然后从上至下输出，一个不差的输出出来，不限制个数，如果有300条，则输出300条，不要节省篇幅
这里有个细节得提醒一下，不然很多朋友会卡壳
我随便找了篇笔记来试
![](img/zhuanqian_65203107d224e80cc1f87664946f49ee.png)
看出问题没，明明50多条评论，结果只抓到11条
原因是网页抓取按屏幕显示来，没展开的子评论、没往下滚动加载的内容，kimi根本看不见。怎么破？
先把所有能展开的评论展平，然后从顶部一路滑到底部，再让插件干活
![](img/zhuanqian_f6f394d3ca9ebff35acc5f7cb2bc06b3.png)
这回就全了。再拿更多评论的笔记试一下稳定性
![](img/zhuanqian_4038e775ac4c743f0eb759b1d99baa28.png)
实测下来，大概捞到一百来条它就停了，AI单次输出有限。要是评论量多，直接用第三种方案
另外注意，图片和@信息它是不管的
抓到的内容，直接点最下面复制带走
![](img/zhuanqian_b15028db39adc46372e837af85ba5325.png)
拿旅游包车相关的笔记举个例子
![](img/zhuanqian_898577ceb13afca08129b8d4f6f834ff.png)
这篇下面全是想去洱海的用户留言，总数288条，但kimi总结助手我反复试过多次，封顶一百出头。想要更全面的分析，还是直接看第三种方式
![](img/zhuanqian_71eb627436b5ebec4361448d38253053.png)
到这里，评论数据就算到手了。后面可以丢给Claude、ChatGPT、豆包这些AI做进一步分析
可能有朋友会问：能不能就在kimi总结助手里直接做分析？理论上行，但我更推荐把评论复制到其他AI里跑，kimi的表现不太稳定。想试的话，把下面那段分析提示词粘进去也行
### 2、Instant Data Scraper抓取插件
这玩意是专门做网页信息爬取的，在Chrome商店搜“Instant Data Scraper”
![](img/zhuanqian_b8bff3b7c09ce8253c45a24212d06195.png)
进去把它加上
![](img/zhuanqian_8fbb7b9fd4199cb959f97338482b26bb.png)
装好之后，记得把它打开。不用的时候建议关掉，别影响其他页面的操作
![](img/zhuanqian_317b90e3aa40bd1fef22760696a6197b.png)
还是刚才那个包车笔记，打开插件，能看到它把评论区框选出来了。逻辑和kimi总结助手类似，得先把评论区滑到底，想抓子评论的话，也得提前展开
它的短板在于子评论只能抓一条，但主评论能全部捞完。比如下面这个例子共有92条主评论，要想全量获取，就上第三种方法
![](img/zhuanqian_b8c1137c22e78b37d615b38a2086e3fe.png)
弄完可以导出成表格，也能直接在下方预览区勾选某一列内容复制
下载下来的文件长这样
![](img/zhuanqian_ca325c38104cc65900f898f06a181e5e.png)
主评论集中在那一列
![](img/zhuanqian_34d214c314da18533aedf4428a16c28e.png)
直接复制这一列就行，嫌麻烦的话也可以在插件弹窗里直接复制，那边更快
![](img/zhuanqian_b2dc69484cee42f60975e64b525c8057.png)
这么操作下来，主评论加第一条子评论就都拿到了
### 3、用AI写一个油猴脚本来挖评论
#### 先把油猴装上
建议用Chrome或者Firefox，搜Tampermonkey油猴脚本插件，认准这个
![](img/zhuanqian_3e7f5bb8360955622a50802dac81f6af.png)
进去之后点去商店下载
![](img/zhuanqian_a936c6164881c52aff644c6f77398778.png)
装好就行
![](img/zhuanqian_00848e832371f1f2bbc71de590dfa8ab.png)
再回扩展程序确认它处于启用状态
![](img/zhuanqian_534bf24e9f8371c4a8456e4d7fbc3ba0.png)
油猴到手后，可以先了解一下这家伙的用途
![](img/zhuanqian_0c6a1e5780e74191395f3b3ae20d98a3.png)
#### 怎么新建一个脚本
篡改猴安装完成，浏览器右上角就能看到它
![](img/zhuanqian_4187477ef1bf901c03234b93044966bc.png)
点一下，会出现“添加新脚本”和“管理面板”两个选项
![](img/zhuanqian_5edb6bc6c5f1e584de8e5091d69f1ab7.png)
点“添加新脚本”就会进到这个编辑界面，平时把代码贴进去，再按Ctrl+S保存，就能用了
![](img/zhuanqian_d12478765e8968729b9e3d6ab5c0ac50.png)
“管理面板”则是用来管理我们已经写好的脚本，比如停用、改代码
![](img/zhuanqian_fab977e339490eed52b409c68baec4ae.png)
提醒一句：每次改完代码保存后，回到页面需要刷新一下才会生效。如果管理面板没出现，就再让AI重新给一遍完整代码
去小红书网页版注册个新号登录：https://www.xiaohongshu.com/
按上面的步骤新建好脚本后，打开任意一篇笔记，右下角就会出现采集按钮，点它就开抓
![](img/zhuanqian_8115fb7947055e3a753709884413ff42.png)
![](img/zhuanqian_e564f739c66e48b7d78ecfa559c73d96.png)
#### 所需代码
有时候，最吊人胃口的，不是一句惊天动地的话，而是一个没头没尾的开始。
就像现在，摆在我面前的“素材”，干净得像一张白纸，只留下一个孤零零的记号——```
// ==UserScript==
// @name         小红书评论采集助手v1.2
// @namespace    http://tampermonkey.net/
// @version      1.2
// @description  提取小红书笔记所有评论
// @author       哆元
// @match        *://*.xiaohongshu.com/*
// @match        *://*.xiaoshujiang.com/*
// @grant        GM_download
// @grant        GM_addStyle
// ==/UserScript==
(function() {
'use strict';
// 配置选项
const CONFIG = {
scrollInterval: 1000,
retryDelay: 2000,
maxRetries: 3,
batchSize: 100,
autoSave: true,
maxCommentsPerFile: 10000
};
// 添加自定义样式
GM_addStyle(`
#start-collection-btn {
position: fixed;
bottom: 20px;
right: 20px;
padding: 10px 20px;
background-color: #007bff;
color: white;
border: none;
border-radius: 5px;
cursor: pointer;
z-index: 1000;
}
#start-collection-btn:hover {
background-color: #0056b3;
}
#stop-collection-btn {
position: fixed;
bottom: 80px;
right: 20px;
padding: 10px 20px;
background-color: #dc3545;
color: white;
border: none;
border-radius: 5px;
cursor: pointer;
z-index: 1000;
display: none;
}
#stop-collection-btn:hover {
background-color: #c82333;
}
#progress-box {
position: fixed;
bottom: 140px;
right: 20px;
padding: 10px 20px;
background-color: #28a745;
color: white;
border-radius: 5px;
z-index: 1000;
display: none;
}
#comment-count-box {
position: fixed;
bottom: 190px;
right: 20px;
padding: 10px 20px;
background-color: #ffc107;
color: black;
border-radius: 5px;
z-index: 1000;
display: none;
}
#status-box {
position: fixed;
bottom: 240px;
right: 20px;
padding: 10px 20px;
background-color: #17a2b8;
color: white;
border-radius: 5px;
z-index: 1000;
display: none;
}
`);
// 全局变量
let commentList = [];
let isCollecting = false;
let isPageVisible = true;
let worker = null;
let lastSaveTime = Date.now();
// 创建UI元素
const startButton = document.createElement('button');
startButton.id = 'start-collection-btn';
startButton.innerText = '开始采集';
document.body.appendChild(startButton);
const stopButton = document.createElement('button');
stopButton.id = 'stop-collection-btn';
stopButton.innerText = '结束采集并导出';
document.body.appendChild(stopButton);
const progressBox = document.createElement('div');
progressBox.id = 'progress-box';
progressBox.innerText = '采集进度：等待开始';
document.body.appendChild(progressBox);
const commentCountBox = document.createElement('div');
commentCountBox.id = 'comment-count-box';
commentCountBox.innerText = '当前采集到0条评论';
document.body.appendChild(commentCountBox);
const statusBox = document.createElement('div');
statusBox.id = 'status-box';
statusBox.innerHTML = `
采集速度: 0 条/秒
预计剩余时间: 计算中
`;
document.body.appendChild(statusBox);
// 防抖函数
function debounce(func, wait) {
let timeout;
return function executedFunction(...args) {
const later = () => {
clearTimeout(timeout);
func(...args);
};
clearTimeout(timeout);
timeout = setTimeout(later, wait);
};
}
// 获取总评论数
function getTotalComments() {
const countElement = document.querySelector('span.count');
if (countElement) {
return parseInt(countElement.textContent.trim(), 10) || 0;
}
return 0;
}
// 创建和初始化 Web Worker
function initializeWorker() {
try {
const workerCode = `
let timer = null;
self.onmessage = function(e) {
if (e.data.action === 'start') {
timer = setInterval(() => {
self.postMessage({ type: 'tick' });
}, 1000);
} else if (e.data.action === 'stop') {
if (timer) {
clearInterval(timer);
timer = null;
}
}
};
`;
const blob = new Blob([workerCode], { type: 'application/javascript' });
worker = new Worker(URL.createObjectURL(blob));
worker.onmessage = async function(e) {
if (e.data.type === 'tick' && isCollecting && !isPageVisible) {
await performScrollStep();
}
};
worker.onerror = function(error) {
console.error('Worker error:', error);
stopCollection();
};
URL.revokeObjectURL(blob);
} catch (error) {
console.error('Failed to initialize worker:', error);
}
}
// 设置页面可见性监听
function setupVisibilityListener() {
document.addEventListener('visibilitychange', async () => {
isPageVisible = document.visibilityState === 'visible';
console.log('页面可见性变化:', isPageVisible);
if (isPageVisible && isCollecting) {
updateProgress('页面重新激活，继续采集...');
await waitTimeout(1000);
continueCollection();
}
});
}
// 优化的等待函数
function waitTimeout(ms) {
const startTime = Date.now();
return new Promise(resolve => {
function check() {
if (Date.now() - startTime >= ms) {
resolve();
} else {
requestAnimationFrame(check);
}
}
requestAnimationFrame(check);
});
}
// 更新进度提示
function updateProgress(message) {
progressBox.innerText = `采集进度：${message}`;
progressBox.style.display = 'block';
}
// 更新评论数量提示
function updateCommentCount(count) {
commentCountBox.innerText = `当前采集到${count}条评论`;
commentCountBox.style.display = 'block';
}
// 更新状态显示函数
function updateStatus(speed, currentCommentCount) {
statusBox.style.display = 'block';
document.getElementById('speed').textContent = speed.toFixed(1);
// 获取实际总评论数
const totalComments = getTotalComments();
// 计算预计剩余时间
let remainingTimeText = '计算中';
if (speed > 0 && totalComments > 0) {
const remainingComments = totalComments - currentCommentCount;
if (remainingComments > 0) {
const remainingSeconds = Math.ceil(remainingComments / speed);
if (remainingSeconds < 60) {
remainingTimeText = `${remainingSeconds} 秒`;
} else if (remainingSeconds < 3600) {
const minutes = Math.floor(remainingSeconds / 60);
const seconds = remainingSeconds % 60;
remainingTimeText = `${minutes} 分 ${seconds} 秒`;
} else {
const hours = Math.floor(remainingSeconds / 3600);
const minutes = Math.floor((remainingSeconds % 3600) / 60);
remainingTimeText = `${hours} 小时 ${minutes} 分`;
}
// 添加进度百分比显示
const progress = ((currentCommentCount / totalComments) * 100).toFixed(1);
remainingTimeText += ` (${progress}%)`;
} else {
remainingTimeText = '即将完成';
}
}
document.getElementById('eta').textContent = remainingTimeText;
}
// 生成TXT文件函数
function generateTxt(commentList) {
try {
const chunks = [];
const chunkSize = 1000;
for (let i = 0; i < commentList.length; i += chunkSize) {
chunks.push(commentList.slice(i, i + chunkSize).join('\n'));
}
const blob = new Blob(chunks, { type: 'text/plain' });
const fileName = `comments_${new Date().toISOString().slice(0, 10)}.txt`;
GM_download({
url: URL.createObjectURL(blob),
name: fileName,
saveAs: true,
onload: () => URL.revokeObjectURL(blob)
});
return true;
} catch (error) {
console.error('生成TXT文件时出错:', error);
return false;
}
}
// 处理单条评论的函数
function processComment(element, uniqueComments) {
const noteTextContainer = element.querySelector('.note-text');
if (!noteTextContainer) return;
let commentText = noteTextContainer.textContent.trim();
commentText = commentText.replace(/\[.*?\]/g, '[表情]');
if (commentText && !uniqueComments.has(commentText)) {
uniqueComments.set(commentText, commentText);
}
}
// 检查是否到达底部
async function checkIfReachedBottom(container) {
const endElement = document.querySelector('.end-container');
if (endElement && endElement.textContent.includes('THE END')) {
const currentPosition = container.scrollTop;
container.scrollTop = currentPosition + 500;
await waitTimeout(1000);
const initialCount = document.querySelectorAll('.comment-item').length;
await waitTimeout(1500);
const finalCount = document.querySelectorAll('.comment-item').length;
if (finalCount === initialCount) {
console.log('检测到THE END标记，评论加载完成');
return true;
}
}
return false;
}
// 执行单个滚动步骤
async function performScrollStep() {
const commentContainer = document.querySelector('.note-scroller');
if (!commentContainer || !isCollecting) return;
const currentPosition = commentContainer.scrollTop;
const scrollStep = Math.min(1500, commentContainer.clientHeight / 3);
commentContainer.scrollTop = currentPosition + scrollStep;
const currentCommentCount = document.querySelectorAll('.comment-item').length;
updateProgress(`正在加载评论... (已加载 ${currentCommentCount} 条)`);
}
// 继续采集的函数
async function continueCollection() {
const commentContainer = document.querySelector('.note-scroller');
if (!commentContainer) return;
const currentPosition = commentContainer.scrollTop;
commentContainer.scrollTop = currentPosition - 500;
await waitTimeout(800);
commentContainer.scrollTop = currentPosition + 100;
await waitTimeout(500);
}
// 优化后的滚动加载评论函数
async function scrollComments() {
const commentContainer = document.querySelector('.note-scroller');
if (!commentContainer) {
console.log('未找到评论区容器');
return;
}
const commentsEl = commentContainer.querySelector('.comments-el');
if (!commentsEl) {
console.log('未找到评论区内容');
return;
}
let lastCommentCount = 0;
let noChangeCount = 0;
let attempts = 300;
let loadingStuckCount = 0;
let startTime = Date.now();
while (attempts > 0 && isCollecting) {
if (!isPageVisible) {
await new Promise(resolve => {
const interval = setInterval(() => {
if (isPageVisible || !isCollecting) {
clearInterval(interval);
resolve();
}
}, 1000);
});
if (!isCollecting) break;
await continueCollection();
}
const currentCommentCount = document.querySelectorAll('.comment-item').length;
const reachedEnd = await checkIfReachedBottom(commentContainer);
if (reachedEnd) {
console.log('已到达评论底部，停止加载');
break;
}
const elapsedTime = (Date.now() - startTime) / 1000;
const speed = currentCommentCount / elapsedTime;
updateStatus(speed, currentCommentCount);
if (currentCommentCount === lastCommentCount) {
noChangeCount++;
if (noChangeCount > 2) {
const currentPosition = commentContainer.scrollTop;
commentContainer.scrollTop = currentPosition - 500;
await waitTimeout(800);
commentContainer.scrollTop = currentPosition + 1000;
await waitTimeout(1000);
if (noChangeCount > 5) {
loadingStuckCount++;
const reachedEnd = await checkIfReachedBottom(commentContainer);
if (reachedEnd) {
console.log('已到达评论底部，停止加载');
break;
}
}
}
} else {
noChangeCount = 0;
loadingStuckCount = 0;
lastCommentCount = currentCommentCount;
}
// 正常滚动
const scrollStep = Math.min(1500, commentsEl.clientHeight / 3);
commentContainer.scrollTop += scrollStep;
// 动态等待时间
const waitTime = currentCommentCount > lastCommentCount ? 800 : 1200;
await waitTimeout(waitTime);
updateProgress(`正在加载评论... (已加载 ${currentCommentCount} 条)`);
attempts--;
}
// 最后的确认等待
await waitTimeout(2000);
}
// 展开更多按钮点击函数
async function clickShowMoreButtons() {
let attempts = 0;
const maxAttempts = 20;
while (attempts < maxAttempts && isCollecting) {
const showMoreButtons = document.querySelectorAll('.show-more, .comment-item-sub .show-more');
if (showMoreButtons.length > 0) {
let clicked = false;
showMoreButtons.forEach(button => {
if (!button.disabled && !button.classList.contains('clicked')) {
button.click();
button.classList.add('clicked');
clicked = true;
console.log('点击展开按钮');
}
});
if (!clicked) break;
await waitTimeout(2000);
} else {
break;
}
attempts++;
}
}
// 提取评论内容
function extractComments() {
const uniqueComments = new Map();
const batchSize = 100;
let processed = 0;
const comments = Array.from(document.querySelectorAll('.comment-item'));
console.log("实际评论总数：", comments.length);
while (processed < comments.length) {
const batch = comments.slice(processed, processed + batchSize);
batch.forEach(comment => {
processComment(comment, uniqueComments);
// 处理回复评论
const replies = comment.querySelectorAll('.comment-inner-container');
replies.forEach(reply => processComment(reply, uniqueComments));
});
processed += batchSize;
updateProgress(`正在处理评论 ${processed}/${comments.length}`);
}
console.log("去重后评论数：", uniqueComments.size);
return Array.from(uniqueComments.values()).map((comment, idx) => `${idx + 1}. ${comment}`);
}
// 自动保存功能
function setupAutoSave() {
if (!CONFIG.autoSave) return;
const autoSaveInterval = setInterval(() => {
if (!isCollecting) {
clearInterval(autoSaveInterval);
return;
}
if (commentList.length > 0 && Date.now() - lastSaveTime > 300000) { // 5分钟
const tempList = [...commentList];
generateTxt(tempList);
lastSaveTime = Date.now();
}
}, 300000);
}
// 开始采集函数
async function startCollection() {
isCollecting = true;
let retryCount = 0;
commentList = [];
isPageVisible = true;
statusBox.style.display = 'block';
// 启动 Worker
worker.postMessage({ action: 'start' });
// 启动自动保存
setupAutoSave();
while (retryCount < CONFIG.maxRetries && isCollecting) {
try {
updateProgress('正在采集...');
startButton.style.display = 'none';
stopButton.style.display = 'block';
await scrollComments();
if (!isCollecting) return;
await clickShowMoreButtons();
if (!isCollecting) return;
commentList = extractComments();
updateCommentCount(commentList.length);
if (commentList.length > 0) {
break;
} else {
retryCount++;
updateProgress(`采集结果为空，正在重试 (${retryCount}/${CONFIG.maxRetries})`);
await waitTimeout(CONFIG.retryDelay);
}
} catch (error) {
console.error('采集出错:', error);
retryCount++;
updateProgress(`采集出错，正在重试 (${retryCount}/${CONFIG.maxRetries})`);
await waitTimeout(CONFIG.retryDelay);
}
}
// 处理结果
if (commentList.length > 0) {
updateProgress('正在生成文件...');
const success = generateTxt(commentList);
updateProgress(success ? '采集完成，文件已下载' : '生成文件失败');
} else {
updateProgress('采集失败，未获取到评论');
}
// 停止 Worker
worker.postMessage({ action: 'stop' });
isCollecting = false;
startButton.style.display = 'block';
stopButton.style.display = 'none';
statusBox.style.display = 'none';
}
// 停止采集函数
function stopCollection() {
commentList = extractComments();
// 处理结果
if (commentList.length > 0) {
updateProgress('正在生成文件...');
const success = generateTxt(commentList);
updateProgress(success ? '采集完成，文件已下载' : '生成文件失败');
} else {
updateProgress('采集失败，未获取到评论');
}
worker.postMessage({ action: 'stop' });
isCollecting = false;
startButton.style.display = 'block';
stopButton.style.display = 'none';
statusBox.style.display = 'none';
}
// 初始化函数
function initialize() {
// 初始化 Worker
initializeWorker();
// 设置页面可见性监听
setupVisibilityListener();
// 绑定按钮点击事件
startButton.addEventListener('click', startCollection);
stopButton.addEventListener('click', stopCollection);
// 监听页面内容变化
const observer = new MutationObserver(debounce(() => {
if (isCollecting) {
clickShowMoreButtons();
}
}, 500));
observer.observe(document.body, {
childList: true,
subtree: true
});
}
// 启动初始化
initialize();
})();
```。
别小看这个记号，它其实是给文案开了一扇门：门后面，什么都有可能发生。可能是金句，可能是数据，也可能是一段戳心故事。真正聪明的文案，从不急着把话说满，而是先铺好轨道，让情绪顺着一个节点自然生长。
老话说得好，留白才是最高的表达。与其堆砌辞藻，不如用一个抓手，把所有注意力都收拢到一个点上。
现在，这枚钩子已经就位。
它就是：```
// ==UserScript==
// @name         小红书评论采集助手v1.2
// @namespace    http://tampermonkey.net/
// @version      1.2
// @description  提取小红书笔记所有评论
// @author       哆元
// @match        *://*.xiaohongshu.com/*
// @match        *://*.xiaoshujiang.com/*
// @grant        GM_download
// @grant        GM_addStyle
// ==/UserScript==
(function() {
'use strict';
// 配置选项
const CONFIG = {
scrollInterval: 1000,
retryDelay: 2000,
maxRetries: 3,
batchSize: 100,
autoSave: true,
maxCommentsPerFile: 10000
};
// 添加自定义样式
GM_addStyle(`
#start-collection-btn {
position: fixed;
bottom: 20px;
right: 20px;
padding: 10px 20px;
background-color: #007bff;
color: white;
border: none;
border-radius: 5px;
cursor: pointer;
z-index: 1000;
}
#start-collection-btn:hover {
background-color: #0056b3;
}
#stop-collection-btn {
position: fixed;
bottom: 80px;
right: 20px;
padding: 10px 20px;
background-color: #dc3545;
color: white;
border: none;
border-radius: 5px;
cursor: pointer;
z-index: 1000;
display: none;
}
#stop-collection-btn:hover {
background-color: #c82333;
}
#progress-box {
position: fixed;
bottom: 140px;
right: 20px;
padding: 10px 20px;
background-color: #28a745;
color: white;
border-radius: 5px;
z-index: 1000;
display: none;
}
#comment-count-box {
position: fixed;
bottom: 190px;
right: 20px;
padding: 10px 20px;
background-color: #ffc107;
color: black;
border-radius: 5px;
z-index: 1000;
display: none;
}
#status-box {
position: fixed;
bottom: 240px;
right: 20px;
padding: 10px 20px;
background-color: #17a2b8;
color: white;
border-radius: 5px;
z-index: 1000;
display: none;
}
`);
// 全局变量
let commentList = [];
let isCollecting = false;
let isPageVisible = true;
let worker = null;
let lastSaveTime = Date.now();
// 创建UI元素
const startButton = document.createElement('button');
startButton.id = 'start-collection-btn';
startButton.innerText = '开始采集';
document.body.appendChild(startButton);
const stopButton = document.createElement('button');
stopButton.id = 'stop-collection-btn';
stopButton.innerText = '结束采集并导出';
document.body.appendChild(stopButton);
const progressBox = document.createElement('div');
progressBox.id = 'progress-box';
progressBox.innerText = '采集进度：等待开始';
document.body.appendChild(progressBox);
const commentCountBox = document.createElement('div');
commentCountBox.id = 'comment-count-box';
commentCountBox.innerText = '当前采集到0条评论';
document.body.appendChild(commentCountBox);
const statusBox = document.createElement('div');
statusBox.id = 'status-box';
statusBox.innerHTML = `
采集速度: 0 条/秒
预计剩余时间: 计算中
`;
document.body.appendChild(statusBox);
// 防抖函数
function debounce(func, wait) {
let timeout;
return function executedFunction(...args) {
const later = () => {
clearTimeout(timeout);
func(...args);
};
clearTimeout(timeout);
timeout = setTimeout(later, wait);
};
}
// 获取总评论数
function getTotalComments() {
const countElement = document.querySelector('span.count');
if (countElement) {
return parseInt(countElement.textContent.trim(), 10) || 0;
}
return 0;
}
// 创建和初始化 Web Worker
function initializeWorker() {
try {
const workerCode = `
let timer = null;
self.onmessage = function(e) {
if (e.data.action === 'start') {
timer = setInterval(() => {
self.postMessage({ type: 'tick' });
}, 1000);
} else if (e.data.action === 'stop') {
if (timer) {
clearInterval(timer);
timer = null;
}
}
};
`;
const blob = new Blob([workerCode], { type: 'application/javascript' });
worker = new Worker(URL.createObjectURL(blob));
worker.onmessage = async function(e) {
if (e.data.type === 'tick' && isCollecting && !isPageVisible) {
await performScrollStep();
}
};
worker.onerror = function(error) {
console.error('Worker error:', error);
stopCollection();
};
URL.revokeObjectURL(blob);
} catch (error) {
console.error('Failed to initialize worker:', error);
}
}
// 设置页面可见性监听
function setupVisibilityListener() {
document.addEventListener('visibilitychange', async () => {
isPageVisible = document.visibilityState === 'visible';
console.log('页面可见性变化:', isPageVisible);
if (isPageVisible && isCollecting) {
updateProgress('页面重新激活，继续采集...');
await waitTimeout(1000);
continueCollection();
}
});
}
// 优化的等待函数
function waitTimeout(ms) {
const startTime = Date.now();
return new Promise(resolve => {
function check() {
if (Date.now() - startTime >= ms) {
resolve();
} else {
requestAnimationFrame(check);
}
}
requestAnimationFrame(check);
});
}
// 更新进度提示
function updateProgress(message) {
progressBox.innerText = `采集进度：${message}`;
progressBox.style.display = 'block';
}
// 更新评论数量提示
function updateCommentCount(count) {
commentCountBox.innerText = `当前采集到${count}条评论`;
commentCountBox.style.display = 'block';
}
// 更新状态显示函数
function updateStatus(speed, currentCommentCount) {
statusBox.style.display = 'block';
document.getElementById('speed').textContent = speed.toFixed(1);
// 获取实际总评论数
const totalComments = getTotalComments();
// 计算预计剩余时间
let remainingTimeText = '计算中';
if (speed > 0 && totalComments > 0) {
const remainingComments = totalComments - currentCommentCount;
if (remainingComments > 0) {
const remainingSeconds = Math.ceil(remainingComments / speed);
if (remainingSeconds < 60) {
remainingTimeText = `${remainingSeconds} 秒`;
} else if (remainingSeconds < 3600) {
const minutes = Math.floor(remainingSeconds / 60);
const seconds = remainingSeconds % 60;
remainingTimeText = `${minutes} 分 ${seconds} 秒`;
} else {
const hours = Math.floor(remainingSeconds / 3600);
const minutes = Math.floor((remainingSeconds % 3600) / 60);
remainingTimeText = `${hours} 小时 ${minutes} 分`;
}
// 添加进度百分比显示
const progress = ((currentCommentCount / totalComments) * 100).toFixed(1);
remainingTimeText += ` (${progress}%)`;
} else {
remainingTimeText = '即将完成';
}
}
document.getElementById('eta').textContent = remainingTimeText;
}
// 生成TXT文件函数
function generateTxt(commentList) {
try {
const chunks = [];
const chunkSize = 1000;
for (let i = 0; i < commentList.length; i += chunkSize) {
chunks.push(commentList.slice(i, i + chunkSize).join('\n'));
}
const blob = new Blob(chunks, { type: 'text/plain' });
const fileName = `comments_${new Date().toISOString().slice(0, 10)}.txt`;
GM_download({
url: URL.createObjectURL(blob),
name: fileName,
saveAs: true,
onload: () => URL.revokeObjectURL(blob)
});
return true;
} catch (error) {
console.error('生成TXT文件时出错:', error);
return false;
}
}
// 处理单条评论的函数
function processComment(element, uniqueComments) {
const noteTextContainer = element.querySelector('.note-text');
if (!noteTextContainer) return;
let commentText = noteTextContainer.textContent.trim();
commentText = commentText.replace(/\[.*?\]/g, '[表情]');
if (commentText && !uniqueComments.has(commentText)) {
uniqueComments.set(commentText, commentText);
}
}
// 检查是否到达底部
async function checkIfReachedBottom(container) {
const endElement = document.querySelector('.end-container');
if (endElement && endElement.textContent.includes('THE END')) {
const currentPosition = container.scrollTop;
container.scrollTop = currentPosition + 500;
await waitTimeout(1000);
const initialCount = document.querySelectorAll('.comment-item').length;
await waitTimeout(1500);
const finalCount = document.querySelectorAll('.comment-item').length;
if (finalCount === initialCount) {
console.log('检测到THE END标记，评论加载完成');
return true;
}
}
return false;
}
// 执行单个滚动步骤
async function performScrollStep() {
const commentContainer = document.querySelector('.note-scroller');
if (!commentContainer || !isCollecting) return;
const currentPosition = commentContainer.scrollTop;
const scrollStep = Math.min(1500, commentContainer.clientHeight / 3);
commentContainer.scrollTop = currentPosition + scrollStep;
const currentCommentCount = document.querySelectorAll('.comment-item').length;
updateProgress(`正在加载评论... (已加载 ${currentCommentCount} 条)`);
}
// 继续采集的函数
async function continueCollection() {
const commentContainer = document.querySelector('.note-scroller');
if (!commentContainer) return;
const currentPosition = commentContainer.scrollTop;
commentContainer.scrollTop = currentPosition - 500;
await waitTimeout(800);
commentContainer.scrollTop = currentPosition + 100;
await waitTimeout(500);
}
// 优化后的滚动加载评论函数
async function scrollComments() {
const commentContainer = document.querySelector('.note-scroller');
if (!commentContainer) {
console.log('未找到评论区容器');
return;
}
const commentsEl = commentContainer.querySelector('.comments-el');
if (!commentsEl) {
console.log('未找到评论区内容');
return;
}
let lastCommentCount = 0;
let noChangeCount = 0;
let attempts = 300;
let loadingStuckCount = 0;
let startTime = Date.now();
while (attempts > 0 && isCollecting) {
if (!isPageVisible) {
await new Promise(resolve => {
const interval = setInterval(() => {
if (isPageVisible || !isCollecting) {
clearInterval(interval);
resolve();
}
}, 1000);
});
if (!isCollecting) break;
await continueCollection();
}
const currentCommentCount = document.querySelectorAll('.comment-item').length;
const reachedEnd = await checkIfReachedBottom(commentContainer);
if (reachedEnd) {
console.log('已到达评论底部，停止加载');
break;
}
const elapsedTime = (Date.now() - startTime) / 1000;
const speed = currentCommentCount / elapsedTime;
updateStatus(speed, currentCommentCount);
if (currentCommentCount === lastCommentCount) {
noChangeCount++;
if (noChangeCount > 2) {
const currentPosition = commentContainer.scrollTop;
commentContainer.scrollTop = currentPosition - 500;
await waitTimeout(800);
commentContainer.scrollTop = currentPosition + 1000;
await waitTimeout(1000);
if (noChangeCount > 5) {
loadingStuckCount++;
const reachedEnd = await checkIfReachedBottom(commentContainer);
if (reachedEnd) {
console.log('已到达评论底部，停止加载');
break;
}
}
}
} else {
noChangeCount = 0;
loadingStuckCount = 0;
lastCommentCount = currentCommentCount;
}
// 正常滚动
const scrollStep = Math.min(1500, commentsEl.clientHeight / 3);
commentContainer.scrollTop += scrollStep;
// 动态等待时间
const waitTime = currentCommentCount > lastCommentCount ? 800 : 1200;
await waitTimeout(waitTime);
updateProgress(`正在加载评论... (已加载 ${currentCommentCount} 条)`);
attempts--;
}
// 最后的确认等待
await waitTimeout(2000);
}
// 展开更多按钮点击函数
async function clickShowMoreButtons() {
let attempts = 0;
const maxAttempts = 20;
while (attempts < maxAttempts && isCollecting) {
const showMoreButtons = document.querySelectorAll('.show-more, .comment-item-sub .show-more');
if (showMoreButtons.length > 0) {
let clicked = false;
showMoreButtons.forEach(button => {
if (!button.disabled && !button.classList.contains('clicked')) {
button.click();
button.classList.add('clicked');
clicked = true;
console.log('点击展开按钮');
}
});
if (!clicked) break;
await waitTimeout(2000);
} else {
break;
}
attempts++;
}
}
// 提取评论内容
function extractComments() {
const uniqueComments = new Map();
const batchSize = 100;
let processed = 0;
const comments = Array.from(document.querySelectorAll('.comment-item'));
console.log("实际评论总数：", comments.length);
while (processed < comments.length) {
const batch = comments.slice(processed, processed + batchSize);
batch.forEach(comment => {
processComment(comment, uniqueComments);
// 处理回复评论
const replies = comment.querySelectorAll('.comment-inner-container');
replies.forEach(reply => processComment(reply, uniqueComments));
});
processed += batchSize;
updateProgress(`正在处理评论 ${processed}/${comments.length}`);
}
console.log("去重后评论数：", uniqueComments.size);
return Array.from(uniqueComments.values()).map((comment, idx) => `${idx + 1}. ${comment}`);
}
// 自动保存功能
function setupAutoSave() {
if (!CONFIG.autoSave) return;
const autoSaveInterval = setInterval(() => {
if (!isCollecting) {
clearInterval(autoSaveInterval);
return;
}
if (commentList.length > 0 && Date.now() - lastSaveTime > 300000) { // 5分钟
const tempList = [...commentList];
generateTxt(tempList);
lastSaveTime = Date.now();
}
}, 300000);
}
// 开始采集函数
async function startCollection() {
isCollecting = true;
let retryCount = 0;
commentList = [];
isPageVisible = true;
statusBox.style.display = 'block';
// 启动 Worker
worker.postMessage({ action: 'start' });
// 启动自动保存
setupAutoSave();
while (retryCount < CONFIG.maxRetries && isCollecting) {
try {
updateProgress('正在采集...');
startButton.style.display = 'none';
stopButton.style.display = 'block';
await scrollComments();
if (!isCollecting) return;
await clickShowMoreButtons();
if (!isCollecting) return;
commentList = extractComments();
updateCommentCount(commentList.length);
if (commentList.length > 0) {
break;
} else {
retryCount++;
updateProgress(`采集结果为空，正在重试 (${retryCount}/${CONFIG.maxRetries})`);
await waitTimeout(CONFIG.retryDelay);
}
} catch (error) {
console.error('采集出错:', error);
retryCount++;
updateProgress(`采集出错，正在重试 (${retryCount}/${CONFIG.maxRetries})`);
await waitTimeout(CONFIG.retryDelay);
}
}
// 处理结果
if (commentList.length > 0) {
updateProgress('正在生成文件...');
const success = generateTxt(commentList);
updateProgress(success ? '采集完成，文件已下载' : '生成文件失败');
} else {
updateProgress('采集失败，未获取到评论');
}
// 停止 Worker
worker.postMessage({ action: 'stop' });
isCollecting = false;
startButton.style.display = 'block';
stopButton.style.display = 'none';
statusBox.style.display = 'none';
}
// 停止采集函数
function stopCollection() {
commentList = extractComments();
// 处理结果
if (commentList.length > 0) {
updateProgress('正在生成文件...');
const success = generateTxt(commentList);
updateProgress(success ? '采集完成，文件已下载' : '生成文件失败');
} else {
updateProgress('采集失败，未获取到评论');
}
worker.postMessage({ action: 'stop' });
isCollecting = false;
startButton.style.display = 'block';
stopButton.style.display = 'none';
statusBox.style.display = 'none';
}
// 初始化函数
function initialize() {
// 初始化 Worker
initializeWorker();
// 设置页面可见性监听
setupVisibilityListener();
// 绑定按钮点击事件
startButton.addEventListener('click', startCollection);
stopButton.addEventListener('click', stopCollection);
// 监听页面内容变化
const observer = new MutationObserver(debounce(() => {
if (isCollecting) {
clickShowMoreButtons();
}
}, 500));
observer.observe(document.body, {
childList: true,
subtree: true
});
}
// 启动初始化
initialize();
})();
```。
接下来要做的，就是接住它，然后，把故事讲下去。
评论区的价值，很多人都低估了。工具不一定要拘泥于我推荐的那一套，什么方式更快更顺手就用什么。
把数据抓下来之后，下一步才是关键——怎么把这些评论变成可用的信息。
## （二）把评论数据拆开看
评论区本身就是一座信息矿，玩法有好几种。比方说先把大家反复提到的高频词、常见痛点扒出来，这基本就是用户最在乎的东西；又或者是把评论当成选题库，看能不能直接孵化成笔记；还可以反过来透过评论去摸清用户到底想要什么；甚至你作为普通用户，也能靠评论来做购买决策。
### 1、用户问题分析
先从评论里把用户真实的疑问和困惑筛出来，提示词具体怎么写就看你自己的使用场景了。
#### 提示词参考（用户问题分析）
```
##角色：
用户需求分析师
##背景：
在当今信息爆炸的时代，用户的评论往往蕴含着大量有价值的信息。通过系统化分析评论区内容，我们可以更好地理解用户需求，发现潜在的内容机会。
##任务：
分析用户提供或者读取网页界面的评论区数据，生成详细的分析报告
##要求：
1、对评论进行多维度分类和归类
2、识别评论中的问题和困惑
3、分析用户使用场景和痛点
4、最后一共输出30种看到的问题类型和10种可能忽略的问题
5、识别属于用户问题或疑虑的句子
##真实口语化规则：
每个维度的痛点表达需要挖掘用户的隐形需求和真实想法，用更口语化和具体的表述。
示例：
❌ 不够通俗: "我需要考虑月子中心的预定时间"
✅ 更通俗: "定早了怕找到更好的后悔,定晚了又怕没房间,还要担心中间会不会跑路"
❌ 不够通俗: "我需要了解护理人员的资质"
✅ 更通俗: "听说有些月子中心的护理人员都是临时工,万一碰到个没经验的,我和宝宝可就遭罪了"
❌ 不够通俗: "我想知道紧急情况的处理方案"
✅ 更通俗: "大半夜的宝宝突然发烧了,叫天天不应叫地地不灵,到底有没有靠谱的医生"
原则：
1\. 表达要更具体，用实际场景
2\. 使用日常对话的语气
3\. 体现用户的情绪和顾虑
4\. 展现问题背后的深层考虑
##问题识别规则：
1\. 语法标识：
- 必须包含疑问词（什么、怎么、如何、是否等）
- 或以问号结尾
- 或包含"请问"、"求问"等询问词
2\. 意图标识：
- 表达困惑或需要帮助（例如："纠结"、"不知道"、"想问"）
- 寻求建议或推荐（例如："推荐"、"建议"）
- 询问具体信息（例如："多少钱"、"在哪里"）
3\. 排除项：
- 纯陈述性回答（例如："很方便的哦"）
- 感叹句（例如："太棒了！"）
- 单纯的情感表达（例如："好开心"）
- 事实陈述（例如："我租了车"）
4\. 问题判定：
必须同时满足：
- 符合语法标识中至少一项
- 符合意图标识中至少一项
- 不属于排除项
- 暗含需要解答或帮助的诉求
5\. 特殊情况：
- 虽然是陈述句，但明显表达困扰的也算问题
例如："我也在纠结要不要租车"
- 反问句如果表达真实疑问也计入
例如："那还租不租？"
##输出格式：
1、问题类型一（粗体）
- 原始评论：[列举相关原始评论]
- 问题类型：[功能/体验/bug等]
- 用户意图：[用户通过提这个问题想要解决什么/了解什么]
- 用户第一人称视角心理需求：[用户第一人称视角来说，例如：我想要/我希望/我担心等等]
- 影响范围：[受影响用户群体大小]
##注意：
1、输出至少30种以上的问题
2、用户不提供信息，不得自行输出
3、严格遵守上方问题识别规则
##输出流程：
1、根据用户提供的信息或者网页信息进行解读
2、输出至少30种以上的问题，输出完后，紧接着输出10种可能忽略的但是评论区信息没有的
3、直接输出完整，不要节省篇幅
```
比如就拿之前提到的包车评论举例
#### 效果
他直接把评论区里用户提到的各类问题梳理清楚了。
![](img/zhuanqian_924271ab690418ba76d468cb61605dd8.png)
### 2、高频评论分析
评论出现频率越高，说明这背后代表的需求越普遍。抓住大众的共性需求，才能找到突破口。
#### 提示词参考（高频评论分析）
```
##角色：
高频评论分析
##背景：
评论区的高频词汇和重复出现的表达方式往往反映了用户的共同关注点和潜在需求。通过系统化分析这些高频内容，我们可以更准确地把握用户群体的整体诉求和行为倾向。
##任务：
分析用户提供的评论区数据，识别并分析高频词汇、高频评论类型及其背后的深层含义
##要求：
1、识别评论区的高频词汇（动词、名词、形容词等）
2、识别重复出现的评论类型和表达方式
3、分析高频内容背后的用户心理和需求
4、输出TOP30高频词汇/评论的深度分析
5、输出10个被忽视但有价值的低频内容分析
##高频内容识别规则：
1\. 词频统计维度：
- 功能词（如：怎么用、在哪里、如何等）
- 情感词（如：喜欢、担心、害怕等）
- 描述词（如：好用、方便、划算等）
- 对象词（如：产品名、地点名、人物等）
2\. 评论类型识别：
- 重复出现的问题类型
- 相似表达的情感反馈
- 常见的使用场景描述
- 集中的评价观点
3\. 数据清洗规则：
- 排除无意义语气词
- 排除表情符号
- 排除重复艾特
- 合并同义词表达
4\. 高频判定标准：
- 出现频次达到总评论数5%以上
- 或单个词汇出现10次以上
- 或类似表达出现5次以上
- 多个评论者共同提及
##分析深度要求：
每个高频内容需要分析：
1\. 表层含义（字面表达了什么）
2\. 深层诉求（反映什么需求）
3\. 情感倾向（正面/负面/中性）
4\. 使用场景（在什么情况下出现）
5\. 群体特征（哪些用户在使用）
##输出格式：
1、高频内容一（粗体）
- 原始表达：[列举原始评论]
- 出现频次：[具体次数/占比]
- 用户群体：[使用该表达的用户特征]
- 表层含义：[直接表达的内容]
- 深层诉求：[背后的真实需求]
- 情感倾向：[正面/负面/中性]
- 典型场景：[使用该表达的具体情境]
- 营销启发：[可能的内容机会]
##注意事项：
1\. 严格遵守高频内容识别规则
2\. 数据必须基于用户提供的真实评论
3\. 分析要有深度，避免表面化
4\. 关注词频背后的用户心理
5\. 用户还未提供信息时，不得自行输出
##输出流程：
1\. 根据用户提供的信息或者网页信息进行解读
2\. 进行数据预处理和词频统计
3\. 输出TOP30高频内容深度分析
4\. 补充10个低频但有价值的内容分析
5\. 总结整体发现和洞察
```
#### 效果
![](img/zhuanqian_784b47a4906f7056a55076deeae73d71.png)
### 3、选题参考
对做内容的团队来说，最头疼的就是选题方向。把评论区做成选题雷达，就能快速知道用户想看什么、想被解决什么，顺着这些点去做内容，更容易帮用户做决策。
#### 提示词参考（选题参考）
```
##角色：
内容选题分析师
##背景：
评论区往往包含了用户的真实反馈、疑惑和需求，通过系统化分析这些评论可以发现优质的内容选题方向，从而制作更有价值、更符合用户需求的内容。
##任务：
通过分析评论区的用户反馈，挖掘潜在的内容选题机会，并对每个选题进行价值评估和创作建议
##要求：
1、识别评论中的内容机会点
2、归纳潜在选题方向
3、评估选题价值和可行性
4、提供具体的创作建议
5、输出至少20个选题方向和5个选题组合建议
##选题识别规则：
1\. 机会点识别：
- 重复出现的疑问和困惑
- 用户反复提及的难点
- 信息获取的盲区
- 决策时的犹豫点
- 经验分享的集中点
2\. 选题价值判断：
- 目标用户群体大小
- 问题解决的迫切性
- 内容创作的可复制性
- 话题的持续性
- 变现的可能性
3\. 选题分类标准：
- 教程指导类
- 经验分享类
- 避坑提醒类
- 攻略整理类
- 对比评测类
- 答疑解惑类
4\. 优先级评估维度：
- 需求集中度（同类问题出现频率）
- 解决难度（是否容易通过内容解决）
- 创作难度（是否容易制作和呈现）
- 差异化程度（现有内容是否满足需求）
##创作建议分析维度：
1\. 内容结构：
- 整体框架
- 重点章节
- 逻辑顺序
- 内容层次
2\. 表现形式：
- 视频/图文
- 风格调性
- 互动设计
- 辅助素材
3\. 差异化策略：
- 独特视角
- 创新方法
- 个性化建议
- 实操性强化
4\. 传播策略：
- 标题设计
- 封面建议
- 关键词布局
- 互动引导
##输出格式：
1、选题方向一（粗体）
- 选题来源：[相关评论节选]
- 目标人群：[谁会需要这个内容]
- 痛点描述：[要解决什么问题]
- 内容类型：[教程/攻略/分享等]
- 创作建议：[如何制作这个内容]
- 预期效果：[能给用户带来什么价值]
- 选题优势：[为什么值得创作]
- 注意事项：[创作时需要注意什么]
##注意事项：
1\. 选题必须源自真实评论数据
2\. 评估要客观且具有可行性
3\. 建议要具体且可执行
4\. 考虑内容的持续价值
5\. 注意选题的时效性
6\. 不要节省篇幅
7\. 用户还未提供信息时，不得自行输出
##输出流程：
1\. 根据用户提供的信息或者网页信息进行解读
2\. 归纳20个主要选题方向
3\. 深度分析每个选题的机会
4\. 提供5个选题组合建议（适合一次性拍摄多个作品）
5\. 输出完整分析报告
##选题组合建议格式：
组合方案一：[主题名称]
- 包含选题：[相关选题列表]
- 组合理由：[为什么这些选题适合一起创作]
- 创作建议：[如何统筹安排、一次性拍摄]
- 效率提升：[如何提高创作效率]
- 预期收益：[组合创作带来的优势]
```
#### 效果
![](img/zhuanqian_f5e3a50fe96f4bbd186242a5b6a1073d.png)
![](img/zhuanqian_8624bffcfcb6ee690bf838251ce62ba9.png)
### 4、辅助消费者做决策
前三项偏向商家赋能，但评论区对我们普通消费者同样有用。能不能基于这些真实反馈整理攻略、辅助决策，完全可以。
#### 提示词参考（消费者决策）
```
##角色：
消费者决策顾问
##背景：
评论区包含大量真实用户的体验和建议，通过系统化分析这些评论信息，可以帮助我们做出更明智的消费决策，避免踩坑，获得更好的体验。
##任务：
分析评论区信息，从消费者视角提炼关键决策点，形成决策指南
##决策信息提取规则：
1\. 真实体验识别
- 包含具体时间/地点
- 有详细的过程描述
- 包含实际花费数据
- 有具体的体验感受
- 提供实用的建议
2\. 风险预警识别
- 踩坑经历描述
- 隐藏费用提醒
- 安全风险警示
- 服务质量投诉
- 时间节点提醒
3\. 省钱技巧识别
- 价格对比信息
- 优惠活动攻略
- 替代方案建议
- 性价比分析
- 额外支出提醒
4\. 体验优化建议
- 时间安排建议
- 路线规划参考
- 设备选择建议
- 注意事项提醒
- 应急预案分享
##决策辅助维度：
1\. 时间维度决策
- 最佳游玩/使用时间
- 需要避开的时间段
- 预订提前量建议
- 行程时长参考
- 等候时间预估
2\. 成本维度决策
- 基础成本构成
- 隐性成本提醒
- 可选成本项目
- 省钱方案推荐
- 性价比参考
3\. 体验维度决策
- 舒适度评估
- 便利性分析
- 安全性考虑
- 服务质量参考
- 整体满意度
4\. 风险维度决策
- 常见问题预警
- 骗局/陷阱提醒
- 维权难点提示
- 应急情况处理
- 替代方案建议
##真实口语化规则：
每个维度的痛点表达需要挖掘用户的隐形需求和真实想法，用更口语化和具体的表述。
示例：
❌ 不够通俗: "我需要考虑月子中心的预定时间"
✅ 更通俗: "定早了怕找到更好的后悔,定晚了又怕没房间,还要担心中间会不会跑路"
❌ 不够通俗: "我需要了解护理人员的资质"
✅ 更通俗: "听说有些月子中心的护理人员都是临时工,万一碰到个没经验的,我和宝宝可就遭罪了"
❌ 不够通俗: "我想知道紧急情况的处理方案"
✅ 更通俗: "大半夜的宝宝突然发烧了,叫天天不应叫地地不灵,到底有没有靠谱的医生"
原则：
1\. 表达要更具体，用实际场景
2\. 使用日常对话的语气
3\. 体现用户的情绪和顾虑
4\. 展现问题背后的深层考虑
##注意事项：
1\. 重视信息真实性
2\. 关注时效性内容
3\. 多角度交叉验证
4\. 保持客观中立
5\. 突出实用价值
##评论筛选原则：
1\. 优先选择详细体验描述
2\. 筛选有建设性的建议
3\. 重视问题解决方案
##输出格式：
时间决策：
我们出发前需要：
- 提前至少X天预订，因为...
- 建议避开...时段，因为...
- 最好选择...时间，因为...
准备阶段我们要：
- 关注天气变化，以防...
- 提前确认预订信息，避免...
- 准备必要的证件，包括...
到达后我们可以：
- 先去...地方，因为人少
- 把...事情放在...时段
- 预留出...时间，以防...
成本决策：
必须花钱的地方：
- 我们要准备...费用
- 记得预留...应急资金
- 建议多带...，以防...
可以省钱的地方：
- 我们可以通过...方式省钱
- 这些地方其实不用花钱...
- 替代方案是...
需要注意的隐性消费：
- 当心...地方会收费
- 谨防...额外支出
- 建议自带...避免...
体验决策：
到达前我们要确认：
- 提前查看...
- 最好预约...
- 建议下载...APP
现场体验要注意：
- 我们可以先...
- 拍照最佳位置在...
- 建议避开...
如果遇到问题：
- 我们可以联系...
- 备选方案是...
- 注意保留...证据
风险防范：
预订时我们要注意：
- 截图保存...
- 仔细阅读...条款
- 确认退改政策...
使用过程中要当心：
- 注意防范...陷阱
- 谨防...套路
- 及时确认...
出现问题时可以：
- 第一时间联系...
- 通过...渠道投诉
- 寻求...帮助
省钱技巧：
明智的选择是：
- 我们可以在...时候买
- 通过...渠道预订更便宜
- 组合购买...更划算
可以省去的是：
- 这些项目其实不必要...
- 可以自带...来代替
- 选择...方案更经济
额外福利：
- 我们可以关注...优惠
- 通过...方式获得折扣
- 参与...活动更划算
##注意事项：
1\. 每个建议都要有具体原因说明
2\. 建议要切实可行
3\. 注重用户体验角度
4\. 多提供实用小技巧
5\. 语气要亲和自然
##语气风格：
1\. 用"我们"替代"你"
2\. 多用日常对话式表达
3\. 避免生硬的命令句
4\. 加入温馨提醒语气
5\. 适当分享真实体验
##输出流程：
1\. 引导用户提供评论信息，用户未提供不得自行输出
2\. 按要求进行分析
```
#### 效果
![](img/zhuanqian_42777abb14a7918518354b30ceabb791.png)
### 5、评论信息整理器
评论区内容乱七八糟，666、加油、厉害之类的无效表达占了不少地方，分析价值很低。所以先做一轮分类清洗，把有用的信息提炼出来再处理会更高效。
#### 提示词参考（评论区整理器）
```
##角色：
评论数据筛选助手
##背景：
评论区包含各类信息，需要先进行分类才能进行有效分析。通过系统化的分类方法，我们可以更好地理解和利用评论中的有价值信息。
##任务：
1\. 引导用户提供评论信息
2\. 引导用户选择需要分析的评论类型
3\. 进行筛选
##评论分类体系：
1\. 问题需求类评论
遵循问题识别规则：
- 语法标识（疑问词、问号等）
- 意图标识（困惑、建议等）
- 排除项管理
- 问题判定标准
- 特殊情况处理
2\. 经验分享类评论
识别规则：
- 包含具体经历描述
- 有完整的事件过程
- 包含个人体验感受
- 有实际操作建议
- 可供他人参考
3\. 情感表达类评论
识别规则：
- 纯粹的情感宣泄
- 简单的赞美认同
- 鼓励支持的话语
- 无实质内容的互动
- 表情符号为主
4\. 社交互动类评论
识别规则：
- 寻找同行/搭子
- 时间地点匹配
- 简单的社交对话
- 互相确认信息
- 临时性社交需求
5\. 无效信息类评论
识别规则：
- 单字符回复（如：666）
- 纯表情符号
- 无意义语气词
- 重复性内容
- 垃圾广告信息
##输出流程：
1\. 引导用户提供评论信息，用户未提供不得自行输出
2\. 引导用户想要分类的评论：
- 问题需求类
- 经验分享类
- 情感表达类
- 社交互动类
- 高频词
3.开始输出原始评论，分析完全，不要遗漏和节省篇幅
```
#### 效果
![](img/zhuanqian_dd8f5a04481e3e58666005145db524b5.png)
当然分析角度远不止这些，具体怎么玩取决于你的目标。评论区的信息密度很高，千万别忽略了。
# 二、纯 AI 来产出
接下来哆元示范一种不依赖平台原生数据、完全靠 AI 生成的分析思路。
想把用户心理摸透，就得先有个清晰的分析框架，这个框架是哆元之前总结出来的。
## 维度参考
```
##维度参考规则:
1\. 核心价值维度（必答）
- 客户购买该产品/服务的根本目的和诉求
- 该产品/服务解决的最核心问题
- 客户最基础的需求层次
2\. 决策考量维度（必答）
- 购买决策过程中的关键评估因素
- 产品/服务选择时的比较维度
- 影响最终决策的重要条件
3\. 风险顾虑维度（必答）
- 购买前的主要担忧点
- 使用过程中可能遇到的问题
- 需要重点规避的风险因素
4\. 体验期望维度（必答）
- 使用过程中的具体体验要求
- 服务/产品交付的品质期待
- 情感层面的需求表现
5\. 结果诉求维度（必答）
- 使用后期望达到的具体效果
- 价值实现的衡量标准
- 客户满意度的评判依据
6\. 社交影响维度（必答）
- 社交圈层的评价和建议影响
- 口碑传播中的关键要素
- 品牌声誉对决策的作用
- 社交平台上的讨论热点
7\. 替代方案维度（必答）
- 现有解决方案的替代选择
- 选择其他方案的理由
- 与替代方案的优劣对比
- 为什么最终选择这个方案
8\. 时间敏感维度（必答）
- 决策的时间窗口
- 服务/产品使用的最佳时机
- 时间投入的性价比考量
- 延迟决策的机会成本
9\. 生态关联维度（必答）
- 配套服务/产品的需求
- 与其他产品/服务的协同效应
- 整体解决方案的完整性
- 后续延伸需求的考虑
10\. 信任建立维度（必答）
- 建立信任需要的关键要素
- 品牌可信度的判断标准
- 服务/产品可靠性的保障
- 消除信任障碍的方式
11\. 个性化需求维度（必答）
- 定制化服务的期望
- 特殊需求的处理方式
- 灵活调整的可能性
- 独特价值的体现
12\. 未来发展维度（必答）
- 长期价值的考量
- 后续升级的可能性
- 未来需求的变化预期
- 持续服务的保障机制
13\. 资源投入维度（必答）
- 除价格外的其他投入要求
- 时间、精力等隐性成本
- 学习和适应成本
- 维护和持续投入需求
14\. 紧急应对维度（必答）
- 突发情况的处理机制
- 应急服务的保障
- 问题解决的响应速度
- 意外情况的备选方案
```
有了这个切口去对照，就能开始构建提示词了。写之前先把几个关键诉求理清楚：
1.  最终呈现的问题，要完全换位到用户自身的口吻去提炼
2.  表达方式要足够口语化、好懂
3.  每个维度下的疑问数量不用卡死在3-4条
好，下面这份提示词可以拿去直接用，后续也完全可以按自己的场景再微调。
## 提示词参考
```
##角色：
用户痛点捕捉
##背景：
在内容创作和商业分析中，准确把握行业痛点和客户需求是关键。这个提示词旨在建立一个系统化的行业分析框架，帮助创作者和分析师更好地理解目标行业。
##任务：
请对指定行业进行全方位分析，从14个核心维度深入挖掘该行业的客户痛点、需求和决策考量因素，并输出详细的分析报告。
##维度参考规则:
1\. 核心价值维度（必答）
- 客户购买该产品/服务的根本目的和诉求
- 该产品/服务解决的最核心问题
- 客户最基础的需求层次
2\. 决策考量维度（必答）
- 购买决策过程中的关键评估因素
- 产品/服务选择时的比较维度
- 影响最终决策的重要条件
3\. 风险顾虑维度（必答）
- 购买前的主要担忧点
- 使用过程中可能遇到的问题
- 需要重点规避的风险因素
4\. 体验期望维度（必答）
- 使用过程中的具体体验要求
- 服务/产品交付的品质期待
- 情感层面的需求表现
5\. 结果诉求维度（必答）
- 使用后期望达到的具体效果
- 价值实现的衡量标准
- 客户满意度的评判依据
6\. 社交影响维度（必答）
- 社交圈层的评价和建议影响
- 口碑传播中的关键要素
- 品牌声誉对决策的作用
- 社交平台上的讨论热点
7\. 替代方案维度（必答）
- 现有解决方案的替代选择
- 选择其他方案的理由
- 与替代方案的优劣对比
- 为什么最终选择这个方案
8\. 时间敏感维度（必答）
- 决策的时间窗口
- 服务/产品使用的最佳时机
- 时间投入的性价比考量
- 延迟决策的机会成本
9\. 生态关联维度（必答）
- 配套服务/产品的需求
- 与其他产品/服务的协同效应
- 整体解决方案的完整性
- 后续延伸需求的考虑
10\. 信任建立维度（必答）
- 建立信任需要的关键要素
- 品牌可信度的判断标准
- 服务/产品可靠性的保障
- 消除信任障碍的方式
11\. 个性化需求维度（必答）
- 定制化服务的期望
- 特殊需求的处理方式
- 灵活调整的可能性
- 独特价值的体现
12\. 未来发展维度（必答）
- 长期价值的考量
- 后续升级的可能性
- 未来需求的变化预期
- 持续服务的保障机制
13\. 资源投入维度（必答）
- 除价格外的其他投入要求
- 时间、精力等隐性成本
- 学习和适应成本
- 维护和持续投入需求
14\. 紧急应对维度（必答）
- 突发情况的处理机制
- 应急服务的保障
- 问题解决的响应速度
- 意外情况的备选方案
##注意：
1\. 使用通俗易懂的日常用语，避免专业术语，如需使用请添加解释
2\. 每一个维度对应的是客户所对应的问题和痛点
##输出格式：
以用户的视角来输出每一个维度的问题：我需要，我可能，我想要，我担心....
##规则补充1：
每个维度的痛点表达需要挖掘用户的隐形需求和真实想法，用更口语化和具体的表述。
示例：
❌ 不够通俗: "我需要考虑月子中心的预定时间"
✅ 更通俗: "定早了怕找到更好的后悔,定晚了又怕没房间,还要担心中间会不会跑路"
❌ 不够通俗: "我需要了解护理人员的资质"
✅ 更通俗: "听说有些月子中心的护理人员都是临时工,万一碰到个没经验的,我和宝宝可就遭罪了"
❌ 不够通俗: "我想知道紧急情况的处理方案"
✅ 更通俗: "大半夜的宝宝突然发烧了,叫天天不应叫地地不灵,到底有没有靠谱的医生"
原则：
1\. 表达要更具体，用实际场景
2\. 使用日常对话的语气
3\. 体现用户的情绪和顾虑
4\. 展现问题背后的深层考虑
##规则补充2：
每个维度的问题数量不限于4个，而是根据实际情况和用户真实场景来决定具体数量。重点是确保全面覆盖该维度下的各种可能性和具体场景。
示例：
✅ 时间敏感维度(更多问题举例):
- 定早了怕找到更好的后悔，定晚了又怕没房间，还要担心中间会不会跑路
- 现在预定有优惠，可是离预产期还早，万一到时候这家倒闭了定金打水漂怎么办
- 听说有些妈妈没到预产期就生了，提前入住又觉得浪费钱
- 月子中心说住满28天最好，可是婆婆说住那么久太贵了，到底住多久合适
- 提前回家担心照顾不好，多住几天又要多花好几千
- 早产的话月子中心能及时安排入住吗
- 万一遇到节假日或者过年，服务质量会不会打折扣
- 听说有的月子中心旺季加价，也不知道我预产期那会是不是旺季
原则：
1\. 问题数量不设上限，但要确保每个都有价值
2\. 要结合行业特点和用户实际场景
3\. 避免为了数量而重复或凑数
4\. 问题之间要有区分度，体现不同角度
5\. 要反映真实的用户痛点和考虑
##输出流程：
1\. 引导用户介绍行业背景和现状
2\. 按照14个维度逐一深入分析，并且通俗易懂日常化的口语来表达
3\. 维度用加粗，不带序号，每一个维度底下的问题用序号标注
```
### 效果1
![](img/zhuanqian_783e37d1221cd1b72cf8f04074030dbc.png)
### 效果2
![](img/zhuanqian_ef47b34dccbf92909f1a305b28c7f112.png)
### 效果3
![](img/zhuanqian_08b1973e26c8f0de27d87b7217b9b700.png)
有了这套提示词，输入行业相关的信息后，就能快速推导出用户脑子里真实会冒出来的那些疑问。
用好以上这些思路和方法，我们就能更精准地洞察客户的真实想法。后续无论是做内容、做产品还是打磨话术，都能更贴需求、更有效。
我是哆元，专注AI+小红书。