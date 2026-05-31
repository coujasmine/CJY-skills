# Repository Map

## 顶层结构

```text
.
├── docs/
├── knowledge-base/
├── skills/
└── assets/
```

## 每一层放什么

### `docs/`
放“怎么使用这个仓库”的文档，不放研究内容本身。

建议先读：
- `START-HERE.md`
- `SKILLS-INDEX.md`

### `knowledge-base/`
放你的个人科研知识沉淀，是这个仓库的主战场。

目录逻辑：
- `00_首页与导航`：你的研究总面板、收件箱、使用说明
- `01_研究方向`：主题、关键词、问题、研究空白
- `02_文献库`：按篇精读的文献卡
- `03_理论库`：理论卡、概念边界、常见误用
- `04_方法库`：设计、测量、识别、稳健性
- `05_选题与Idea池`：早期选题与可投稿题目
- `06_专题综述`：从零散文献走向主题综述
- `07_论文写作库`：标题、摘要、引言、假设、讨论等写作素材
- `08_期刊与投稿`：目标期刊、风格、投稿记录
- `09_项目库`：正在做的具体课题
- `10_模板库`：笔记模板、理论卡模板、Idea 卡模板
- `11_复盘与成长`：导师反馈、月度复盘、拒稿经验

### `skills/`
放可直接调用的“论文专家”技能。目前 4 个 skill，按使用阶段分两类：

**上游研究向**
- `utd24-proposal-optimizer` — idea / design / proposal 阶段优化，针对 UTD24（SMJ、AMJ、ASQ、OS、MS strategy/innovation/entrepreneurship、AMR）

**期刊投稿向**
- `jbr-submission-assistant` — 投 Journal of Business Research 时润色 / 审查 / 模拟评审 / AI 风格去除 / 投稿包打包
- `strategy-science-submission-assistant` — 投 Strategy Science 时的同类工具
- `markdown-word` — Markdown → Word 投稿格式排版（已支持 JBR、Strategy Science、generic 模板）

详细 mode、subagent、调用顺序见 `docs/SKILLS-INDEX.md`。

### `assets/source-materials/`
放原始手册、抽取文本和不适合作为日常入口的底层资料。

## 一个简单判断标准

- 如果内容需要长期复用、持续沉淀，放 `knowledge-base/`
- 如果内容是工作流、诊断规则、提示结构，放 `skills/`
- 如果内容只是原始参考资料，放 `assets/`
