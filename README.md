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

`0.9.6-pptb.11` 修复了 Editorial 模板导出时的背景兼容问题，并补齐桌面端运行所需的 Sentry 依赖。

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
