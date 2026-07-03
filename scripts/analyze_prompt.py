#!/usr/bin/env python3
"""AI Agent系统提示词自动化分析工具

输入一个系统提示词文件，输出6维度结构化分析结果：
1. 身份声明
2. 工具调用格式
3. 边界约束
4. 语气风格
5. 安全策略
6. 上下文管理

用法: python analyze_prompt.py <文件路径> [--json]
"""

import re
import sys
import json
import argparse
from pathlib import Path


DIMENSIONS = {
    "identity": {
        "keywords": ["你是", "你是一个", "你是一名", "你作为", "You are", "身份"],
        "extract": lambda text: _extract_identity(text),
    },
    "tool_format": {
        "keywords": ["<>", "</", "function_call", "tools", "工具"],
        "extract": lambda text: _detect_tool_format(text),
    },
    "boundaries": {
        "keywords": ["不能", "不要", "拒绝", "禁止", "切勿", "不会", "不应该", "must not", "do not"],
        "extract": lambda text: _extract_boundaries(text),
    },
    "tone": {
        "keywords": ["语气", "风格", "简洁", "直接", "友好", "专业", "tone", "style", "concise"],
        "extract": lambda text: _extract_tone(text),
    },
    "security": {
        "keywords": ["安全", "密钥", "恶意", "漏洞", "密码", "security", "malicious", "key", "secret"],
        "extract": lambda text: _extract_security(text),
    },
    "context": {
        "keywords": ["上下文", "环境", "git", "文件", "env", "context", "environment", "workspace"],
        "extract": lambda text: _extract_context(text),
    },
}


def _extract_identity(text: str) -> str:
    """提取身份声明"""
    patterns = [
        r"你是[一一个名位]?\s*(.+?)[。\n]",
        r"你[是叫为]\s*(.+?)[，,。\n]",
        r"You are an?\s+(.+?)[.,\n]",
    ]
    for p in patterns:
        m = re.search(p, text, re.IGNORECASE)
        if m:
            return m.group(1).strip()
    return "未检测到"


def _detect_tool_format(text: str) -> dict:
    """检测工具调用格式"""
    xml_count = len(re.findall(r"<\w+>.*?</\w+>", text, re.DOTALL))
    json_tool = len(re.findall(r'"name"\s*:\s*"', text))
    function_call = "function_call" in text.lower() or "tool_choice" in text.lower()

    fmt = []
    if xml_count > 3:
        fmt.append("XML标签")
    if json_tool > 2 or function_call:
        fmt.append("JSON Function Calling")

    result = {"detected": fmt if fmt else ["未检测到明确格式"], "xml_count": xml_count, "json_tool_count": json_tool}
    return result


def _extract_boundaries(text: str) -> list:
    """提取边界约束"""
    lines = text.split("\n")
    constraints = []
    neg_patterns = [r"不能", r"不要", r"拒绝", r"禁止", r"切勿", r"不会", r"不应该"]

    for line in lines:
        for pattern in neg_patterns:
            if re.search(pattern, line):
                cleaned = line.strip().lstrip("- *>#")
                if 5 < len(cleaned) < 200:
                    constraints.append(cleaned)
                break

    return constraints[:10]


def _extract_tone(text: str) -> dict:
    """提取语气风格"""
    tone_info = {"style": "未指定", "rules": []}

    # 检测极简风格
    if re.search(r"(简洁|不超过|精简|省略|省略不必要|concise|brief|minimal|without|不要.*多余)", text, re.IGNORECASE):
        tone_info["style"] = "极简"

    elif re.search(r"(友好|friend|礼貌|积极|helpful)", text, re.IGNORECASE):
        tone_info["style"] = "友好"

    elif re.search(r"(专业|professional|正式|formal|enterprise)", text, re.IGNORECASE):
        tone_info["style"] = "专业"

    # 提取具体语气规则
    tone_patterns = [
        r"(不[要应]?.*?道歉.*?)([。；;])",
        r"(不[要应]?.*?表情.*?)([。；;])",
        r"(不[要应]?.*?emoji.*?)([。；;])",
        r"(请.*?语气.*?)([。；;])",
    ]
    for p in tone_patterns:
        m = re.search(p, text, re.IGNORECASE)
        if m:
            tone_info["rules"].append(m.group(1).strip())

    return tone_info


def _extract_security(text: str) -> dict:
    """提取安全策略"""
    sec = {"level": "basic", "rules": []}

    rules = []

    if re.search(r"(不安全|恶意|攻击|weapon|exploit|malware)", text, re.IGNORECASE):
        rules.append("拒绝恶意用途")
    if re.search(r"(密钥|密码|敏感|secret|password|API.?key)", text, re.IGNORECASE):
        rules.append("密钥保护")
    if "defensive" in text.lower() or "防御" in text:
        rules.append("仅限防御性安全")
    if re.search(r"(批准|approval|确认|用户.*允许)", text, re.IGNORECASE):
        rules.append("操作审批机制")
    if re.search(r"(不.*透露.*提示|不.*泄露.*系统|prompt.?protect)", text, re.IGNORECASE):
        rules.append("Prompt防护")

    if len(rules) >= 3:
        sec["level"] = "strict"
    elif len(rules) >= 1:
        sec["level"] = "standard"

    sec["rules"] = rules
    return sec


def _extract_context(text: str) -> dict:
    """提取上下文管理策略"""
    ctx = {"injection": [], "updates": "未知"}

    if re.search(r"git.?status|gitStatus|Git.*快照", text, re.IGNORECASE):
        ctx["injection"].append("Git状态")
    if re.search(r"工作目录|working.?directory|cwd", text, re.IGNORECASE):
        ctx["injection"].append("工作目录")
    if re.search(r"平台|platform|OS|操作系统", text, re.IGNORECASE):
        ctx["injection"].append("操作系统")
    if re.search(r"文件.*打开|opened.?file|光标|cursor", text, re.IGNORECASE):
        ctx["injection"].append("打开文件/光标")
    if re.search(r"linter|错误|error|lint", text, re.IGNORECASE):
        ctx["injection"].append("Linter/错误")

    if re.search(r"(自动更新|实时更新|实时|automatic)", text, re.IGNORECASE):
        ctx["updates"] = "自动更新"
    elif re.search(r"(快照|snapshot|初始|不会.*更新)", text, re.IGNORECASE):
        ctx["updates"] = "快照（不自动更新）"

    return ctx


def analyze_file(filepath: str) -> dict:
    """分析单个提示词文件"""
    path = Path(filepath)
    if not path.exists():
        return {"error": f"文件不存在: {filepath}"}

    text = path.read_text(encoding="utf-8", errors="ignore")

    result = {
        "file": str(path.name),
        "size_kb": round(len(text) / 1024, 1),
        "word_count": len(text),
    }

    for dim_name, dim_config in DIMENSIONS.items():
        result[dim_name] = dim_config["extract"](text)

    return result


def main():
    parser = argparse.ArgumentParser(description="AI Agent系统提示词自动化分析")
    parser.add_argument("file", nargs="?", help="提示词文件路径")
    parser.add_argument("--json", action="store_true", help="输出JSON格式")
    args = parser.parse_args()

    if not args.file:
        parser.print_help()
        sys.exit(1)

    result = analyze_file(args.file)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"\n{'='*60}")
        print(f"📄 文件: {result['file']} ({result['size_kb']}KB)")
        print(f"{'='*60}")
        print(f"\n🎭 身份声明: {result['identity']}")
        print(f"\n🔧 工具格式: {', '.join(result['tool_format']['detected'])}")
        print(f"\n🚧 边界约束 ({len(result['boundaries'])}条):")
        for b in result['boundaries'][:5]:
            print(f"   • {b}")
        print(f"\n💬 语气风格: {result['tone']['style']}")
        for r in result['tone']['rules']:
            print(f"   • {r}")
        print(f"\n🔒 安全策略: {result['security']['level']}")
        for r in result['security']['rules']:
            print(f"   • {r}")
        print(f"\n🌐 上下文管理:")
        print(f"   注入: {', '.join(result['context']['injection']) or '无'}")
        print(f"   更新: {result['context']['updates']}")
        print()


if __name__ == "__main__":
    main()
