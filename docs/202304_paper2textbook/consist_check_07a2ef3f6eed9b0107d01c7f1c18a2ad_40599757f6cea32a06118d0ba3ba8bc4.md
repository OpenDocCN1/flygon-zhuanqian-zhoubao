
- **术语不一致：`wasm-opt` 优化参数差异**  
  第 14 章 14.8.5 节 "Rust Wasm极致体积优化编译方法" 中使用 `wasm-opt -Oz ...`；第 15 章 15.4 节 "统一的体积优化管线" 中使用 `wasm-opt -Oz --enable-mutable-globals --strip-debug`，后者新增了 `--enable-mutable-globals` 与 `--strip-debug` 两个关键生产参数，但未在 14 章说明，导致同一工具在不同章节的最佳实践参数不一致。

- **术语不一致：Rust 释放 Wasm 内存的标准模式差异**  
  第 14 章 14.8.3 节使用 `std::mem::forget(vec)` 配合 `Vec::from_raw_parts(ptr, 0, len)` 回收内存；第 15 章 15.5 节 "模式 2：线性内存指针+长度" 使用 `Box::leak(vec.into_boxed_slice())` 与 `Box::from_raw(ptr as *mut [u8])`。两章针对同一“手动内存管理/所有权转移”场景给出了不同的标准库写法（`Vec` vs `Box`），且未解释选型依据，易造成读者困惑。

- **术语不一致：`wasm-bindgen` 导出结构体内存管理模式差异**  
  第 14 章 14.8.5 节 `ImageFilter` 结构体内部使用裸指针 `data_ptr: *mut u8` 手动管理内存；第 15 章 15.5 节 "模式 4" 与 15.7 节 "步骤 1" 均使用 `Vec<T>` / `Vec<f32>` 等安全容器由 `wasm-bindgen` 自动管理内存。同一工具链对“导出复杂结构体”的内存管理范式在两章不一致（手动裸指针 vs 安全容器自动管理），且 14 章未标注为“底层演示/不推荐生产使用”。

- **符号用法不一致：`wasm-pack build` 目标参数差异**  
  第 14 章 14.8.5 节使用 `--target bundler`；第 15 章 15.4 节 "wasm-pack：Rust 到 Web 的零配置高速公路" 列举 `--target web` / `--target bundler` / `--target nodejs`，15.7 节 "步骤 2" `package.json` 脚本中使用 `--target bundler`。虽均合法，但 14 章未说明为何选 `bundler` 而非 `web`，且 15 章未统一规范“浏览器直用选 `web`、打包器选 `bundler`”的决策依据。

- **前后来源引用不准确：第 14 章概念地图中 `P135/P137` 指向的内容在当前章节（第 15 章）而非已生成章节**  
  第 14 章概念地图 "WebAssembly 跨端赋能" 及其子项、"跨端技术选型决策框架" 末项、"方法演进图" 均标注来源为 `P135, P137`。但 `P135/P137` 对应的原文摘录内容（Wasm 核心概念、工具链实战、互操作、SIMD/多线程/GC、Rust 图像处理实战）完整出现在 **当前待检查章节（第 15 章）**，而 **已生成章节（第 1-14 章）中无对应内容**。这属于“前引后文”错误：第 14 章引用了尚未生成的第 15 章素材 ID 作为来源支撑。

- **素材来源格式不一致：第 14 章引用 `AnkEdEtEtoXIbexWlQ3cL6zenFf.md` 但第 15 章未在概念地图来源列出该 ID**  
  第 14 章 "多源对照" 与 "原文摘录" 多处引用 `AnkEdEtEtoXIbexWlQ3cL6zenFf.md`（如 "AI 编程助手现状"、"RAG 在前端知识库落地"、"AI 原生应用开发核心范式转变"），但第 15 章概念地图的来源列表中 **完全缺失该素材 ID**，导致同一素材在两章的引用清单不一致。

- **素材来源格式不一致：第 14 章引用 `A47Vd3fekoelzRxZpdUcTl9Cn7W.md` 但第 15 章概念地图来源列表中无该 ID**  
  第 14 章 "14.4.10 原文摘录" 引用 `A47Vd3fekoelzRxZpdUcTl9Cn7W.md` 印证 "AI 辅助迁移工程实践"，但第 15 章概念地图来源列表中 **无该 ID**。

- **素材来源格式不一致：第 14 章引用 `AiCrd19EAoPvvPx0HSJczxk3nfC.md` 但第 15 章概念地图来源列表中无该 ID**  
  第 14 章 "14.6.5 原文摘录" 与 "14.7.5 原文摘录" 引用 `AiCrd19EAoPvvPx0HSJczxk3nfC.md`，但第 15 章概念地图来源列表中 **无该 ID**。

- **素材来源格式不一致：第 14 章引用 `20230418_135.md` / `20230418_137.md` 等数十个 `20230418_xxx.md` 格式 ID，但第 15 章概念地图来源列表仅含 `AnkEdEtEtoXIbexWlQ3cL6zenFf.md` 单一 ID**  
  第 14 章概念地图、各节"原文摘录"大量使用 `20230418_001.md` 至 `20230418_157.md` 格式的素材 ID；第 15 章概念地图来源列表 **仅包含 `AnkEdEtEtoXIbexWlQ3cL6zenFf.md`**，两章来源 ID 命名规范、粒度、覆盖范围完全不一致。
