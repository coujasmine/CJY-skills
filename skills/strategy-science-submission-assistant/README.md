# Strategy Science Submission Assistant

这是一个面向 **Strategy Science (INFORMS)** 投稿的专项 skill，不是泛用论文润色器。它的目标是把论文送审前最容易被 Strategy Science 编辑和审稿人抓住的问题提前暴露出来：理论贡献是否够 sharp，方法和 claim 是否对齐，AI 风格是否明显，引用是否真实且支持 claim，投稿包是否符合 INFORMS 要求。



## 功能模式

| Mode | 用途 | 是否改写 |
|---|---|---|
| `POLISH` | 按 SS 风格重写/润色 manuscript | 是 |
| `AUDIT` | 投稿前总体诊断 | 否 |
| `WRITING_CHECK` | 写作质量和 AI 风格自查 | 否 |
| `CITATION_AUDIT` | 引用存在性和 claim-citation 对齐检查 | 否 |
| `REVIEW` | 模拟 Strategy Science 编辑和审稿人 | 否 |
| `SECTION` | 单独重写 abstract / intro / theory / methods 等 | 是 |
| `PACKAGE` | cover letter / disclosure / submission package QA | 是 |
| `RESPOND` | Strategy Science R&R 回复信 | 是 |

## Claude Code 中如何安装

Claude Code 官方文档目前支持把 skill 放在个人目录或项目目录。个人 skill 路径是 `~/.claude/skills/<skill-name>/SKILL.md`，项目 skill 路径是 `.claude/skills/<skill-name>/SKILL.md`。自定义 subagent 可以放在 `.claude/agents/` 或 `~/.claude/agents/`。

### 方式 A：个人全局安装

```bash
git clone https://github.com/coujasmine/CJY-skills.git ~/CJY-skills
mkdir -p ~/.claude/skills
ln -s ~/CJY-skills/skills/strategy-science-submission-assistant ~/.claude/skills/strategy-science-submission-assistant
```

安装 subagents：

```bash
mkdir -p ~/.claude/agents
cp ~/CJY-skills/skills/strategy-science-submission-assistant/subagents/*.md ~/.claude/agents/
```

然后在 Claude Code 中直接调用：

```text
/strategy-science-submission-assistant Run a WRITING_CHECK on my Strategy Science introduction. Do not rewrite.
```

### 方式 B：项目级安装

在你的论文项目根目录执行：

```bash
mkdir -p .claude/skills .claude/agents
cp -R /path/to/CJY-skills/skills/strategy-science-submission-assistant .claude/skills/
cp /path/to/CJY-skills/skills/strategy-science-submission-assistant/subagents/*.md .claude/agents/
```

项目级安装适合和合作者共享，个人全局安装适合你自己长期使用。

## 常用指令示例

### 1. 写作质量检查

```text
/strategy-science-submission-assistant Run WRITING_CHECK on this introduction. Report AI-style markers, sentence burstiness, throat-clearing openers, and SS contribution-structure risks. Do not rewrite.
```

### 2. 引用审计

```text
/strategy-science-submission-assistant Run CITATION_AUDIT. I will provide the manuscript excerpt, reference list, and locator notes. Check reference existence, missing locators, and whether each citation supports the claim.
```

### 3. Strategy Science 模拟审稿

```text
/strategy-science-submission-assistant Run REVIEW for a first submission to Strategy Science. Use the review contract first, then simulate AE, theory reviewer, methods reviewer, style/positioning reviewer, devil's advocate, and editorial synthesis.
```

### 4. LLM-as-measurement 审计

```text
/strategy-science-submission-assistant Audit my GPT-coded construct measure for Strategy Science. Check prompt hygiene, human benchmark, Krippendorff alpha, multi-LLM robustness, hallucination review, and disclosure.
```

### 5. 投稿包检查

```text
/strategy-science-submission-assistant Run PACKAGE QA for my INFORMS / Strategy Science submission. Check abstract length, keywords, blinding, AI-use disclosure, IRB, data availability, cover letter, and file inventory.
```

## 本地脚本

这些脚本可以在 skill 目录中直接运行：

```bash
python3 scripts/check_writing_quality.py manuscript.txt
python3 scripts/check_sentence_burstiness.py manuscript.txt
python3 scripts/extract_references.py references.txt --json
python3 scripts/extract_citation_contexts.py manuscript.txt --json
python3 scripts/verify_references.py references.txt
python3 scripts/verify_references.py --online references.txt
```

`verify_references.py --online` 会尝试查询 Crossref、OpenAlex 和 Semantic Scholar。没有网络权限时，可以先用离线模式；离线模式只能检查结构和缺失字段，不能证明文献存在。

## 关于 `/plugin marketplace add`

目前这个目录是一个 standalone skill，可以通过 `.claude/skills/` 直接使用。如果未来要像 ARS 一样用：

```text
/plugin marketplace add coujasmine/CJY-skills
/plugin install <plugin-name>@<marketplace-name>
```

仓库还需要补 Claude Code plugin manifest 和 marketplace 配置。Claude Code 的插件模式会给 skill 加 namespace，例如 `/plugin-name:strategy-science-submission-assistant`。在当前版本中，最稳妥的用法仍是上面的个人或项目级 skill 安装。

## 参考文档

- Claude Code skills: https://code.claude.com/docs/en/skills
- Claude Code subagents: https://code.claude.com/docs/en/sub-agents
- Claude Code plugins: https://code.claude.com/docs/en/plugins
- Claude Code plugin marketplace: https://code.claude.com/docs/en/discover-plugins

