# Skills Index

`skills/` 目录下目前有 4 个 skill。两类：**期刊投稿向**（拿到稿件之后做润色、审查、打包）和 **上游研究向**（idea / design / proposal 阶段的优化与排版）。

## 期刊投稿向

### `jbr-submission-assistant`
为 **Journal of Business Research (Elsevier)** 量身定制的稿件润色 / 审查 / 模拟同行评审 / AI 风格去除 / Cover Letter & Response / 投稿包打包工具。六个 mode（POLISH 默认 / AUDIT / REVIEW / SECTION / RESPOND / PACKAGE）加两个 subagent（`jbr-ai-decontaminator`、`jbr-gpt-measurement-auditor`）。

什么时候用：「polish my draft for JBR」「JBR fit check」「simulate JBR reviewers」「remove AI flavor from my JBR draft」「audit before JBR submission」「JBR cover letter」「format for JBR submission」。

### `strategy-science-submission-assistant`
为 **Strategy Science (INFORMS)** 量身定制的同类工具。六个 mode 加五个 subagent（`ss-ai-decontaminator`、`ss-llm-measurement-auditor`、`ss-claim-citation-auditor`、`ss-devils-advocate-reviewer`、`ss-editorial-synthesizer`），10 个机械化检查脚本（abstract / keywords / causal verbs / AI markers / writing quality / sentence burstiness / references / citation contexts / citation coverage / reference existence）。还有 expanded exemplar corpus（2024–2026 的 4 篇 SS 论文，用来做论证逻辑和措辞的更深层校准）。

什么时候用：「polish for Strategy Science」「SS reviewer simulation」「audit SS citation coverage」「remove AI flavor from SS draft」「SS desk-reject risk」。

## 上游研究向

### `utd24-proposal-optimizer`
针对 **UTD24 战略 / 创新 / 创业** outlets（SMJ、AMJ、ASQ、OS、MS Strategy / Innovation / Entrepreneurship sections、AMR；以及 Strategy Science 作为 UTD24-adjacent）的研究 proposal 优化器。四个 mode：

- **IDEA**：评 idea 站不站得住
- **DESIGN**：ex-ante 研究设计咨询（DiD vs PSM、机制怎么推假设、母理论挂哪棵树）
- **MANUSCRIPT**：proposal 或 pre-submission 稿件按 5 维度（RQ / 文献对话 / 理论机制 / 假设架构 / 方法识别）打分
- **REVIEW**：模拟 AE / Reviewer 报告

支持中文情境与 AI × strategy 新兴脉络，不只是西方主流理论。

什么时候用：「评价这个 idea」「UTD24 水平」「怎么改才能投 SMJ/AMJ/ASQ」「母理论该挂哪棵树」「identification gap」「模拟 reviewer」。

### `markdown-word`
Markdown → Word 投稿格式排版工具。Pandoc + python-docx，per-journal YAML 配置（目前 jbr、strategy-science、generic 三套，加新期刊只需 1 个 YAML）。处理三线表、字体字号、行距、引用风格、参考文献格式。四个 mode：CONVERT（默认）/ VALIDATE / ADD-JOURNAL / TROUBLESHOOT。

什么时候用：「把 markdown 转成 word」「format for JBR/Strategy Science submission」「排版」「三线表」「生成投稿 Word」「加一个新期刊模板」。

## 推荐调用顺序

```
knowledge-base/ —————————————— 长期积累（文献、理论、方法、idea 池）
      ↓
utd24-proposal-optimizer ——— idea / design / proposal 阶段（上游决策）
      ↓
（用户自己写稿）
      ↓
jbr-submission-assistant   ——— 投 JBR 时
strategy-science-submission-assistant ——— 投 Strategy Science 时
      ↓
markdown-word ——————————————— 转 Word、按期刊格式排版
```

## 什么时候不要用 skill

- 你只是想长期存文献和观点：用 `knowledge-base/`
- 你还在发散选题、没形成研究问题：先用 `knowledge-base/05_选题与Idea池/`
- 你在做综述和理论梳理：先写进 `knowledge-base/06_专题综述/` 和 `03_理论库/`
- 你的目标期刊不在 JBR / Strategy Science / UTD24 列表里：上面这些 skill 不会乱套用——它们都会先检查 outlet 匹配，不匹配就拒绝
