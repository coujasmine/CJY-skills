---
name: ft50-part-ai-ml
description: 用于评审并润色 AI/ML+管理论文，判定 AI/ML 在文中的角色、理论增量类型与方法主导风险，避免"只提升预测"却声称FT50贡献，并输出 polished 英文改写版本。
---

# Part: AI/ML

## 目标
确保 AI/ML 服务理论 puzzle，而不是成为方法展示。完成诊断后，直接输出符合 FT50 标准的英文改写版本。

---

## Phase 1: 诊断评审

### 角色判定
先判 AI/ML 角色：
- A 理论对象
- B 测量工具
- C 决策/优化工具
- D 纯预测工具

仅 A/B 且有明确理论 puzzle 时，进入 FT50 通道。

### 贡献类型
- 新机制来源（替代/增强、权力与学习变化）
- 测量显微镜（从非结构化数据提取理论变量）
- 决策规则边界（何时 ML 规则优于传统规则）

### 风险红灯
- 标题主语是算法名。
- 贡献只写"首次用XX算法""准确率提升X%"。
- 算法堆砌且无理论选择理由。

### 诊断输出模板
- AI/ML角色判定：
- 理论 puzzle：
- 理论增量：
- 方法主导风险：
- 投稿定位建议（FT50或降档）：
- 红线检查：通过/不通过 + 原因

---

## Phase 2: 英文润色改写

### 强制规则
1. 最终改写内容必须是英文；不输出中文句子作为正文。
2. 不改变原始技术实现和实证结果，只改语言表达与理论定位的清晰度。
3. AI/ML 方法描述必须服务于理论 puzzle，而非展示技术细节。
4. 每段保留"topic sentence → evidence/logic → implication"结构。

### AI/ML 论文专用句式模板
#### 理论定位（AI 作为理论对象）
- `The introduction of [AI/ML technology] fundamentally alters [theoretical mechanism], because [reason].`
- `We theorize that [AI/ML] serves as a new source of [mechanism: substitution/augmentation/learning], which challenges the assumption that [prior assumption].`

#### 测量定位（AI 作为测量工具）
- `We leverage [NLP/CV/ML method] to extract [theoretical construct] from [unstructured data source], enabling measurement at a scale and granularity previously unavailable.`
- `This computational approach allows us to operationalize [construct] in a way that overcomes [limitation of traditional measures].`

#### 方法合法性
- `Our choice of [algorithm/model] is driven by the theoretical need to [capture X / classify Y / extract Z], rather than by predictive performance alone.`
- `We select [method] because its architecture is particularly suited to [theoretical feature of data], as opposed to [alternative methods] which assume [inappropriate assumption].`

#### 理论增量表述
- `Beyond predictive accuracy, [ML method] reveals [substantive pattern] that extends [theory] by [specific theoretical increment].`
- `The use of [AI/ML] is not merely methodological but substantive: it uncovers [mechanism/pattern] invisible to traditional approaches.`

### 高频误用替换（AI/ML 场景）
- Bad: `We are the first to use [algorithm] in [field].` → Better: `We leverage [algorithm] to address [specific theoretical puzzle] that existing methods cannot resolve.`
- Bad: `Our model achieves X% accuracy.` → Better: `Our model identifies [substantive pattern], with a classification accuracy that supports the theoretical distinction between [A] and [B].`
- Bad: `We apply deep learning to management data.` → Better: `We employ [specific DL architecture] to extract [construct] from [data type], motivated by the theoretical need to capture [specific feature].`

### 执行流程
1. 基于 Phase 1 诊断结果，确定 AI/ML 角色定位和理论增量表述的改进方向。
2. 建立术语表：统一算法名、理论构念名、数据描述术语。
3. 改写重心：强化理论 puzzle 驱动的叙事，弱化纯技术展示。
4. 先做句级修复（技术表述精确化），再做段级重写（理论-方法衔接）。
5. 确保每个 AI/ML 方法选择都有理论依据。

### 润色输出模板
1. `Polished Version`（英文，按段输出涉及 AI/ML 的改写部分）
2. `Key Edits`（英文，3-8条，说明主要改动与升级点）
3. `Word/Phrase Upgrades`（英文替换对照表）

---

## 完整输出结构

```
## Diagnostic Report
- AI/ML角色判定：...
- 理论 puzzle：...
- 理论增量：...
- 方法主导风险：...
- 投稿定位建议：...
- 红线检查：...

## Polished AI/ML Sections
[完整改写的英文版本，涵盖涉及 AI/ML 的所有相关段落]

## Key Edits
1. ...
2. ...
3. ...

## Word/Phrase Upgrades
| Original | Revised | Reason |
|----------|---------|--------|
| ...      | ...     | ...    |
```
