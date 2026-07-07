# Agent 系统提示词设计模式

> 🔬 从10个主流AI编码工具逆向提炼的Agent设计模式库  
> 📊 6维度 × 10工具深度对比 | 7大通用设计模式 | 可复用分析脚本

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
![Status](https://img.shields.io/badge/status-active-brightgreen)

---

## 🎯 这是什么？

对Claude Code、Cursor、Devin、Kimi等10个主流AI编码工具的**真实系统提示词**进行源码级分析，提炼出7个跨工具的通用设计模式，并在实际Agent框架中验证了实战价值。

---

## 📂 仓库结构

```
├── README.md                    # 你在看这里
├── PATTERNS.md                  # 🔥 7大通用设计模式（核心）
├── ANALYSIS.md                  # 10工具逐项深度6维度分析
├── USAGE.md                     # 📖 使用指南 + 分析脚本
├── IMPROVEMENT_PROPOSAL.md      # 设计模式实战应用案例
├── analysis_matrix.md           # 对比矩阵速查表
├── scripts/
│   ├── analyze_prompt.py        # 自动化提示词分析工具
│   └── generate_matrix.py       # 对比矩阵生成器
└── data/
    └── matrix.json              # 结构化对比数据(JSON)
```

### 文档导航

| 文档 | 内容 | 建议 |
|---|---|---|
| [PATTERNS.md](./PATTERNS.md) | 7大通用设计模式详解（核心） | 先读这个 |
| [ANALYSIS.md](./ANALYSIS.md) | 10工具6维度逐项分析 | 深入了解 |
| [analysis_matrix.md](./analysis_matrix.md) | 对比矩阵速查表 | 快速查阅 |
| [IMPROVEMENT_PROPOSAL.md](./IMPROVEMENT_PROPOSAL.md) | 设计模式实战应用案例 | 应用参考 |
| [USAGE.md](./USAGE.md) | 使用指南 + 分析脚本 | 工具使用 |

---

## 🔍 7大设计模式速览

| # | 模式 | 一句话 | 代表工具 |
|---|---|---|---|
| 1 | 分层安全防线 | 6层防线从外到内收紧 | Claude Code, Cline |
| 2 | 工具调用格式解耦 | XML vs JSON，选择影响Agent自主度 | Claude Code(XML) vs Cursor(JSON) |
| 3 | 语气梯度控制 | 从极简到详尽的语气密度设计 | Claude Code(极简) vs Devin(详尽) |
| 4 | 上下文窗口管理 | 3层优先级：必注入→条件→按需 | Claude Code(少而精) vs Cursor(多而全) |
| 5 | 渐进式拒绝 | 5级降级响应：完成→部分→引导→替代→拒绝 | Kimi, Claude Code, Qoder |
| 6 | 任务规划与执行分离 | TodoWrite/Plan/Quest三种规划策略 | Claude Code, Cline, Qoder |
| 7 | 身份锚定与Prompt防护 | 防注入+模型伪装+反侦察 | Trae, Windsurf |

→ 详见 [PATTERNS.md](./PATTERNS.md)

---

## 📊 分析覆盖

| 工具 | 公司 | 提示词量 | 设计亮点 |
|---|---|---|---|
| **Claude Code** | Anthropic | 3.5KB | 极简主义典范 |
| **Cursor** | Anyscale | 11.5KB | 工具即能力 |
| **Kimi K2.5** | Moonshot AI | 10.1KB | 限制→生态导流 |
| **Devin** | Cognition | 30.7KB | 工程方法论手册 |
| **Cline** | VS Code | 52KB | 二元审批安全 |
| **Gemini CLI** | Google | 74KB | 体量最大 |
| **Trae** | 字节跳动 | ~15KB | 不道歉策略 |
| **通义千问/Qoder** | 阿里巴巴 | ~10KB | Quest多Agent |
| **Copilot** | GitHub | ~15KB | 编辑器深度集成 |
| **Windsurf** | Codeium | ~10KB | 模型伪装反侦察 |

→ 详见 [ANALYSIS.md](./ANALYSIS.md)

---

## ⚡ 快速开始

```bash
# 生成对比矩阵
python scripts/generate_matrix.py

# 分析单个提示词文件
python scripts/analyze_prompt.py path/to/system-prompt.txt
```

---

## 🏗️ 实战验证

本项目不仅停留在分析层面。基于发现的7个模式，对一个轻量Agent框架进行了5项改进验证：

- ✅ 模式3：语气梯度控制 → toneAdapt语气自适应系统
- ✅ 模式5：渐进式拒绝 → 5级fallback降级链
- ✅ 模式6：规划执行分离 → Plan-Execute两阶段架构

→ 详见 [IMPROVEMENT_PROPOSAL.md](./IMPROVEMENT_PROPOSAL.md)

---

## 🙏 致谢

数据来源：[system-prompts-and-models-of-ai-tools-chinese](https://github.com/InfyEdge/system-prompts-and-models-of-ai-tools-chinese)  
本项目全程由AI Agent驱动完成分析工作

---

## 📄 License

本项目基于MIT License。引用的提示词数据同样来自MIT项目。
