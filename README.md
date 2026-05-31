# Research Knowledge Base

这个仓库现在分成两层：

1. `knowledge-base/`：你的个人科研知识库，负责长期积累。
2. `skills/`：可调用的论文诊断与重写技能，负责即时执行。

如果你第一次打开这个仓库，建议按这个顺序使用：

1. 先看 [docs/START-HERE.md](/Users/caojiaying/Desktop/yiyuan mai/论文专家agent/docs/START-HERE.md)
2. 再看 [docs/REPO-MAP.md](/Users/caojiaying/Desktop/yiyuan mai/论文专家agent/docs/REPO-MAP.md)
3. 真正开始沉淀内容时，进入 [knowledge-base/README.md](/Users/caojiaying/Desktop/yiyuan mai/论文专家agent/knowledge-base/README.md)
4. 需要改论文时，查 [docs/SKILLS-INDEX.md](/Users/caojiaying/Desktop/yiyuan mai/论文专家agent/docs/SKILLS-INDEX.md)

## 现在的仓库结构

```text
.
├── README.md
├── docs/                 # 仓库入口、使用说明、技能地图
├── knowledge-base/       # 你的科研知识沉淀
├── skills/               # 论文专家技能包
└── assets/               # 原始参考资料
```

## 你应该怎么用

- 如果你要做自己的科研知识库：从 `knowledge-base/` 开始。
- 如果你要改一篇具体论文：从 `skills/` 开始。
- 如果你不知道用哪个 skill：先看 `docs/SKILLS-INDEX.md`。
- 如果你不知道一篇文献该放哪：先放进 `knowledge-base/02_文献库/`，再按主题汇总到 `06_专题综述/`。

## 四条最常用路径

### 1. 日常读文献
`knowledge-base/02_文献库/` -> `knowledge-base/06_专题综述/` -> `knowledge-base/05_选题与Idea池/`

### 2. 搭自己的研究方向
`knowledge-base/01_研究方向/` -> `knowledge-base/03_理论库/` -> `knowledge-base/04_方法库/`

### 3. 推进单个论文项目
`knowledge-base/09_项目库/` -> `knowledge-base/07_论文写作库/` -> `skills/`

### 4. 推进 / 投稿一篇论文
- 上游（idea / design / proposal 阶段）：`skills/utd24-proposal-optimizer/`
- 投 JBR：`skills/jbr-submission-assistant/`
- 投 Strategy Science：`skills/strategy-science-submission-assistant/`
- 转 Word、按期刊格式排版：`skills/markdown-word/`

## 目录定位

- [docs](/Users/caojiaying/Desktop/yiyuan mai/论文专家agent/docs)：先看这里，解决“这个仓库怎么用”。
- [knowledge-base](/Users/caojiaying/Desktop/yiyuan mai/论文专家agent/knowledge-base)：长期知识沉淀主目录。
- [skills](/Users/caojiaying/Desktop/yiyuan mai/论文专家agent/skills)：可复用的论文工作流。
- [assets/source-materials](/Users/caojiaying/Desktop/yiyuan mai/论文专家agent/assets/source-materials)：原始手册和抽取文本，不作为日常入口。
