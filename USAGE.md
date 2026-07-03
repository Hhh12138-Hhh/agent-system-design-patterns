# 使用指南

> 这个仓库你可以怎么用？面试官可以怎么读？

---

## 👤 你（开发者/求职者）怎么用

### 面试场景：30秒电梯游说

> "我最近做了一个Agent系统设计模式的研究项目——我分析了Claude Code、Cursor、Devin等10个主流AI工具的系统提示词源码，提炼出了7个通用的Agent设计模式，然后用这些模式反向改进我自己的Agent框架，验证了它们的实战价值。"

### 面试场景：技术深挖时的回答

**Q: "你具体分析了什么？"**
→ 指向 [ANALYSIS.md](./ANALYSIS.md)：6维度（身份/工具格式/边界/语气/安全/上下文）× 10工具的逐项分析

**Q: "你发现了什么规律？"**
→ 指向 [PATTERNS.md](./PATTERNS.md)：7个可复用的设计模式，每个都有"问题→方案→实例→适用场景"

**Q: "你怎么验证这些模式的？"**
→ 指向 [IMPROVEMENT_PROPOSAL.md](./IMPROVEMENT_PROPOSAL.md)：5项反哺GenericAgent的实战改进

**Q: "你有什么量化产出？"**
→ 指向 [analysis_matrix.md](./analysis_matrix.md)：对比矩阵速查表，一目了然

### 日常使用：扩展分析

```bash
# 1. 分析新的提示词文件
python scripts/analyze_prompt.py path/to/new-system-prompt.txt

# 2. 生成更新后的对比矩阵
python scripts/generate_matrix.py
```

### 技术博客/分享

仓库中的所有markdown文件都是**即用型**内容。你可以：
- 把 PATTERNS.md 改写成一篇 Agent Design Patterns 博文
- 把 analysis_matrix.md 做成信息图
- 把 scripts/ 扩展到更多工具的自动化分析

---

## 👔 面试官/技术Leader怎么读

### 5分钟快速评估

1. **README.md**（2分钟）：了解项目全貌
2. **PATTERNS.md**（3分钟）：看设计模式提炼是否深刻

### 判断标准

**能看出此人具备以下能力的信号：**

| 能力 | 在哪里看 | 信号 |
|---|---|---|
| 深度技术理解 | ANALYSIS.md 每节末尾的"核心洞察" | 不是泛泛而谈，有独特视角 |
| 抽象归纳能力 | PATTERNS.md 的7个模式 | 能跨越10个工具找到共性 |
| 工程落地能力 | IMPROVEMENT_PROPOSAL.md | 不是纸上谈兵，有before/after对比 |
| 工具驾驭力 | 整个项目由AI Agent驱动完成 | 理解AI Agent的真正价值 |

---

## 📚 学习者怎么用

### 推荐学习路径

```
Day 1: README.md → analysis_matrix.md（建立全局观）
Day 2: ANALYSIS.md 精读（理解每个工具的设计哲学）
Day 3: PATTERNS.md 精读（掌握7个通用模式）
Day 4: 动手：用 scripts/analyze_prompt.py 分析一个新工具
Day 5: IMPROVEMENT_PROPOSAL.md → 在自己的项目中应用
```

### 扩展练习

1. **模式匹配**：找一个不在列表中的AI工具，看看它使用了7个模式中的哪几个
2. **模式改进**：尝试改进1个模式（比如给"渐进式拒绝"加一个新的降级层）
3. **新建模式**：分析过程中你是否发现了第8个模式？

---

## 🏗️ 应用到自己的Agent项目

### 极简起步（30分钟）

从 PATTERNS.md 中选1个模式应用到你的项目：

```
模式3（语气梯度控制）是最容易入手的：
1. 定义3档语气密度：极简/专业/详尽
2. 给你的Agent加一个参数控制语气
3. 在不同场景下切换
```

### 进阶实战（2小时）

同时应用3个模式：

```
模式1（安全防线）+ 模式5（渐进拒绝）+ 模式6（规划执行分离）
= 一个安全、优雅、可控的Agent框架
```

→ 参考 [IMPROVEMENT_PROPOSAL.md](./IMPROVEMENT_PROPOSAL.md) 中的GenericAgent改进案例

---

## 🔧 脚本说明

### `scripts/analyze_prompt.py`

自动化分析工具，输入一个系统提示词文件，输出结构化分析结果。

```bash
python scripts/analyze_prompt.py <文件路径>
```

输出包括：
- 身份声明提取
- 工具调用格式识别（XML/JSON/混合）
- 边界约束汇总
- 语气风格关键词
- 安全策略摘要

### `scripts/generate_matrix.py`

基于 `data/matrix.json` 生成对比矩阵Markdown表格。

```bash
python scripts/generate_matrix.py
```

---

## ❓ 常见问题

**Q: 提示词会过期吗？**
A: 会的。分析基于2025-2026年的提示词版本。你可以用 `analyze_prompt.py` 对新版本做增量分析。

**Q: 我可以直接用这些模式吗？**
A: 可以。这些是通用设计模式，不涉及任何工具的商业秘密。MIT协议。

**Q: 为什么是这10个工具？**
A: 覆盖了行业巨头（Google/Microsoft/字节/阿里）、明星创业（Anthropic/Cognition）、和开源社区（Cline），设计思想光谱完整。
