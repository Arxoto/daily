# vscode 代码片段

## 教程

1. 文件-首选项-配置代码片段
1. input a name and edit file
1. a help website [snippet-generator](https://snippet-generator.app/?description=&tabtrigger=&snippet=%0A&mode=vscode)

## Example

workspace
```json
{
	"rust_test_mod": {
		"scope": "rust",
		"prefix": "test_mod",
		"body": [
			"",
			"#[cfg(test)]",
			"mod tests {",
			"    use super::*;",
			"",
			"    $0",
			"}",
			""
		],
		"description": ""
	},
	"rust_test_fn": {
		"scope": "rust",
		"prefix": "test_fn",
		"body": [
			"",
			"#[test]",
			"fn ${1:test_func}() {",
			"    $0",
			"}",
			""
		],
		"description": ""
	},
	"python_main": {
		"scope": "python",
		"prefix": "main",
		"body": [
			"",
			"",
			"def ${1:main}():",
			"    ${2:pass}$0",
			"",
			"",
			"if __name__ == \"__main__\":",
			"    ${1:main}()",
			""
		],
		"description": ""
	}
}
```
