# 决定性瞬间 · Decisive Moments

一个探索个人 taste 来源的轻量 Agent Skill。

从你选定的历史对话中，找出那些模型容易忽略、你却有依据地辨别出的差别，再沿着经历、社群参与和反馈追溯来历。有形成轨迹就讲故事，只有片段就呈现来源线索。

## 使用

将本仓库放入 Agent 的 Skills 目录，文件夹命名为 `decisive-moments`。以 Codex 的默认目录为例：

```sh
git clone https://github.com/Y0ung-Elephant/decisive-moments.git ~/.codex/skills/decisive-moments
```

如果已存在同名目录，先处理已有版本，不要覆盖自己的修改。自定义了 `CODEX_HOME` 时使用其下的 `skills` 目录。其他支持 `SKILL.md` 的 Agent 可使用各自的安装目录；历史访问能力取决于宿主环境。

然后对 Agent 说：

> 用 $decisive-moments 帮我找找我的 taste 从哪里来。先列出可选的历史范围。

也可以直接指定：

> 用 $decisive-moments 分析我提供的这份聊天记录。

## 会发生什么

1. **选择范围**：先发现可访问的数据源与时间范围，再由你选择；已指定范围时直接开始。
2. **寻找瞬间**：分批阅读，找观察角度、评价标准和行动方向上的转变。
3. **追溯来历**：寻找什么曾经纠正你的判断、哪些关系与实践带来了新视角，区分记录、本人自述与推测。
4. **交付故事**：通常生成 2–4 条故事，附原文定位；证据少就少写，不凑数。

独立回放是可选辅助手段，不会默认重演全部历史。Skill 本身只有一个 Markdown 文件，不依赖专用服务或额外 API。

## 边界

这是探索性玩具，不是人格测评或经过验证的因果归因工具。人机差异是发现入口，不是 taste 的定义。模型一次没想到，并不证明其他模型也想不到；记录里看到某种判断，也不意味着已找到它的起源。

灵感来自 Tim Sullivan 的文章 [Beyond slop, taste, and AI moral panic: What social science tells us](https://a16zcrypto.com/posts/article/beyond-slop-taste-ai-social-science/)，重点借用跨社群参与与反馈训练两种解释视角。

## 数据

历史记录保持只读，Skill 不要求上传记录到本仓库或另一个分析服务。所选内容仍会进入你正在使用的 Agent/模型上下文，具体数据处理遵循该宿主服务。

生成的报告可能包含个人原话、本地路径和会话标识，默认作为私人结果使用，分享前另行脱敏。本仓库只包含通用 Skill 和说明，不包含作者的聊天记录、测试报告或个人案例；根目录采用 Git 跟踪白名单，避免运行结果被误提交。
