# 使用指南

> 如何使用这个仓库中的分析工具和设计模式

---

## 🛠 脚本工具

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

→ 参考 [IMPROVEMENT_PROPOSAL.md](./IMPROVEMENT_PROPOSAL.md) 中的设计模式实战改进案例

---

## 📚 扩展学习

### 拓展练习

1. **模式匹配**：找一个不在列表中的AI工具，看看它使用了7个模式中的哪几个
2. **模式改进**：尝试改进1个模式（比如给"渐进式拒绝"加一个新的降级层）
3. **新建模式**：分析过程中你是否发现了第8个模式？

### 内容复用

仓库中的markdown文件可用于：
- 把 PATTERNS.md 改写为技术博文
- 把 analysis_matrix.md 做成信息图
- 把 scripts/ 扩展到更多工具的自动化分析

---

## ❓ FAQ

**Q: 提示词会过期吗？**
A: 会的。分析基于2025-2026年的提示词版本。可以用 `analyze_prompt.py` 对新版本做增量分析。

**Q: 可以直接用这些模式吗？**
A: 可以。通用设计模式，不涉及任何工具的商业秘密。MIT协议。

**Q: 为什么是这10个工具？**
A: 覆盖了行业巨头（Google/Microsoft/字节/阿里）、明星创业（Anthropic/Cognition）、和开源社区（Cline），设计思想光谱完整。
