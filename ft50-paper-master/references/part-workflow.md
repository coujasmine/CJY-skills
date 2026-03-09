# 论文 Part 映射清单

## Part 0 选题/问题定义
- 调用 skill: `ft50-part-introduction`
- 输入: 题目、研究问题、目标期刊
- 输出: 现象级问题、世界观归属、FT50放大建议
- 失败信号: X->Y 变量题、仅样本替换

## Part 1 Introduction
- 调用 skill: `ft50-part-introduction`
- 输入: 引言草稿
- 输出: 四段式重写（现象、缺口、问题定位、贡献预告）
- 失败信号: “研究较少”替代现实张力

## Part 2 Literature/Theory
- 调用 skill: `ft50-part-theory-dialogue`
- 输入: 理论综述段落
- 输出: 主干/辅干理论结构、挂名风险、重写建议
- 失败信号: 理论拼盘、核心构念缺失

## Part 3 Hypotheses/Model
- 调用 skill: `ft50-part-theory-building` + `ft50-part-mechanism`
- 输入: 假设推导、模型图说明
- 输出: 机制链、边界条件、跳步修复
- 失败信号: 中介调节堆叠但无过程逻辑

## Part 4 Methods
- 调用 skill: `ft50-part-methods-results`
- 输入: 数据、变量、模型、识别策略
- 输出: 设计风险、测量风险、内生性补强
- 失败信号: 层级不匹配、构念测量错位

## Part 5 Results
- 调用 skill: `ft50-part-methods-results`
- 输入: 结果表与解释文字
- 输出: 理论化解释、稳健性优先项
- 失败信号: 只报显著，不回扣机制

## Part 6 Discussion/Conclusion
- 调用 skill: `ft50-part-discussion-contribution`
- 输入: 讨论草稿
- 输出: 贡献三条、边界三条、启示与局限
- 失败信号: 贡献空泛、重复结果

## Part A AI/ML 专项（可插入任意 part）
- 调用 skill: `ft50-part-ai-ml`
- 输入: 涉及算法的题目、理论、方法段
- 输出: AI角色判定、理论增量、方法主导风险
- 失败信号: 算法主语、纯精度贡献

## Part B 新构念/量表专项（可插入任意 part）
- 调用 skill: `ft50-part-construct-measurement`
- 输入: 构念定义、量表条目、改编说明
- 输出: 新构念必要性判定、量表规范修订
- 失败信号: 旧构念改名、拼盘式拼题
