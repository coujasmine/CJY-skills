# Start Here

这个仓库不是单纯的 `skills` 集合，也不是单纯的文献文件夹，而是一个分层使用的科研系统。

## 先判断你当前要做什么

### 我想搭自己的科研知识库
从 [knowledge-base/README.md](/Users/caojiaying/Desktop/yiyuan mai/论文专家agent/knowledge-base/README.md) 开始。

### 我手头有一篇论文想诊断或重写
从 [docs/SKILLS-INDEX.md](/Users/caojiaying/Desktop/yiyuan mai/论文专家agent/docs/SKILLS-INDEX.md) 找对应 skill。

### 我不知道某类内容该存在哪里
先看 [docs/REPO-MAP.md](/Users/caojiaying/Desktop/yiyuan mai/论文专家agent/docs/REPO-MAP.md)。

### 我想先把仓库跑起来，不想一开始太复杂
只用下面 6 个目录就够了：

- `knowledge-base/00_首页与导航`
- `knowledge-base/01_研究方向`
- `knowledge-base/02_文献库`
- `knowledge-base/03_理论库`
- `knowledge-base/05_选题与Idea池`
- `knowledge-base/09_项目库`

## 两套系统的分工

### `knowledge-base/`
回答的是：你长期知道什么、积累了什么、接下来可以做什么。

### `skills/`
回答的是：当你处于具体的研究阶段（评 idea、做研究设计、投稿前润色、转 Word 排版）时，应该如何按目标期刊或上游环节去诊断、改写、打包。目前 4 个 skill：`utd24-proposal-optimizer`（上游）、`jbr-submission-assistant`、`strategy-science-submission-assistant`、`markdown-word`。

## 推荐的使用顺序

1. 日常把文献和想法放进 `knowledge-base/`
2. 形成项目后，在 `knowledge-base/09_项目库/` 里推进
3. 需要高强度诊断时，再调用 `skills/`
4. 修改经验和模板，反过来沉淀回 `knowledge-base/10_模板库/` 和 `11_复盘与成长/`
