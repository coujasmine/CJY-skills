---
name: ft50-part-construct-measurement
description: 用于评审并润色新构念与量表 part，判断是否应引入新构念，规范既有量表的定义、改编、计分、结构检验与边界说明，并输出 polished 英文改写版本。
---

# Part: Construct & Measurement

## 目标
避免无效造概念，确保量表使用规范且可审稿防守。完成诊断后，直接输出符合 FT50 标准的英文改写版本。

---

## Phase 1: 诊断评审

### 新构念必要性
至少满足 3 项才考虑：
1. 直指理论盲点
2. 改变现象组织方式
3. 与近邻构念边界清晰
4. 跨情境稳定并有增量预测
5. 让理论更简洁

### 高风险信号
- 旧构念加前缀（AI/数字化/绿色等）。
- 多个旧构念打包无 emergent property。
- 去掉新词后故事仍完全成立。

### 量表规范
1. 先核对原始定义与理论角色。
2. 不随意改维度结构；改动需理论+统计依据。
3. 跨语境必须翻译-回译并做结构检验。
4. 区分反映式与形成式模型。
5. 避免拼盘式拼题并沿用原名。

### 诊断输出模板
- 是否值得新构念：是/否 + 依据
- 量表使用风险：
- 必补检验：
- 命名与定义修订建议：
- 红线检查：通过/不通过 + 原因

---

## Phase 2: 英文润色改写

### 强制规则
1. 最终改写内容必须是英文；不输出中文句子作为正文。
2. 不改变原始构念定义的核心含义，只改语言表达的精确度和学术规范性。
3. 构念定义必须包含：概念内涵、与近邻构念的区分、理论角色。
4. 量表描述必须包含：来源、维度、信效度证据。

### Construct & Measurement 专用句式模板
#### 构念定义
- `We define [construct] as [concise definition], distinguishing it from [neighboring construct] in that [key differentiator].`
- `Unlike [related concept], [construct] captures [unique theoretical dimension] that is central to [theoretical mechanism].`
- `[Construct] refers to [definition]. It differs from [Construct B] in [specific dimension] and from [Construct C] in [another dimension].`

#### 新构念合法性
- `Introducing [construct] is warranted because existing concepts—[A], [B], and [C]—fail to capture [specific theoretical gap].`
- `A new construct is necessary because [specific theoretical blind spot] cannot be addressed by simply combining [existing constructs].`

#### 量表来源与改编
- `We measured [construct] using the [N]-item scale developed by [author (year)], which has been validated in [contexts].`
- `Following [citation], we adapted the original scale by [specific modification], justified by [theoretical/contextual reason].`
- `Results from confirmatory factor analysis (CFA) support the [N]-factor structure (CFI = ..., RMSEA = ..., SRMR = ...).`

#### 效度论证
- `Discriminant validity was established through [AVE comparison / HTMT / chi-square difference tests], confirming that [construct A] is empirically distinct from [construct B].`
- `Convergent validity is supported by [factor loadings / AVE values] exceeding recommended thresholds.`

#### 反映式 vs 形成式
- `[Construct] is modeled as a reflective construct, as its indicators are manifestations of the underlying latent variable.`
- `[Construct] is modeled as a formative construct, as its dimensions represent distinct causal indicators that collectively constitute the concept.`

### 高频误用替换（Construct & Measurement 场景）
- Bad: `We created a new scale for X.` → Better: `We developed and validated a scale for [X], following [established scale development procedure: DeVellis/Hinkin].`
- Bad: `The reliability is good.` → Better: `Internal consistency was acceptable (Cronbach's alpha = ...; composite reliability = ...).`
- Bad: `We used X's scale.` → Better: `We measured [construct] using [author]'s [N]-item scale, adapted for [context] with [specific modifications].`
- Bad: `Our concept is different from Y.` → Better: `[Construct] differs from [Y] in that it captures [specific dimension], whereas [Y] emphasizes [different dimension].`

### 执行流程
1. 基于 Phase 1 诊断结果，确定构念定义、量表描述和效度论证的改进方向。
2. 建立术语表：统一构念名称、维度名称、统计指标表述。
3. 按"构念定义与合法性 → 量表来源与改编 → 效度检验 → 反映/形成式说明"顺序改写。
4. 先做句级修复（定义精确化、统计表述规范化），再做段级重写（论证逻辑衔接）。
5. 确保构念定义的三要素（内涵、区分、理论角色）齐全。

### 润色输出模板
1. `Polished Version`（英文，按段输出完整改写的 Construct & Measurement 部分）
2. `Key Edits`（英文，3-8条，说明主要改动与升级点）
3. `Word/Phrase Upgrades`（英文替换对照表）

---

## 完整输出结构

```
## Diagnostic Report
- 是否值得新构念：...
- 量表使用风险：
  1. ...
  2. ...
- 必补检验：
  1. ...
  2. ...
- 命名与定义修订建议：
  1. ...
- 红线检查：...

## Polished Construct & Measurement
[完整改写的英文 Construct & Measurement 部分，按段落输出]

## Key Edits
1. ...
2. ...
3. ...

## Word/Phrase Upgrades
| Original | Revised | Reason |
|----------|---------|--------|
| ...      | ...     | ...    |
```
