---
name: ft50-part-methods-results
description: 用于评审并润色 Methods、Results 与 Robustness 部分，校验研究设计是否支撑理论命题（测量一致性、层级匹配、因果识别），检查结果解释是否回扣机制，设计完整稳健性方案，并输出 polished 英文改写版本。基于 AMJ/SMJ/OrgSci/JBR 等顶刊实证论文写作范式。
---

# Part: Methods, Results & Robustness Analysis

## 目标
让方法服务理论，结果讲述故事，稳健性体系化消除疑虑。完成诊断后，直接输出符合 FT50 标准的英文改写版本。

---

## Phase 1: 诊断评审

### Data & Sample 检查
1. 是否清楚说明了 empirical setting 及其理论适配性（为什么选择这个情境来检验理论）。
2. 数据来源是否逐一列出（每个数据库/来源单独说明提供了什么类型的数据）。
3. 样本构建过程是否透明（初始样本 → 筛选条件 → 缺失/合并导致的样本缩减 → 最终样本量）。
4. 时间跨度是否明确（起止年份 + 为什么选择这个时间段）。
5. 观测单位是否明确（firm-year / CEO-quarter / individual-level 等）。
6. 是否处理了样本选择偏差（survivorship bias / sample-inclusion bias 检验）。

### Variable Measurement 检查
1. **每个变量**是否包含完整的测量信息链：
   - 构念名称 → 概念定义 → 操作化方式 → 数据来源 → 支撑文献（citation）→ 计算公式（如有）
2. 核心自变量/因变量的测量**必须有参考文献支撑**（`following [citation]` 或 `adapted from [citation]`）。
3. 新构念或非标准测量是否提供了 construct validity 证据（专家评分、CFA、收敛/区分效度等）。
4. 反映式与形成式测量是否正确区分。
5. 控制变量是否每一个都给出了**理论纳入理由**（为什么要控制这个变量）和**操作化方式**。

### Methods 检查（设计与模型）
1. 识别策略处理内生性（FE/IV/匹配/滞后/CFA/DID/RDD 等）。
2. 模型与机制一致（避免只跑净效应，须体现中介/调节链条）。
3. 估计方法的选择是否有统计依据（如 Hausman test 决定 FE vs RE）。

### Results 检查
1. 结果是否按理论命题顺序报告（base model → main effects → interactions → full model）。
2. 是否先解释实质性发现（substantive finding），再报统计数字。
3. 交互效应是否做了 simple slope test 或 marginal effect 分析。
4. 异质性/边界结果是否真正对应理论边界。
5. 中介分析是否采用了当前推荐方法（bootstrapping、Monte Carlo）。

### Robustness 检查
1. 是否有内生性纠正（至少一种：2SLS/CFA/PSM/Heckman/反向因果检验）。
2. 是否有替代测量检验（核心自变量和因变量各至少一种替代测量）。
3. 是否有替代模型规格检验（FE vs RE、不同滞后期、不同聚类标准误）。
4. 可选加分项：伪造检验（falsification test）、遗漏变量偏差检验（ITCV）、子样本分析。

### 红线
- 数据来源不明或无法复现样本构建过程：判"数据透明度不足"。
- 核心变量（DV/IV）的测量缺少参考文献支撑：判"测量缺乏依据"。
- 控制变量无理论纳入理由（纯罗列无解释）：判"控制变量论证不足"。
- 结果能显著但无法解释机制：判"统计成立，理论不足"。
- 因果语言但无因果识别策略：判"语言越界"。
- 稳健性仅有一种且未覆盖内生性：判"稳健性不足"。

### 诊断输出模板
- Data & Sample 评估：
  - 情境适配性说明：✓/✗
  - 数据来源逐一列出：✓/✗
  - 样本构建过程透明度：✓/✗（是否展示了从初始样本到最终样本的缩减路径）
  - 时间跨度与理由：✓/✗
  - 观测单位明确性：✓/✗
  - 选择偏差处理：✓/✗/不需要
- Variable Measurement 评估：
  - 各变量信息链完整性检查（✓ = 完整；✗ = 缺失要素）：
    - DV：构念名 / 操作化 / 数据来源 / citation / 公式 / 选择理由
    - IV：构念名 / 操作化 / 数据来源 / citation / 公式 / validity 证据（若新构念）
    - Moderators：操作化 / 数据来源 / citation / 编码规则
    - Mediators：操作化 / 数据来源 / citation
    - Controls：纳入理由 / 操作化 / citation（逐一检查）
  - 缺失 citation 的变量清单：
  - 需补充 validity 证据的变量清单：
- 设计风险清单：
- 结果解释缺口：
- 稳健性体系评估（✓已覆盖 / ✗缺失）：
  - 内生性纠正：
  - 替代测量：
  - 替代模型规格：
  - 反向因果：
  - 子样本/边界：
- 红线检查：通过/不通过 + 原因

---

## Phase 2: 英文润色改写

### 强制规则
1. 最终改写内容必须是英文；不输出中文句子作为正文。
2. **绝对不改变**原始实证结果、变量关系方向、效应符号、统计显著性和核心识别策略。
3. 只改语言表达、结构组织和结果解释的清晰度。
4. 结果报告必须先写实质性发现（substantive finding），再写统计数字。
5. 稳健性分析必须完整撰写，不能仅以一两句话带过。

---

### Methods 专用句式模板

#### A. 研究设计概述（Design Summary）
- `We test our arguments using [design] based on [sample/context].`
- `Our empirical setting is [context], which is appropriate because [theoretical advantage for identification].`
- `We empirically test [theory/model] using longitudinal data from [N] [units] (SIC code [X]) between [start year] and [end year].`
- `To test the hypotheses outlined above, the key challenge is to [methodological challenge], which we address by [approach].`

#### B. Data and Sample（数据与样本）

> **写作要求**：Data & Sample 是 Methods 的第一个完整小节，必须让读者清楚了解"数据从哪来、样本怎么构建、最终分析的是什么"。顶刊通常用 1–2 页篇幅，结构如下：

##### B-1. Empirical Setting 与理论适配性（1–2 句）
说明为什么选择这个情境来检验理论，而不是简单罗列数据。
- `Our empirical setting is [context]. This setting is particularly suitable for testing our theory because [theoretical advantage: e.g., natural variation in IV, clean identification, relevant boundary conditions].`
- `We focus on [industry/context] because it provides [theoretical advantage for identification, e.g., sufficient variation in key constructs, regulatory shock, natural experiment].`
- `We chose [context] as our empirical setting for [N] reasons. First, [reason 1]. Second, [reason 2].`

##### B-2. 数据来源逐一列出（每个数据库单独说明提供了什么数据）
- `We collected data from multiple sources. First, we obtained [data type, e.g., financial data] from [database, e.g., COMPUSTAT]. Second, we collected [data type, e.g., CEO and board characteristics] from [database, e.g., EXECUCOMP / BOARDEX]. Third, [data type] from [database]. Finally, [data type] from [database].`
- `We supplement the [primary data] with data from a variety of databases such as [database list].`
- `[Specific variable] data was obtained from the [specific database], which provides [what the database covers].`

##### B-3. 样本构建过程（必须透明，展示从初始到最终的缩减路径）
- `Our initial sample frame consists of all [population, e.g., S&P 1500 firms / Fortune 500 companies] between [start year] and [end year].`
- `We began with [N] firms from [source]. We then excluded [N] firms due to [reason 1, e.g., missing financial data], [N] firms due to [reason 2, e.g., industry restrictions], and [N] firms due to [reason 3, e.g., incomplete board data].`
- `Events such as mergers, delisting, and missing data resulted in some firms not having complete data, yielding an unbalanced panel of [N] firm-year observations.`
- `The final sample contains [N] [unit]-[time] observations (e.g., firm-year / CEO-quarter) relating to [N] unique [units] across [N] industries.`
- `To choose firms randomly, we used a random-number generator to assign a random value to each remaining firm, choosing the [N] highest values for inclusion (Eklund & Mannor, 2021).`

##### B-4. 时间跨度说明
- `Our sample covers the period from [start year] to [end year]. We chose this time frame because [reason, e.g., data availability, regulatory change, theoretical relevance].`
- `The independent variables are measured at year t−1, with dependent variables measured at year t, to establish temporal precedence.`

##### B-5. 样本选择偏差处理（如有需要）
- `We tested for sample-inclusion bias by comparing the characteristics of the included and excluded firms using the Kolmogorov-Smirnov two-sample test. Across all archival variables, the results showed no statistically significant difference (Rhee, 2024).`
- `To address potential survivorship bias, we include all firms that appear in the sample at any point during our observation window, regardless of whether they exit during the period.`

#### C. Variable Measurement（变量测量）

> **核心写作规范——每个变量必须包含以下信息链**：
> 1. **构念名称**（Construct name）
> 2. **操作化方式**（How it is measured / calculated）
> 3. **数据来源**（Which database / source provides the raw data）
> 4. **支撑文献**（Citation justifying this measurement approach）——**强制要求，不可省略**
> 5. **计算公式或编码规则**（If applicable: formula, coding scheme, scale items）
> 6. **Construct validity 证据**（仅新构念/非标准测量需要：CFA、专家评分、收敛效度等）
>
> **详细程度分级**：
> - **因变量 (DV)**：最详细——需完整说明操作化 + 数据来源 + citation + 为什么选择该测量 + 公式
> - **核心自变量 (IV)**：与 DV 同等详细——如果是新测量，还需附 construct validity 证据
> - **调节变量 (Moderators)**：中等详细——操作化 + 数据来源 + citation + 编码规则
> - **中介变量 (Mediators)**：中等详细——操作化 + 数据来源 + citation + 数据获取挑战说明（如有）
> - **控制变量 (Controls)**：简洁但完整——每个变量须给出（1）纳入理由（为什么要控制）+（2）操作化方式 + （3）citation，可以按层级分组批量介绍

##### C-1. 因变量（Dependent Variable）
- `We measure the dependent variable, [DV name], based on [specific operationalization] using data from [source]. This measure is widely used in prior research (e.g., [citation A]; [citation B]) and captures [what the variable reflects].`
- `Following prior research (e.g., [citation]), we operationalize [DV] as [specific formula/measure]. We chose this measure because [reason: e.g., it captures both short-term and long-term performance implications / it is less susceptible to manipulation than accounting measures].`
- `[DV] was computed as [formula], where [define each component]. Data was obtained from [database].`

##### C-2. 核心自变量（Independent Variable）
- `We measure [IV name] following the approach developed by [citation]. Specifically, [IV] is calculated as [specific operationalization / formula], using data from [source].`
- `We calculated our independent variable, [IV], by following the [citation] method for [approach]. This measure captures [conceptual definition in one sentence].`
- `[Construct] was operationalized as [measure], following [citation]. Higher values indicate [interpretation].`

###### 文本分析类变量的构建（Text-Based Measures）——需要额外 validation
- `To develop [measure], we follow the general approach to computer-aided text analysis described by [citation, e.g., Short et al., 2010; McKenny et al., 2018].`
- `We take both deductive and inductive approaches to generate the list of keywords indicating [construct]. The deductive approach draws on [source A, e.g., established dictionaries / prior theoretical work]. The inductive approach involves [process, e.g., manual reading of a random subset of transcripts to identify additional keywords].`
- `The final dictionary contains [N] words/phrases across [N] categories. The complete list of keywords is provided in the Appendix.`
- `To validate the keyword measure, we recruited [N] [experts, e.g., management scholars / industry professionals / doctoral students] who independently rated [N] [units, e.g., transcripts / letters]. We found a significantly high correlation between the keyword-based measures and manual ratings (r = [value]; p < [value]), providing empirical support for the validity of our measure (following [citation]).`
- `We also conduct a [sentiment analysis / topic modeling analysis] to rule out the possibility that [construct] merely reflects [alternative explanation, e.g., positive tone rather than genuine strategic attention].`

###### 残差法构建变量（Residual-Based Measures）
- `Following previous research ([citation]), we operationalized [construct, e.g., CEO overpayment] by taking the residuals from a regression of [outcome, e.g., CEO total compensation] on [determinants: e.g., firm size, performance, CEO tenure, industry dummies]. Positive residuals represent [interpretation, e.g., overpayment] (Pan et al., 2025; Seo et al., 2015).`

###### 指数/复合变量构建（Index / Composite Measures）
- `Because we have multiple constructs reflecting [concept], we followed the approach of [citation] and created an index variable. We first used principal component analysis (PCA) and obtained [N] factor(s) with eigenvalue greater than one. We then recast the data along the first principal component axis to obtain the [index name] (Pan et al., 2025).`
- `We calculated our independent variable by following the [citation] method, assigning each [unit] an aggregate score based on the following [N] indicators: (1) [indicator], (2) [indicator], (3) [indicator], and (4) [indicator] (Tuggle et al., 2024).`

##### C-3. 调节变量（Moderating Variables）
- `To assess [moderator concept] for testing Hypothesis [n], we employ [operationalization], following [citation].`
- `[Moderator] was measured as [operationalization] using data from [source] ([citation]). Higher values indicate [interpretation].`
- `[Moderator] was measured dichotomously: [units] with [condition] were coded as 1, and [units] without as 0, following [citation].`
- `We specify [moderator] as the linear combination of [component A] and [component B], consistent with [citation].`

##### C-4. 中介变量（Mediating Variables）
- `To test [mediation hypothesis], we measure [mediator name] as [operationalization], following [citation]. Data was obtained from [source].`
- `Because collecting [mediator data, e.g., CEO cognitive measures] in a longitudinal, cross-sectional research design is challenging, we turn to [data source, e.g., earnings conference call transcripts / annual reports], following recent studies (e.g., [citation A]; [citation B]).`

##### C-5. 控制变量（Control Variables）

> **写作规范**：每个控制变量必须满足三要素——（1）为什么控制（理论理由）+（2）如何测量 +（3）参考文献。可以按层级分组（firm → CEO → board → industry）提高可读性。

- `We include control variables to rule out factors whose effects on [DV] might be confounded with those of our focal variables.`

**Firm-level controls**:
- `We controlled for firm size, measured as the natural logarithm of [total assets / number of employees], because larger firms may have [reason] ([citation]).`
- `Firm performance was controlled for using return on assets (ROA), calculated as net income divided by total assets ([citation]), as [theoretical reason].`
- `We also controlled for firm age, firm slack (operationalized as the debt-to-equity ratio; [citation]), and firm diversification (Herfindahl index of segment sales; [citation]).`

**CEO/Executive-level controls**:
- `We controlled for CEO duality (coded as 1 if the CEO also serves as board chair, 0 otherwise) because [theoretical reason] ([citation]).`
- `CEO tenure was included as a control, measured as the number of years since the CEO's appointment, following [citation].`

**Board-level controls**:
- `We controlled for board size ([citation]) and board independence, measured as the proportion of independent directors ([citation]).`

**Industry/environment-level controls**:
- `To account for the influence of the industry environment, we controlled for industry dynamism ([operationalization]; [citation]), industry munificence ([operationalization]; [citation]), and industry concentration (Herfindahl index; [citation]) at the [N]-digit SIC level.`

**Fixed effects**:
- `Finally, we included [year / industry / firm] fixed effects to capture unobservable [time / industry / firm]-level heterogeneity.`

#### H. 估计方法与内生性处理（Estimation and Endogeneity）
- `To test our hypotheses, we used a [fixed-effect/random-effect/OLS] regression model to capture unobservable [firm/individual] heterogeneities.`
- `A Hausman test yielded a statistically significant result, which suggests that the use of fixed effects was more appropriate than a random-effects specification.`
- `Standard errors are clustered at the [firm/industry] level to account for non-independence of errors (Petersen, 2009).`
- `To reduce the threat of multicollinearity, we mean-centered the key continuous predicting variables. We obtained the variance inflation factors for all variables, and none was above [threshold], indicating that multicollinearity is unlikely to threaten our results.`

##### 内生性纠正方法
- **Control Function Approach (CFA)**:
  - `We followed recent studies (e.g., [citation]) and used a control function approach to test for any endogeneity bias. Like an instrumental variable approach, CFA relies on an instrument that is theoretically unrelated to the dependent variable but significantly predicts the endogenous variable. However, it is more efficient than the traditional IV approach for testing higher-order variables, such as non-linear or interactive effects.`
  - `We used the industry average value of [endogenous variable], excluding the focal firm's value, as an instrument, as the industry average indicates an industry trend that will not affect a particular firm's [DV] but will likely influence [endogenous variable].`

- **Two-Stage Least Squares (2SLS)**:
  - `To mitigate potential endogeneity concerns, we tested the hypothesized relationships using two-stage least squares models.`
  - `In the first stage, we used [instrument variables] to compute the predicted value for [endogenous variable]; in the second stage, we used the predicted value in the regression analyses.`
  - `We performed two postestimation tests: (1) an F-test to rule out weak instruments (F = [value]; p < [value]), and (2) Sargan's χ² test for overidentifying restrictions (χ² = [value], p = [value]), confirming instrument validity.`

- **Propensity Score Matching (PSM)**:
  - `We implement a propensity score matching analysis to identify the net effect of [IV] on [DV] by comparing only nearly identical [units] with high versus low levels of [IV].`
  - `We conduct 1:1 matching without replacement with a caliper radius of [value], ensuring that we only match firms with a propensity score difference less than [value].`

- **Heckman Selection**:
  - `To address potential selection bias, we employed a Heckman two-stage procedure. In the first stage, we estimated a probit selection model. We then computed the inverse Mills ratio and included it in the main model.`

- **反向因果检验**:
  - `To address the possibility of reverse causality, we conduct an analysis with [IV] in year t as a dependent variable and [DV] in year t−1 as an independent variable. We find no significant relationship, suggesting that [DV] in previous years does not predict [IV] in subsequent years.`

---

### Results 专用句式模板

#### A. 描述性统计（Descriptive Statistics）
- `Table [n] provides descriptive statistics and bivariate correlations among the variables.`
- `All variables used to construct interaction terms were centered prior to calculating interaction terms.`
- `To test for the presence of multicollinearity, we followed procedures outlined by [citation]. The largest variance inflation factor was [value], well below the commonly accepted threshold of 10, indicating multicollinearity is not an issue.`

#### B. 主效应报告（Main Effects）—渐进式模型报告
- `Table [n] presents the results of our analyses. Models [a–b] include only the control variables. Models [c–d] progressively display the results of the hypotheses tests.`
- `Model [n] reports our base regression model, containing only control variables. Model [n+1] adds our independent variable, [IV].`
- `Hypothesis [n] proposes that [IV] is [positively/negatively] associated with [DV]. [Model reference] shows that [IV] is [positively/negatively] related to [DV] (β = [value], p < [value]). This result indicates that [substantive interpretation]. Therefore, Hypothesis [n] is supported.`
- `The results suggest a [positive/negative] relationship between [IV] and [DV] ([coefficient value], p < [value]). Thus, Hypothesis [n] is [strongly] supported.`

##### 实质性解释（Substantive Interpretation）
- `These results demonstrate that compared to a [unit] with [IV] of 1 SD below the mean, a [unit] with [IV] of 1 SD above the mean will experience a [X]% [greater/lower] [outcome].`
- `Translating into practical implications, one standard deviation increase in [IV] is associated with a [specific dollar/percentage change] in [DV].`

#### C. 交互效应报告（Interaction Effects）
- `Hypothesis [n] proposes that [moderator] [amplifies/mitigates] the [positive/negative] association between [IV] and [DV]. [Model reference] shows that the [two-way/three-way] interaction of [variables] is [positively/negatively] related to [DV] (β = [value], p < [value]).`
- `This result indicates that the [relationship/effect] of [IV] on [DV] is [stronger/weaker] when [moderator condition].`
- `We plot this result in Figure [n]. As the figure shows, [description of interaction pattern].`
- `A simple slope test supports our hypothesis: [IV] is [positively/negatively] associated with [DV] when [moderator is high] (b = [value], p < [value]) but [not significant / weaker] when [moderator is low] (b = [value], p = [value]).`

##### 三元交互效应
- `The three-way interaction of [X], [M1], and [M2] is [positively/negatively] related to [DV] (β = [value], p < [value]). This result indicates that the two-way interaction of [X] and [M1] is [weakened/strengthened] when [M2 condition].`

#### D. 中介效应报告（Mediation Effects）
- `To test the mediating effect, we adopted the [method name] approach outlined by [citation].`
- `Using [N] bootstrapped samples, we find the direct effect of [IV] on [DV] positive and significant (b = [value], SE = [value], p = [value], 95% bias-corrected CI = [lower, upper]).`
- `Its indirect effect through [mediator] is also positive and significant (b = [value], SE = [value], p = [value], 95% CI = [lower, upper]).`
- `The absence of zero within the confidence interval confirms the mediation effect.`
- `When controlling for [mediator], the coefficient for [IV] is reduced from [value] to [value], suggesting [mediator] as a partial mediator.`

#### E. 控制变量结果简要提及
- `Of the control variables, the results show that [variable] significantly predicts [DV] (β = [value], p < [value]).`
- `The other control variables show no statistically significant effect on [DV].`

---

### Robustness Analysis 专用句式模板（关键增补）

#### 总体框架
稳健性分析应按体系化方式组织，覆盖以下维度（至少3个）：

##### 维度一：内生性纠正（Endogeneity Correction）
（见 Methods 中的识别策略，此处报告结果）
- `To address potential endogeneity, we [employed strategy]. The results, summarized in [Model/Table reference], were consistent with the original findings.`
- `As a further check, we [alternative endogeneity approach]. Our conclusions remain unchanged.`

##### 维度二：替代测量（Alternative Measures）
- `In the main analysis, we used [measure A] to operationalize [construct]. As an alternative, we used [measure B], following [citation]. [Model/Table reference] shows that our results were not sensitive to this alternative measure, confirming the robustness of our findings.`
- `We also considered alternative operationalizations of [DV/IV]. Specifically, we replaced [original measure] with [alternative measure]. The results did not differ substantively.`

##### 维度三：替代模型规格（Alternative Specifications）
- `Although we used [model type] as our main analyses, we also leveraged the advantages of [alternative model] to check the robustness of our findings. The results remain consistent with the [original model] results.`
- `As a robustness test, [alternative lag/clustering/estimation approach] are also examined. We obtained results similar to the main results.`
- `We also tested our models using [quantile regression / GEE / multilevel modeling]. Our findings remain robust.`

##### 维度四：反向因果/时间结构（Reverse Causality / Temporal Structure）
- `To rule out the possibility of reverse causality, we conducted an analysis with [IV] at time t as a dependent variable and [DV] at time t−1 as an independent variable, together with the full set of controls. We find no significant relationship, alleviating reverse causality concerns.`
- `We consider alternative temporal gaps by lagging [n] years to observe how [IV] in year t−[n] is associated with [DV] in year t. Our findings remain robust.`

##### 维度五：伪造检验（Falsification Tests）
- `As a falsification test, we examine the impact of [IV] on [outcome that should NOT be affected]. We find [IV] has no main effect on [unrelated outcome], strengthening the argument that [IV] specifically affects [theorized DV] rather than [alternative mechanism].`
- `These non-findings confirm that what drives our main results is [theorized mechanism] rather than [alternative explanation].`

##### 维度六：子样本/边界分析（Subsample / Boundary Analyses）
- `Subsample analyses reveal that the relationship holds for [group A] but not [group B], suggesting [theoretical interpretation].`
- `To ensure our results are not driven by [specific subset], we re-estimated the model after excluding [subset]. The results remain substantively unchanged.`
- `We explored whether the effect changes across [time periods / contexts / subgroups]. Our data indicates that [pattern].`

##### 维度七：遗漏变量偏差（Omitted Variable Bias Tests）
- `We conducted an ITCV test to explore whether our results suffer from omitted variable bias (Busenbark et al., 2022). The results indicate that an omitted variable would need to overturn the relationship in [X]% of cases to bias our results. The partial correlations of all included controls are below this threshold, alleviating concerns about omitted variable bias.`

##### 维度八：Construct Validity 检验
- `To validate [measure], we recruited [N] [experts] who independently rated [N] [units]. We found a significantly high correlation between the [automated/keyword] measures and manual ratings (r = [value]; p < [value]), providing empirical support for the validity of [measure].`
- `We also conducted a [sentiment analysis / topic modeling analysis] to rule out the concern that [alternative explanation]. Our analysis reveals [finding that rules out the concern].`

#### 稳健性分析报告总结句
- `Taken together, these robustness checks corroborate our main findings and provide confidence that the results are not artifacts of specific modeling choices or measurement decisions.`
- `Across all robustness checks, our core findings remain qualitatively and quantitatively consistent, supporting the theoretical arguments developed in this study.`

---

### Supplementary / Additional / Post-Hoc Analyses 句式模板

这类分析用于扩展理论理解，超出假设检验范围但为论文增添深度：

- `In supplementary analyses, we also provide new insights into [additional theoretical implication].`
- `Although we did not hypothesize [indirect moderation / additional effect], our theoretical model implies it may exist. To test this, we explored [analysis].`
- `We also explored whether [additional pattern]. Our data indicates that [finding], providing evidence that [theoretical interpretation].`
- `In a post-hoc analysis, we find that when [condition], the [effect] on [DV] [pattern], highlighting [theoretical insight].`

---

### 高频误用替换（Methods, Results & Robustness 场景）

| Bad | Better | Reason |
|-----|--------|--------|
| `We collected data from COMPUSTAT.` | `We obtained financial data (e.g., total assets, ROA) from the COMPUSTAT database. CEO and board characteristics were collected from EXECUCOMP and BOARDEX, respectively.` | 单一来源 → 逐一列出 |
| `Our sample is 500 firms.` | `Our initial sample frame consists of all S&P 1500 firms between 2010 and 2020. After excluding firms with missing financial data (N = X) and incomplete board records (N = Y), our final sample contains Z firm-year observations relating to W unique firms.` | 无过程 → 完整构建路径 |
| `We measure CEO power.` | `Following [citation], we operationalize CEO power as [specific measure], calculated as [formula/coding], using data from [source].` | 缺 citation + 操作化 + 来源 |
| `We control for firm size and age.` | `We controlled for firm size (natural logarithm of total assets; [citation]) because larger firms may have [reason]. Firm age was included because [reason], measured as [operationalization] ([citation]).` | 无理由无来源 → 三要素齐全 |
| `We used a questionnaire and did analysis.` | `We collected survey data and estimated [model], controlling for [key covariates].` | 模糊 → 精确 |
| `H1 is significant.` | `Results support H1: [substantive finding] (β = ..., p < ...).` | 统计优先 → 实质优先 |
| `See Table 2.` | `As shown in Table 2, [main substantive pattern].` | 空指向 → 内容引导 |
| `Our results confirm the theory.` | `Our results are consistent with the theory.` | 过度宣称 → 校准 |
| `X proves that Y causes Z.` | `X provides evidence that Y may causally affect Z.` | 因果越界 → 谨慎因果 |
| `The result is robust.` | `The effect is substantively unchanged when we [alternative specification].` | 空洞 → 具体 |
| `We controlled for many variables.` | `We include control variables to rule out factors whose effects on [DV] might be confounded with those of our covariates.` | 模糊 → 目的导向 |
| `We used instrumental variables.` | `We instrument [endogenous variable] with [instrument], which satisfies the exclusion restriction because [reason].` | 缺乏论证 → 完整论证 |
| `We did a robustness check.` | `To address potential endogeneity concerns, we employed [specific strategy]. The results, presented in [Table], are consistent with our main findings.` | 笼统 → 具体策略 |
| `The robustness checks confirm our findings.` | `Across all robustness checks, our core findings remain qualitatively and quantitatively consistent.` | 简单 → 系统性总结 |
| `We tested for endogeneity.` | `Endogeneity may potentially bias our results, as [specific threat]. To address this issue, we [strategy] (e.g., [citation]).` | 无动机 → 明确威胁 + 对策 |
| `Results are significant at the 5% level.` | `[Substantive finding in words] (β = [value], p < 0.05).` | 数字优先 → 含义优先 |
| `The interaction is significant.` | `The interaction term [X × M] is [positive/negative] and significant (b = [value], p < [value]). A simple slope test reveals that [interpretation].` | 不完整 → 含 slope test |
| `We did mediation analysis.` | `Using [N] bootstrapped samples, we find the indirect effect through [mediator] is significant (b = [value], 95% CI = [lower, upper]).` | 笼统 → 方法+结果 |

### Claim 强度校准
- 描述性证据：`shows`, `indicates`, `documents`
- 相关性推断：`is associated with`, `is linked to`, `correlates with`
- 机制一致推断：`is consistent with the mechanism that`, `suggests that [M] may explain`
- 因果语言（仅强设计：IV/RDD/DID）：`increases`, `reduces`, `causally affects`
- 有限因果：`may influence`, `appears to affect`, `is consistent with a causal interpretation`

---

### 执行流程

1. **诊断**：基于 Phase 1 诊断结果，确定 Methods 中的设计描述缺口、Results 中的解释缺口、Robustness 中的覆盖缺口。
2. **术语表**：统一变量名、方法名、统计表达。
3. **Methods 改写**：按以下顺序组织——
   - **Design overview**: 研究设计概述 + empirical setting 的理论适配性
   - **Data and Sample**: 数据来源逐一列出 → 样本构建过程（初始 → 筛选 → 最终 N）→ 时间跨度 → 观测单位 → 选择偏差处理
   - **Dependent variable**: 构念名 + 操作化 + 数据来源 + citation + 公式 + 选择理由
   - **Independent variable(s)**: 同 DV 详细程度 + construct validation（若新构念）
   - **Moderating variables**: 操作化 + 数据来源 + citation + 编码规则
   - **Mediating variables**: 操作化 + 数据来源 + citation + 数据获取挑战说明
   - **Control variables**: 按层级分组（firm → CEO → board → industry），每个变量给出（1）纳入理由 +（2）操作化 +（3）citation
   - **Estimation approach**: 模型选择 + 统计依据（如 Hausman test）+ 标准误聚类方式
   - **Endogeneity strategy**: 具体识别策略 + 工具变量选择与排他性论证
   - **Model specification**: 写出完整模型公式（如有必要）
4. **Results 改写**：按理论命题顺序改写——
   - Descriptive statistics & correlations
   - 渐进式模型呈现（controls-only → main effects → interactions → full model）
   - 每条假设：先说实质发现 → 再报系数与显著性 → 判定结果
   - 交互效应附 simple slope test / marginal effect
   - 中介效应用 bootstrapping CI 报告
5. **Robustness 改写**：按体系化维度组织——
   - Endogeneity correction (结果报告)
   - Alternative measures
   - Alternative model specifications
   - Reverse causality / temporal robustness
   - Falsification tests (if applicable)
   - Subsample / boundary analyses
   - Omitted variable bias tests (if applicable)
   - 总结句
6. **Supplementary Analyses**（可选）：Post-hoc 发现、理论延伸分析。
7. **Claim 强度校准**：确保语言与识别策略匹配（相关设计不用因果语言）。

---

### 润色输出模板

1. `Polished Version`（英文，Methods、Results、Robustness 三部分分别输出）
2. `Key Edits`（英文，5-12条，说明主要改动与升级点）
3. `Word/Phrase Upgrades`（英文替换对照表）

---

## 完整输出结构

```
## Diagnostic Report
- Data & Sample 评估：
  - 情境适配性：✓/✗
  - 数据来源逐一列出：✓/✗
  - 样本构建透明度：✓/✗
  - 观测单位明确性：✓/✗
- Variable Measurement 评估：
  - DV 信息链：✓/✗ [缺失要素]
  - IV 信息链：✓/✗ [缺失要素]
  - 缺失 citation 的变量：[列出]
  - 需补充 validity 的变量：[列出]
- 设计风险清单：
  1. ...
  2. ...
- 结果解释缺口：
  1. ...
- 稳健性体系评估：
  - 内生性纠正：✓/✗ [具体方法]
  - 替代测量：✓/✗ [具体方法]
  - 替代模型规格：✓/✗ [具体方法]
  - 反向因果：✓/✗
  - 伪造检验：✓/✗
  - 子样本/边界：✓/✗
  - 遗漏变量偏差：✓/✗
- 必做稳健性建议（按优先级排序）：
  1. ...
  2. ...
  3. ...
- 红线检查：通过/不通过 + 原因

## Polished Methods
[完整改写的英文 Methods 部分]

## Polished Results
[完整改写的英文 Results 部分，按假设顺序输出，含渐进式模型报告]

## Polished Robustness Analysis
[完整改写的英文稳健性分析部分，按维度体系化组织]

## Supplementary Analyses (if applicable)
[Post-hoc 分析或理论延伸发现]

## Key Edits
1. ...
2. ...
...

## Word/Phrase Upgrades
| Original | Revised | Reason |
|----------|---------|--------|
| ...      | ...     | ...    |
```
