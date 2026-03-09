---
name: ft50-paper-master
description: 用于按《论文专家规范手册》对整篇论文进行分阶段诊断、重写与评审编排，并在最后执行全文英文润色。适用于需要从选题到理论贡献做全流程把关，或需要按“每个 part”输出修改意见与重写草稿的场景。
---

# FT50 Paper Master

按以下固定顺序执行，不跳步：
1. 第2章问题判断
2. 第3章理论对话
3. 第4章理论建构
4. 第5章机制完整性
5. 第6章AI/ML规范（仅AI论文）
6. 第7章新构念与量表规范（涉及构念/量表时）
7. 第8章综合评审输出
8. 第9章全文英文润色（默认必做）

## 输入最小要求
- 论文题目或研究问题
- 当前稿件（完整稿或指定 part）
- 目标期刊层级（如 AMJ/SMJ/RP）
- 语言目标（默认：英文期刊写作）

## 标准输出格式
按以下 9 段输出：
1. `总体结论`：FT50 潜力等级（高/中/低）+一句话理由
2. `问题层面`：是否属于创新/创业核心世界观；若不合格，明确写“问题层面即失败”
3. `理论对话`：主干理论、辅助理论、是否挂名
4. `理论建构`：现象张力、概念创造、边界条件
5. `机制链条`：micro→meso→capability/structure→macro，标注跳步点
6. `方法与证据`：是否支持理论命题（含内生性/测量质量）
7. `分 part 修改单`：按 Introduction/Theory/Methods/Results/Discussion 给可执行修改
8. `全文英文润色`：给出全稿 polished version（英文），并附 key edits 与高频替换
9. `下一轮优先任务`：仅列 3 条最关键动作

## 强制判定规则
- 仅有 X→Y 关系且缺少不确定性/机会/涌现过程：判低潜力。
- 理论挂名、拼盘式整合、边界不清：降档。
- 没有 micro→macro 机制链：不得称“机制论文”。
- AI/ML 仅提高预测精度但无理论增量：不得走 FT50 路线。
- 若用户目标为国际期刊写作，最终稿必须完成全文英文润色；不得仅润色单一 part。

## 与子技能协同
需要逐段重写时，按 part 调用对应子 skill：
- 选题与引言：`ft50-part-introduction`
- 文献与理论定位：`ft50-part-theory-dialogue`
- 理论模型与命题：`ft50-part-theory-building`
- 机制链与假设逻辑：`ft50-part-mechanism`
- 方法与结果：`ft50-part-methods-results`
- 讨论与贡献：`ft50-part-discussion-contribution`
- AI论文：`ft50-part-ai-ml`
- 新构念/量表：`ft50-part-construct-measurement`
- 全文英文润色（最后统一执行）：`ft50-academic-english-polish`

执行约束：
1. 先完成结构与理论层改写，再做语言润色，避免“边润色边改理论”导致术语漂移。
2. `ft50-academic-english-polish` 默认作用于全文，不只单段。
3. 润色阶段不得改变结论方向、效应符号、统计显著性和核心识别策略。

读取 [references/part-workflow.md](references/part-workflow.md) 获取“每个论文 part 的输入/输出/失败信号”速查。
