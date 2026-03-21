---
name: ft50-part-theory-hypotheses
description: 用于评审并优化论文 Theory Framework & Hypotheses 部分，强制要求引用近5年全文期刊文献支撑每条假设，诊断假设逻辑链完整性、机制清晰度与边界条件，并输出 polished 英文改写版本。适用于公司治理、战略管理、CEO/董事会研究、组织行为等领域。当用户提交理论框架草稿、假设推导、或要求优化 hypotheses 时触发。
---

# Part: Theory Framework & Hypotheses

## 目标
将"变量关系预测"升级为"理论驱动 + 近5年文献锚定的机制假设体系"。每条假设必须：① 有明确理论来源，② 有因果机制，③ 有边界条件，④ 有近5年期刊文献引用支撑。

---

## 强制文献引用规则

**每条假设的论证段落必须包含至少1篇近5年（2020–2025）全文期刊文献引用。**

引用格式要求：
- 引用必须来自 AMJ / SMJ / ASQ / JOM / OS / JAP / AMR 等 FT50 期刊或同等级别期刊
- 引用必须是支撑机制逻辑的实质性引用，不得仅作为"prior research shows"的装饰性引用
- 每条假设至少1篇近5年文献 + 1篇经典理论文献（可超过5年）

**可直接引用的近5年文献库（基于本研究领域）：**

| 文献 | 期刊 | 年份 | 核心贡献 | 适用假设类型 |
|------|------|------|---------|------------|
| Tuggle et al. (2024) | Strategic Management Journal | 2024 | CEO通过语气/框架设置引导董事会注意力，影响决策结果 | CEO-董事会注意力、议程设置、认知影响 |
| Pan et al. (2024) | [管理学期刊] | 2024 | 女性董事 → CEO战略注意力广度 → 公司绩效；注意力广度为中介 | 董事会多样性、CEO认知广度、绩效中介 |
| Rhee (2024) | [管理学期刊] | 2024 | CEO特征（任期/职能背景/教育）→ 战略决策；董事会构成调节CEO自由裁量权 | CEO特征、战略变革、董事会调节 |
| Eklund (2021) | [公司治理期刊] | 2021 | 董事忙碌程度稀释注意力带宽，降低战略监督质量 | 董事注意力、董事会效能、认知资源 |

**经典理论文献（必须配合近5年文献使用）：**
- Ocasio (1997) AMR — 注意力基础观（ABV）核心框架
- Hambrick & Mason (1984) AMR — 高层梯队理论
- Jensen & Meckling (1976) JFE — 代理理论
- Pfeffer & Salancik (1978) — 资源依赖理论

---

## Phase 1: 诊断评审

### 执行步骤
1. **理论锚定检查**：主干理论是否真正驱动假设推导（非挂名）
2. **逻辑链检查**：`IV → 机制/过程 → DV`，标注跳步点
3. **假设质量逐条评估**：方向 + 机制 + 边界条件
4. **文献引用检查**：每条假设是否有近5年期刊文献支撑
5. **调节逻辑一致性**：调节变量是否改变了主效应的机制强度

### 红线
- 假设仅有 `X → Y` 无机制：判**弱假设**
- 假设无近5年文献引用：判**文献脱节**
- 调节假设与主效应逻辑矛盾：判**逻辑错位**
- 多理论并用无整合逻辑：判**理论拼盘**
- 中介假设无过程描述：判**黑箱中介**

### 诊断输出模板
```
- 主干理论：
- 核心机制链（IV → M → DV）：
- 假设逐条评估：
  H1: 方向[✓/✗] 机制[✓/✗] 边界[✓/✗] 近5年文献[✓/✗]
  H2: ...
- 文献引用缺口（哪些假设缺近5年文献）：
- 调节逻辑一致性：
- 红线检查：通过/不通过 + 原因
- 结构性修改建议（3-5条）：
```

---

## Phase 2: 英文润色改写

### 强制规则
1. 最终改写内容必须是英文；不输出中文句子作为正文
2. 每条假设论证段必须嵌入至少1篇近5年期刊文献引用
3. 不改变假设方向与核心机制逻辑，只改语言表达与论证严密度
4. 假设陈述用 `We hypothesize/propose that...` 引出
5. 每段结构：`理论逻辑 → 近5年文献支撑 → 假设陈述`

### 专用句式模板

#### 理论定位 + 文献锚定
- `Drawing on [theory], and consistent with [Author et al., 202X], we argue that [X] influences [Y] through [mechanism].`
- `Recent evidence suggests that [finding from 202X paper], which implies that [theoretical extension to our context].`
- `Building on [theory] and extending [Author, 202X]'s insight to [new context], we propose that...`

#### 机制推导
- `We propose that [X] influences [Y] through [mechanism M], because [micro-level logic]. This is consistent with [Author et al., 202X], who find that [relevant finding].`
- `[Theory] posits that [core assumption]. Recent work by [Author, 202X] demonstrates that [empirical support], suggesting that [implication for our hypothesis].`

#### 假设陈述
- `**Hypothesis N**: [Directional claim about X→Y relationship].`
- `We hypothesize that [X] is positively (negatively) associated with [Y] (Hypothesis N).`

#### 调节逻辑 + 文献支撑
- `We expect [moderator] to strengthen this relationship because [theoretical reasoning]. [Author et al., 202X] show that [relevant evidence], supporting the view that [moderator logic].`
- `When [moderator condition is high], [mechanism] operates more forcefully, amplifying the effect of [X] on [Y]. Consistent with this, [Author, 202X] find that...`

### 高频误用替换
| 原文（Bad） | 改写（Better） |
|------------|--------------|
| `X affects Y.` | `X influences Y through [M] (Author et al., 202X), particularly when [boundary].` |
| `Based on the above, we propose H1.` | `Drawing on [theory] and consistent with [Author, 202X], we hypothesize that [directional claim] (H1).` |
| `Prior research shows X relates to Y.` | `[Author et al., 202X] demonstrate that [specific finding], suggesting that [mechanism] links X to Y.` |
| `We use ABV as our framework.` | `Drawing on ABV (Ocasio, 1997), and consistent with Tuggle et al. (2024)'s finding that [specific result], we argue that [attention mechanism] explains why [X→Y].` |

---

## 完整输出结构

```
## Diagnostic Report
- 主干理论：
- 核心机制链：IV → M → DV
- 假设评估：
  H1: 方向✓ 机制✓ 边界✗ 近5年文献✗ → 需补[Tuggle 2024 / Pan 2024 / Eklund 2021]
  H2: ...
- 文献引用缺口：
- 红线检查：通过/不通过
- 结构性修改建议：
  1. ...

## Polished Theory Framework & Hypotheses
[完整英文改写，每条假设论证段嵌入近5年文献引用，假设用 **HN:** 加粗标注]

## Key Edits
1. ...

## Word/Phrase Upgrades
| Original | Revised | Reason |
|----------|---------|--------|
```
