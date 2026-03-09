---
name: ft50-paper-master
description: 用于按《论文专家规范手册》对整篇论文进行分阶段诊断、重写与评审编排。适用于需要从选题到理论贡献做全流程把关，或需要按“每个 part”输出修改意见与重写草稿的场景。
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

## 输入最小要求
- 论文题目或研究问题
- 当前稿件（完整稿或指定 part）
- 目标期刊层级（如 AMJ/SMJ/RP）

## 标准输出格式
按以下 8 段输出：
1. `总体结论`：FT50 潜力等级（高/中/低）+一句话理由
2. `问题层面`：是否属于创新/创业核心世界观；若不合格，明确写“问题层面即失败”
3. `理论对话`：主干理论、辅助理论、是否挂名
4. `理论建构`：现象张力、概念创造、边界条件
5. `机制链条`：micro→meso→capability/structure→macro，标注跳步点
6. `方法与证据`：是否支持理论命题（含内生性/测量质量）
7. `分 part 修改单`：按 Introduction/Theory/Methods/Results/Discussion 给可执行修改
8. `下一轮优先任务`：仅列 3 条最关键动作

## 强制判定规则
- 仅有 X→Y 关系且缺少不确定性/机会/涌现过程：判低潜力。
- 理论挂名、拼盘式整合、边界不清：降档。
- 没有 micro→macro 机制链：不得称“机制论文”。
- AI/ML 仅提高预测精度但无理论增量：不得走 FT50 路线。

## 与子技能协同
需要逐段重写时，调用对应子 skill：
- 选题与引言：`ft50-part-introduction`
- 文献与理论定位：`ft50-part-theory-dialogue`
- 理论模型与命题：`ft50-part-theory-building`
- 机制链与假设逻辑：`ft50-part-mechanism`
- 方法与结果：`ft50-part-methods-results`
- 讨论与贡献：`ft50-part-discussion-contribution`
- AI论文：`ft50-part-ai-ml`
- 新构念/量表：`ft50-part-construct-measurement`

读取 [references/part-workflow.md](references/part-workflow.md) 获取“每个论文 part 的输入/输出/失败信号”速查。
