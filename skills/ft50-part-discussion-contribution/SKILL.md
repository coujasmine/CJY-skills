---
name: ft50-part-discussion-contribution
description: 用于统筹论文 Discussion、Limitations/Future Research 与 Conclusion 的整体润色与重写；当用户提交完整讨论部分时，默认联动改写三个子部分，并确保三者使用同一个理论口径与核心命题。
---

# Part: Discussion, Limitations, and Conclusion Orchestrator

## 目标
当用户给的是完整的 Discussion/Conclusion 部分时，默认把 `Discussion + Limitations/Future Research + Conclusion` 当作一个连续收束链整体改写，而不是拆成三个彼此独立的小任务。

这个 skill 的主要职责不是简单分发，而是先统一主命题，再约束三个子部分围绕同一个理论口径、同一个 claims 边界、同一个语气轨迹展开。

## 使用原则
1. 用户提交完整讨论部分时，默认优先调用本 skill。
2. 即使用户只强调其中一个子部分，本 skill 也优先检查三部分是否需要联动调整。
3. 若用户没有特别说明，默认认为三个部分应该联动重写。

## skill 的角色
这个 skill 是“总导演”，不是“路由器”。

它必须先做三件事：
1. 提炼全文唯一的 `core proposition`
2. 规定三个子部分各自承担什么功能
3. 检查三部分是否在同一理论口径下连续收束

## 三个子部分的分工
- `Discussion`
  - 负责展开：回答研究问题、解释结果、重写 literature conversation、提出 practical implications。
- `Limitations and Future Research`
  - 负责收边界：限定 strongest claim 的适用范围，指出当前不能再往前走到哪里。
- `Conclusion`
  - 负责定调：把全文压回一个更高层次、更稳的 proposition，并完成最后收束。

## 跨段一致性规则
以下规则是本 skill 的核心。只要用户给的是完整部分，就必须检查并修正。

### 1. One Proposition Rule
Discussion、Limitations、Conclusion 必须服务于同一个 `core proposition`。

禁止出现：
- Discussion 说的是 mechanism A
- Limitations 改成在谈 measurement B
- Conclusion 最后升华到完全不同的理论主张 C

先写出一句：
- `Core proposition: [一句话写清全文最终主命题]`

后续三个部分都必须围绕这句话服务。

### 2. Same Conversation Rule
Discussion 中对话的核心 literatures，Conclusion 必须延续同一套理论口径。

禁止：
- Discussion 用 attention-based view
- Conclusion 突然换成 broad corporate governance slogan

Conclusion 可以升层级，但不能换频道。

### 3. Claim Discipline Rule
Discussion 提出的 strongest claim，Limitations 只能限定其边界，不能把它改写成另一种更弱、更模糊、甚至不同类型的 claim。

正确关系：
- Discussion: `what we can claim`
- Limitations: `how far that claim travels`
- Conclusion: `why that claim matters`

错误关系：
- Discussion 说因果逻辑
- Limitations 改口成只是相关性描述
- Conclusion 又回到强因果口吻

### 4. Tone Descent Rule
三个部分的语气必须连续下降，而不是跳跃：
- Discussion：展开、解释、对话
- Limitations：收边界、降噪音、控主张
- Conclusion：压缩、提炼、定调

也就是说，行文应从“展开解释”逐步过渡到“边界限定”，最后进入“高度压缩的最终命题”。

### 5. No New Logic Late Rule
Limitations 和 Conclusion 不得引入 Discussion 中没有建立的新机制、新理论主张或新对话对象。

可以做的：
- 缩短
- 提炼
- 限定
- 升层级

不能做的：
- 新增一个 Discussion 从未铺垫的 mediator
- 突然换一个理论 stream
- 最后一段凭空上升到全新规范命题

### 6. Last-Paragraph Echo Rule
Conclusion 必须是对 Discussion 开头的 echo，而不是另起一段。

要求：
- Discussion 开头给 `study-level answer`
- Conclusion 最后一段回到这句 answer
- 但用更高层、更短、更稳的方式说出来

理想关系：
- Opening: `This study shows that ...`
- Ending: `Taken together, this suggests that ...`

### 7. Practical-Boundary Alignment Rule
如果 Discussion 给了 management/governance implications，Limitations 不能把边界写得与这些实践建议直接冲突。

例如：
- 若实践启示只适用于大型上市公司
- Limitations 就要明确这一点
- Conclusion 也不能写成对所有组织都成立的口号

## 联动改写顺序
完整部分必须按以下顺序处理：

1. `Extract the core proposition`
   - 用一句话写出全文最终主命题。

2. `Rewrite Discussion first`
   - 先把 Discussion 主体改到位：
   - study-level answer
   - conversation-based contributions
   - practical implications

3. `Rewrite Limitations second`
   - 不另起炉灶，只对 Discussion 的 strongest claim 做边界限定。

4. `Rewrite Conclusion last`
   - 用与 Discussion 同一理论口径完成压缩收束。

5. `Run cross-part consistency check`
   - 检查 proposition 是否一致
   - 检查 literatures 是否一致
   - 检查 claim strength 是否前后一致
   - 检查 practical implications 与边界是否冲突
   - 检查 conclusion 是否是 echo 而不是新起点

## 改写时必须先写出的 3 个锚点
在开始联动改写前，先在内部明确以下三句：

1. `Core proposition`
   - 这篇论文最后到底要让读者带走什么命题？

2. `Strongest defensible claim`
   - 基于当前设计，最强但仍站得住脚的主张是什么？

3. `Broader significance`
   - 这个命题为什么对更大的理论或管理问题重要？

如果这三句写不清，说明三个部分还不能开始联动改写。

## 常见失配信号
- Discussion 很强，Limitations 把自己写垮了。
- Discussion 很具体，Conclusion 过度空泛。
- Discussion 在谈机制，Conclusion 在谈价值观。
- Limitations 提到的边界，Discussion 前面从未铺垫。
- practical implications 很大，sample boundary 却非常窄。
- Conclusion 不是回声收束，而是新摘要。

## 默认输出
```markdown
## Polished Discussion
[英文改写]

## Polished Limitations and Future Research
[英文改写]

## Polished Conclusion
[英文改写]

## Cross-Part Revision Notes
1. Core proposition: [一句话]
2. Strongest defensible claim: [一句话]
3. Broader significance: [一句话]
4. [说明本次如何保证 Discussion / Limitations / Conclusion 口径一致]
5. [说明本次如何处理 claim 边界与最终定调]
```

只有当用户明确要求“诊断”或“review”时，才额外输出简短问题清单。
