#!/usr/bin/env python3
"""对比矩阵生成器

基于 data/matrix.json 生成 Markdown 格式对比矩阵表格。
用法: python generate_matrix.py
"""

import json
from pathlib import Path


MATRIX_DATA = {
    "tools": [
        {
            "name": "Claude Code",
            "company": "Anthropic",
            "size_kb": 3.5,
            "identity": "交互式CLI工具",
            "tool_format": "XML标签",
            "boundary_strategy": "防御性安全+URL禁猜",
            "tone": "极简（≤4行）",
            "security": "防御安全底线",
            "context": "env注入+gitStatus快照",
        },
        {
            "name": "Cursor",
            "company": "Anyscale",
            "size_kb": 11.5,
            "identity": "GPT-4o AI编码助手",
            "tool_format": "JSON Function Calling",
            "boundary_strategy": "schema约束",
            "tone": "专业对话",
            "security": "标准",
            "context": "全量注入（标注可选）",
        },
        {
            "name": "Kimi K2.5",
            "company": "Moonshot AI",
            "size_kb": 10.1,
            "identity": "AI助手",
            "tool_format": "JSON Function Calling",
            "boundary_strategy": "限制→生态导流",
            "tone": "温和专业",
            "security": "标准+隐私",
            "context": "基础env",
        },
        {
            "name": "Devin",
            "company": "Cognition",
            "size_kb": 30.7,
            "identity": "真正的编程高手",
            "tool_format": "XML标签",
            "boundary_strategy": "工程方法论约束",
            "tone": "工程详尽",
            "security": "sudo审批+密钥保护",
            "context": "详细环境注入",
        },
        {
            "name": "Cline",
            "company": "VS Code插件",
            "size_kb": 52.0,
            "identity": "技术精湛软件工程师",
            "tool_format": "XML+审批标记",
            "boundary_strategy": "用户审批二元制",
            "tone": "详尽技术文档",
            "security": "二元审批（安全/危险）",
            "context": "new_task预加载",
        },
        {
            "name": "Gemini CLI",
            "company": "Google",
            "size_kb": 74.4,
            "identity": "Google AI工具",
            "tool_format": "混合格式",
            "boundary_strategy": "Google AI原则",
            "tone": "技术标准",
            "security": "Google AI原则",
            "context": "env+文件索引",
        },
        {
            "name": "Trae",
            "company": "字节跳动",
            "size_kb": 15.0,
            "identity": "AI编码助手",
            "tool_format": "JSON Function Calling",
            "boundary_strategy": "Prompt防护+不道歉",
            "tone": "专业直给",
            "security": "Prompt防护+内容过滤",
            "context": "文件树+光标",
        },
        {
            "name": "通义千问/Qoder",
            "company": "阿里巴巴",
            "size_kb": 10.0,
            "identity": "AI编码助手(Quest)",
            "tool_format": "Quest双Agent",
            "boundary_strategy": "最严拒绝+不指导",
            "tone": "专业工程",
            "security": "零指导拒绝",
            "context": "Quest共享上下文",
        },
        {
            "name": "GitHub Copilot",
            "company": "Microsoft",
            "size_kb": 15.0,
            "identity": "AI编程助手",
            "tool_format": "JSON Function Calling",
            "boundary_strategy": "VSCode集成约束",
            "tone": "简洁专业",
            "security": "Microsoft标准",
            "context": "编辑器全量上下文",
        },
        {
            "name": "Windsurf",
            "company": "Codeium",
            "size_kb": 10.0,
            "identity": "代理式AI Agent",
            "tool_format": "JSON Function Calling",
            "boundary_strategy": "模型伪装反侦察",
            "tone": "专业工程",
            "security": "模型伪装(GPT 4.1)",
            "context": "env注入",
        },
    ]
}


def generate_matrix_md(matrix: dict) -> str:
    """生成对比矩阵Markdown"""
    tools = matrix["tools"]
    dims = ["name", "company", "tool_format", "security", "tone", "context"]

    headers = {
        "name": "工具",
        "company": "公司",
        "tool_format": "工具调用",
        "security": "安全策略",
        "tone": "语气风格",
        "context": "上下文管理",
    }

    lines = [
        "# AI Agent 系统提示词对比矩阵\n",
        "> 自动生成 | 数据版本: 2026-07-02\n",
        "| " + " | ".join(headers[d] for d in dims) + " |",
        "| " + " | ".join("---" for _ in dims) + " |",
    ]

    for tool in tools:
        row = [tool[d] for d in dims]
        lines.append("| " + " | ".join(row) + " |")

    return "\n".join(lines)


def generate_design_insights(matrix: dict) -> str:
    """生成设计洞察"""
    tools = matrix["tools"]

    xml_tools = [t["name"] for t in tools if "XML" in t["tool_format"]]
    json_tools = [t["name"] for t in tools if "JSON" in t["tool_format"]]
    strict_sec = [t["name"] for t in tools if "审批" in t["security"] or "拒绝" in t["security"] or "防卫" in t["security"]]

    lines = [
        "\n## 设计洞察\n",
        f"### 工具格式分布",
        f"- **XML标签派**（{len(xml_tools)}个）: {', '.join(xml_tools)}",
        f"- **JSON Function Calling派**（{len(json_tools)}个）: {', '.join(json_tools)}",
        "",
        f"### 安全策略梯度",
        f"- **严格审批**（{len(strict_sec)}个）: {', '.join(strict_sec)}",
        "",
        f"### 提示词体量",
        "| 体量 | 代表 |",
        "| --- | --- |",
    ]

    sizes = [(t["name"], t["size_kb"]) for t in tools]
    sizes.sort(key=lambda x: -x[1])
    for name, sz in sizes:
        if sz < 15:
            cat = "精简"
        elif sz < 40:
            cat = "中等"
        else:
            cat = "大型"
        lines.append(f"| {name} | {sz}KB ({cat}) |")

    return "\n".join(lines)


def main():
    base_dir = Path(__file__).parent.parent
    output_path = base_dir / "analysis_matrix.md"
    data_path = base_dir / "data" / "matrix.json"

    # 保存JSON数据
    data_path.parent.mkdir(parents=True, exist_ok=True)
    data_path.write_text(json.dumps(MATRIX_DATA, ensure_ascii=False, indent=2), encoding="utf-8")

    # 生成Markdown矩阵
    md = generate_matrix_md(MATRIX_DATA)
    md += generate_design_insights(MATRIX_DATA)

    output_path.write_text(md, encoding="utf-8")
    print(f"[OK] 矩阵已生成: {output_path}")
    print(f"[OK] 数据已保存: {data_path}")


if __name__ == "__main__":
    main()
