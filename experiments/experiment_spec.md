# 实验需求规格书：智能简历解析Agent

## 项目概述
搭建一个Web应用，用户可以上传简历PDF文件，系统调用大语言模型（LLM）提取结构化信息，并以JSON格式展示结果。

## 功能需求

### 1. 文件上传
- 支持 PDF 文件上传（拖拽或点击选择）
- 文件大小限制 5MB
- 上传后显示文件名和大小

### 2. PDF文本提取
- 使用 PyPDF2 或 pdfplumber 提取PDF中的文本内容
- 处理中文编码

### 3. LLM解析
- 调用大语言模型API（如OpenAI API格式），将提取的文本发送给LLM
- Prompt要求LLM返回结构化JSON，包含以下字段：
  - name: 姓名
  - email: 邮箱
  - phone: 电话
  - education: [{school, degree, major, year}]
  - experience: [{company, title, duration, description}]
  - skills: [技能列表]
  - summary: 一句话总结

### 4. 结果展示
- 以结构化卡片形式展示解析结果
- 支持JSON原始数据切换查看
- 展示LLM调用耗时

### 5. 错误处理
- 文件格式错误提示
- PDF解析失败提示
- LLM API调用失败重试（最多3次）
- Loading状态展示

## 技术栈约束
- 后端：Python Flask
- 前端：原生HTML/CSS/JS（不引入React/Vue等框架）
- LLM API：OpenAI兼容格式（配置化，支持切换）
- 环境变量：API Key通过 .env 文件管理

## 验收标准
1. 能上传PDF并成功解析出结构化信息
2. 前端界面美观、响应式
3. API调用有重试机制
4. 有完整的错误提示
5. 代码有注释

## 交付物
- 完整的可运行项目目录
- requirements.txt
- .env.example（不含真实API Key）
- README.md（含运行说明）
