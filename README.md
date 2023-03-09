# iWhat
What is it? Using AI Inspired by [pyWhat](https://github.com/bee-san/pyWhat)

![image](https://user-images.githubusercontent.com/15976103/223741774-a46ffde6-0f32-4f6f-8e6b-fda5bd07a235.png)

![image](https://user-images.githubusercontent.com/15976103/223899137-dd5bc056-3d06-4469-87af-a1887f55b8fc.png)


## 安装


```console
pip install iwhat
```

## 使用

1. 首先，需要提供你的 OpenAI API key 。你可以把它导入到终端环境变量：

```
export OPENAI_API_KEY=${your_api_key}
```
导入后，以后查询到时候，就不用再提供这个参数了。

你也可以在拼接在查询命令行中：

```
iwhat ${word} --openai_key "sk-xxxxxx"`
```

2. 查询：

```
iwhat ${word}
```
**`word` 请用单引号包裹**，例如：`iwhat 'AI'`

## 注意

1. 能正常联网的环境或 proxy
2. 如果你遇到了墙需要用 Cloudflare Workers 替换 api_base 请使用 `--api_base ${url}` 来替换。**请注意，此处你输入的api应该是"`https://xxxx/v1`"的字样，域名需要用引号包裹**

## 赞赏
谢谢就够了
