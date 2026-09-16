# Template Metadata Toolkit

一个可独立使用的演示文稿模板元数据约定与校验工具。它适用于模板目录、设计系统或内容生成管线的前置校验，不依赖 Presenton++ 应用本身。

## 内容

- `schema.json`：Draft 2020-12 JSON Schema，定义最小模板元数据结构。
- `validate_template.py`：只使用 Python 标准库的结构校验器。
- `examples/product-brief.json`：符合 schema 的示例。

## 模板元数据

每个模板由一个 JSON 文件描述。必须包含：

- `id`：稳定的机器可读标识符；
- `name`：面向用户的名称；
- `description`：简短用途说明；
- `layouts`：至少一个布局，每个布局都有 `id`、`name` 和 `purpose`。

可选的 `tags` 可帮助模板库进行筛选。

## 校验

```bash
python validate_template.py examples/product-brief.json
```

成功时退出码为 0；结构不符合约定时会输出所有发现的问题并返回非零退出码。

## 许可

本工具包按仓库根目录的 [MIT License](../LICENSE) 发布。
