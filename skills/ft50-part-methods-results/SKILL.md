---
name: ft50-part-methods-results
description: 用于评审并润色 Methods 与 Results 部分，校验研究设计是否支撑理论命题（测量一致性、层级匹配、因果识别），检查结果解释是否回扣机制，并输出 polished 英文改写版本。
---

# Part: Methods & Results

## 目标
让方法服务理论，而不是方法喧宾夺主。完成诊断后，直接输出符合 FT50 标准的英文改写版本。

---

## Phase 1: 诊断评审

### Methods 检查
1. 样本与理论对象匹配（主体、情境、层级）。
2. 构念测量与定义一致（反映式/形成式区分）。
3. 识别策略处理内生性（FE/IV/匹配/滞后等）。
4. 模型与机制一致（避免只跑净效应）。

### Results 检查
1. 结果是否按理论命题顺序报告。
2. 是否解释关键模式而非仅报显著性。
3. 异质性/边界结果是否真正对应理论边界。

### 红线
- 结果能显著但无法解释机制：判"统计成立，理论不足"。

### 诊断输出模板
- 设计风险清单：
- 结果解释缺口：
- 必做稳健性（最多3项）：
- 红线检查：通过/不通过 + 原因

---

## Phase 2: 英文润色改写

### 强制规则
1. 最终改写内容必须是英文；不输出中文句子作为正文。
2. **绝对不改变**原始实证结果、变量关系方向、效应符号、统计显著性和核心识别策略。
3. 只改语言表达、结构组织和结果解释的清晰度。
4. 结果报告必须先写实质性发现（substantive finding），再写统计数字。

### Methods 专用句式模板
#### 研究设计概述
- `We test our arguments using [design] based on [sample/context].`
- `Our empirical setting is appropriate because [fit to theory].`

#### 样本与数据
- `Our sample consists of [N] [units] observed over [time period] from [source].`
- `We focus on [context] because it offers [theoretical advantage for identification].`

#### 测量
- `All focal constructs were measured using established scales adapted from [source].`
- `[Construct] was operationalized as [measure], following [citation].`
- `Results from [CFA/reliability checks] indicate acceptable measurement quality.`

#### 识别策略
- `To address endogeneity concerns, we employ [strategy: FE/IV/matching/DID/RDD].`
- `We instrument [endogenous variable] with [instrument], which satisfies the exclusion restriction because [reason].`

### Results 专用句式模板
#### 主效应报告
- `Results provide support for Hypothesis 1.`
- `As shown in Table [n], [substantive finding in words] (beta = ..., p < ...).`

#### 稳健性
- `This pattern remains robust across alternative specifications.`
- `The effect is substantively unchanged when we [alternative model/control/sample].`

#### 异质性/边界
- `The effect is stronger when [moderator], consistent with Hypothesis [n].`
- `Subsample analyses reveal that the relationship holds for [group A] but not [group B], suggesting [theoretical interpretation].`

### 高频误用替换（Methods & Results 场景）
- Bad: `We used a questionnaire and did analysis.` → Better: `We collected survey data and estimated [model], controlling for [key covariates].`
- Bad: `H1 is significant.` → Better: `Results support H1: [effect in words] (beta = ..., p < ...).`
- Bad: `See Table 2.` → Better: `As shown in Table 2, [main substantive pattern].`
- Bad: `Our results confirm the theory.` → Better: `Our results are consistent with the theory.`
- Bad: `X proves that Y causes Z.` → Better: `X provides evidence that Y may causally affect Z.`

### Claim 强度校准
- 描述性证据：`shows`, `indicates`, `documents`
- 相关性推断：`is associated with`, `is linked to`, `correlates with`
- 机制一致推断：`is consistent with the mechanism that`, `suggests that [M] may explain`
- 因果语言（仅强设计）：`increases`, `reduces`, `causally affects`
- 有限因果：`may influence`, `appears to affect`, `is consistent with a causal interpretation`

### 执行流程
1. 基于 Phase 1 诊断结果，确定 Methods 中的设计描述缺口和 Results 中的解释缺口。
2. 建立术语表：统一变量名、方法名、统计表达。
3. Methods：按"设计 → 样本 → 测量 → 识别策略 → 模型"顺序改写。
4. Results：按理论命题顺序改写，每条假设先说实质发现，再报数字。
5. 校准 claim 强度，确保语言与识别策略匹配（相关设计不用因果语言）。

### 润色输出模板
1. `Polished Version`（英文，Methods 和 Results 分别输出）
2. `Key Edits`（英文，3-8条，说明主要改动与升级点）
3. `Word/Phrase Upgrades`（英文替换对照表）

---

## 完整输出结构

```
## Diagnostic Report
- 设计风险清单：
  1. ...
  2. ...
- 结果解释缺口：
  1. ...
- 必做稳健性：
  1. ...
- 红线检查：...

## Polished Methods
[完整改写的英文 Methods 部分]

## Polished Results
[完整改写的英文 Results 部分，按假设顺序输出]

## Key Edits
1. ...
2. ...
3. ...

## Word/Phrase Upgrades
| Original | Revised | Reason |
|----------|---------|--------|
| ...      | ...     | ...    |
```
