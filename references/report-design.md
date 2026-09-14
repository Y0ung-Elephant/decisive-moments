# 报告页：先被看见，再看证据

默认生成离线 HTML 肖像与 Markdown 证据报告。HTML 使用 `../assets/report.html`，通过 `../scripts/render_report.py` 注入数据，不必为每个用户重写页面。

## 文案

- **每条 taste 一句金句**：从已经通过候选筛选的辨别与取舍中提炼金句，让人读到这个人独有的评价尺度。可以带褒奖、惊奇、比喻和情绪共鸣，赞赏要落在已找到的具体取舍上。
- **一句认出自己的来历**：紧随金句，用一个独有细节说明这种眼光；有来源线索时，再点出可能交汇的经验或形成判断的训练。推测用“我猜”“像是”等自然措辞明示，不能只把不确定性藏在展开项。
- **来源与瞬间**：正文说清具体对象、辨别与取舍，再讲来源发现或假设，用 1–2 个短引文承接。已有判断却找不到来历时，坦然保留来源未解。
- **分享金句**：转为第一人称也可以，让人愿意借它表达自己。它是文学化概括，不冒充用户原话。

巴纳姆式共鸣可以体现在读者容易代入的修辞；事实仍来自记录。不要编造排名、罕见比例、被误解的经历或心理动机，也不为了取悦把所有人写成同一个优秀人格。避开一串抽象优点，优先给一个值得记住的视角。

报告面向未参与制作过程的读者，直接讲这个人的发现。把制作时的反馈落实为成品，不把改稿理由、产品规则或对话中的纠正写成开场宣言。

交付前从金句反查对应故事：能否找出它概括的评价尺度与实际取舍？若只剩目标、成长愿望或学习方法，回到候选筛选。来源故事再动人，也不能替代这一步。

## 渲染

将以下结构保存为私人 JSON（文本之外的字段见示例；`story` 是对应故事的零基索引）：

```json
{
  "preset": "print",
  "compare": false,
  "tastes": [{
    "signature": "这一条判断的题签，非固定人格类型",
    "share": "概括评价尺度或取舍眼光的金句，可换行",
    "detail": "体现这份眼光的具体细节，可接来源线索",
    "story": 0
  }],
  "scope": "本次实际读取范围及重要限制",
  "stories": [{
    "title": "这一条发现的金句",
    "insight": "具体对象、辨别出的差别及因此作出的取舍",
    "origin": "有依据的来源或自然表达的待确认线索",
    "limit": "展开后显示的解释边界",
    "moments": [{
      "date": "记录日期",
      "quote": "准确的用户短引文",
      "context": "这句话当时改变了什么",
      "source": "真实文件与行号或会话标识，纯文本"
    }]
  }]
}
```

运行 `python3 <skill目录>/scripts/render_report.py <私人JSON> <新的HTML路径>`。输出文件须不存在。页面离线运行，无远程字体、分析请求或自动发布；Markdown 保留可点击的本地证据链接。若 Python 不可用，可用现有工具安全序列化 JSON 替换模板中的唯一数据占位符：转义 `<`、`>`、`&`，数据只通过 `textContent` 展示。

多条结论置顶；每张卡片通往自己的故事。待展开线索用正文清楚标明缺口，可放在观察之后；不以肯定式金句掩盖证据状态。数量随发现而定，不把一句话拆成多条来凑数。浏览器检查桌面和手机宽度，核对横滑、方向键、前后按钮、对应故事、折叠证据、复制与 PNG 保存；切换风格保持当前卡片。PNG 只使用当前卡片的 `share`、`signature` 和品牌文字；这些字段必须经过脱敏，不能放对话原文、路径或身份信息。整个 HTML 含私人证据，不能当作脱敏分享卡自动发布。

## 设计依据

可借鉴 [Spotify Wrapped](https://newsroom.spotify.com/2024-12-04/wrapped-user-experience-2024/) 的个人回顾、叙事与可分享卡片，[16Personalities](https://www.16personalities.com/intp-strengths-and-weaknesses) 的第二人称和优点命名。[Forer 的原始研究](https://pubmed.ncbi.nlm.nih.gov/18110193/) 提醒我们：读者觉得“准”不能代替个性化证据。这些是呈现参考，不代表本产品的传播效果已验证；日常渲染无需重新联网。

## 三种可比较的预设

`preset` 可取以下值。用户要比较时设置 `compare: true`，显示同内容的三风格切换器；正常交付隐藏切换器。默认采用 `print` 宣言海报风格；用户明确指定时使用其他预设。

- `editorial` / 纸上肖像：暖白纸感、宋体金句、细线与留白。参考 [minimalist-ui](https://github.com/Leonxlnx/taste-skill/blob/main/skills/minimalist-skill/SKILL.md)。
- `print` / 宣言海报：朱红、粗黑体、直角硬边与强排版。参考 [industrial-brutalist-ui 的 Swiss Industrial Print](https://github.com/Leonxlnx/taste-skill/blob/main/skills/brutalist-skill/SKILL.md)。
- `soft` / 柔光卡组：银灰、浅绿、双层圆角与柔和纵深。参考 [high-end-visual-design 的 Soft Structuralism / Z-Axis Cascade](https://github.com/Leonxlnx/taste-skill/blob/main/skills/soft-skill/SKILL.md)。

以上是对原 Skill 风格约束的轻量适配，并未安装其依赖或执行其工作流。三者共享真实内容与证据结构。层叠底卡只作装饰，只有当前卡片可交互；支持触屏横滑、方向键和可见按钮，尊重减少动态效果设置。输出保持离线，无远程字体。
