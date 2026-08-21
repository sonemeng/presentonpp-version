# presentonpp-version

Presenton++ 的版本源仓库。应用内的更新检查器轮询本仓库的 `version.json`，
发现新版本时在界面底部弹出更新横幅，"Download update" 按钮指向本仓库的
Releases 页面。

## version.json 格式

```json
{
  "version": "0.9.6-pptb.3",
  "message": "更新说明（支持换行，会作为 What's new 弹层展示）",
  "downloads": {
    "linux": "https://github.com/sonemeng/presentonpp-version/releases/latest",
    "mac": "https://github.com/sonemeng/presentonpp-version/releases/latest",
    "windows": "https://github.com/sonemeng/presentonpp-version/releases/latest"
  }
}
```

- `version`：必须是比已装版本更新的语义化版本，否则不弹横幅。
- `message`：可选，What's new 内容。
- `downloads.windows`：可选，横幅下载按钮的跳转地址（缺省用 Releases 页）。

## 发版流程

1. 本地完成 Presenton++ 的双版本打包（干净版 + 配置版）。
2. 更新 `version.json` 的 `version` 与 `message` 并推送到 `main`。
3. `gh release create <版本号>` 创建 Release 并上传干净版安装程序 exe。

注意：应用每分钟轮询一次（启动 2 分钟后开始），拉取的是 `main` 分支
`version.json` 的 raw 地址，改动推送后即时生效。
