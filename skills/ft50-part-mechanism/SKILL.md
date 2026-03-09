---
name: ft50-part-mechanism
description: 用于评审并润色论文机制 part（假设推导、理论模型、过程解释），强制检查 micro→meso→capability/structure→macro 的完整链条，定位跳步，并输出 polished 英文改写版本。
---

# Part: Mechanism

## 目标
确保论文是"机制论文"，不是"变量相关论文"。完成诊断后，直接输出符合 FT50 标准的英文改写版本。

---

## Phase 1: 诊断评审

### 机制骨架
`Micro(主体/认知) -> Meso(行为过程) -> Capability/Structure(累积沉淀) -> Macro(结果/位置)`

### 执行步骤
1. Micro：主体、起点位置、认知内容是否具体。
2. Meso：是否有行为序列、反馈循环、关键分岔。
3. Capability/Structure：行为如何累积成能力或网络结构。
4. Macro：结果层级是否与前述机制对齐。
5. 标出跳步点：认知跳绩效、一次行为跳能力、平台标签跳成功等。

### 红线
- 全文无法讲出"谁在何时做了什么"：判非机制论文。

### 诊断输出模板
- 机制链图（文字版）：
- 跳步点清单（位置+原因）：
- 最小补强方案（3条）：
- 红线检查：通过/不通过 + 原因

---

## Phase 2: 英文润色改写

### 强制规则
1. 最终改写内容必须是英文；不输出中文句子作为正文。
2. 不改变原始机制方向与因果逻辑，只改语言表达与论证的层级清晰度。
3. 机制链的每一层（micro→meso→capability→macro）必须在文中有明确对应段落。
4. 每段保留"topic sentence → evidence/logic → implication"结构。

### Mechanism 专用句式模板
#### Micro 层（主体/认知）
- `At the individual level, [actor] perceives [stimulus], which triggers [cognitive/affective response].`
- `The process begins when [actor] encounters [uncertainty/opportunity], prompting [initial action].`

#### Meso 层（行为过程）
- `This initial response leads to [behavioral sequence], characterized by [key features: iteration, experimentation, search].`
- `Through repeated [actions], [actor] engages in [process], which involves [feedback loops/pivots].`

#### Capability/Structure 层（累积沉淀）
- `Over time, these behavioral patterns crystallize into [capability/routine/network structure].`
- `The accumulation of [actions] enables [actor] to develop [specific capability], which serves as [theoretical role].`

#### Macro 层（结果/位置）
- `Collectively, this mechanism explains how [micro trigger] translates into [macro outcome].`
- `The resulting [capability/structure] positions [actor] to achieve [performance/competitive outcome].`

#### 跳步修补
- `A critical step in this process is [missing link], without which the transition from [Level A] to [Level B] remains underspecified.`
- `We address this gap by theorizing that [intermediary mechanism] bridges [Level A] and [Level B].`

### 高频误用替换（Mechanism 场景）
- Bad: `X leads to Y.` → Better: `X triggers [micro process], which through [meso behavior] accumulates into [capability], ultimately shaping Y.`
- Bad: `The mediating effect of M.` → Better: `We theorize that M operates as the generative mechanism through which [X] shapes [Y], because [process logic].`
- Bad: `This process is important.` → Better: `This mechanism is theoretically central because it specifies how [micro actions] aggregate to produce [macro pattern].`

### 执行流程
1. 基于 Phase 1 诊断结果，确定需要补强的跳步点和层级缺口。
2. 建立术语表：统一主体名称、行为术语、能力/结构术语、结果变量。
3. 按"Micro → Meso → Capability/Structure → Macro"顺序逐段改写。
4. 先补跳步点的理论逻辑，再做句级修复和段级衔接。
5. 确保读者能清晰追踪"谁在何时做了什么"。

### 润色输出模板
1. `Polished Version`（英文，按机制层级输出完整改写）
2. `Key Edits`（英文，3-8条，说明主要改动与升级点）
3. `Word/Phrase Upgrades`（英文替换对照表）

---

## 完整输出结构

```
## Diagnostic Report
- 机制链图（文字版）：
  Micro: ... → Meso: ... → Capability/Structure: ... → Macro: ...
- 跳步点清单：
  1. [位置]: [原因]
  2. ...
- 最小补强方案：
  1. ...
  2. ...
  3. ...
- 红线检查：...

## Polished Mechanism
[完整改写的英文 Mechanism 部分，按 Micro→Meso→Capability→Macro 层级输出]

## Key Edits
1. ...
2. ...
3. ...

## Word/Phrase Upgrades
| Original | Revised | Reason |
|----------|---------|--------|
| ...      | ...     | ...    |
```
