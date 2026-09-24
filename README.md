# Presenton++

Presenton++ 是一款本地运行的 AI 演示文稿创作工具。本仓库提供 Windows 版本发布、更新说明，以及一个可独立使用的模板元数据工具包。

## 下载与安装

请前往 [Releases](https://github.com/sonemeng/presentonpp-version/releases) 下载最新的 Windows 安装程序：

1. 下载 `Presentonpp-<version>-installer.exe`。
2. 右键选择“以管理员身份运行”或直接双击安装。
3. 按安装向导完成安装并启动 Presenton++。
4. 如 Windows 显示来自未知发布者的提示，请确认下载来源为本仓库的 GitHub Release 后再继续。

每个发布版本都附带 `SHA256SUMS.txt`。可在 PowerShell 中校验下载文件：

```powershell
Get-FileHash .\Presentonpp-<version>-installer.exe -Algorithm SHA256
```

将输出的 SHA-256 与 `SHA256SUMS.txt` 中的值进行比对。

## 更新

应用启动后会定期检查本仓库的 `version.json`。发现新版本时，应用内会显示更新提示并跳转到 Releases 下载页。建议在更新前关闭正在编辑的演示文稿并保存工作。

## 本次发布

`0.9.6-pptb.12` 修复了大纲生成卡住时误报「无法连接到服务器」的问题：大纲请求恢复流式输出并新增连接保活，慢速渠道不再被提前判定为断线；失败提示改为「请更换渠道或模型重试」，直接指向可操作的动作。同时兼容忽略 `response_format` 的中转站（返回 Markdown 或纯文本时按标题自动切分大纲），并修复了打包版内置中文字体 404 的问题。

更新说明：

- 大纲流式生成不再把「慢」误报成「断线」，慢速渠道/模型会表现为可见的慢，而不是提前重试或报错。
- 大纲失败提示统一为「请更换渠道或模型重试」。
- 兼容忽略结构化输出参数的中转站，Markdown / 纯文本大纲可正常使用；解析失败只提示一次。
- 打包版内置字体（思源黑体 / 思源宋体 / 霞鹜文楷）可正常加载。

> 便携版附带一份预置的渠道与模型配置，便于首次启动时快速填写自己的 Key；它**不包含任何 API Key**，请填入你自己的密钥后再使用。

## 模板元数据工具包

[`template-toolkit/`](template-toolkit/) 是本仓库公开维护的独立、轻量工具包，提供：

- 通用模板元数据的 JSON Schema；
- 一个不依赖第三方包的 Python 校验脚本；
- 可作为自动化和集成起点的示例模板元数据。

它只涵盖通用的描述性模板元数据，不包含 Presenton++ 的核心应用、服务端、构建流水线、运行时组件或任何用户配置。使用方法见 [`template-toolkit/README.md`](template-toolkit/README.md)。

## 反馈与安全

- 功能问题和使用建议请通过 [Issues](https://github.com/sonemeng/presentonpp-version/issues) 提交。
- 请勿在 Issue、日志、截图或讨论中发布 API Key、访问令牌、密码或个人文档内容。
- 如需报告安全问题，请通过仓库所有者的私密渠道联系，而不要公开披露细节。

## 开源范围与许可证

本仓库中的文档、模板元数据工具包及其示例以 [MIT License](LICENSE) 发布。Presenton++ 的完整产品实现与发布构建不包含在本公开仓库中。
