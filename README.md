# iWhat
What is it? Using AI Inspired by [pyWhat](https://github.com/bee-san/pyWhat)

![image](https://user-images.githubusercontent.com/15976103/223741774-a46ffde6-0f32-4f6f-8e6b-fda5bd07a235.png)

![image](https://user-images.githubusercontent.com/15976103/223899137-dd5bc056-3d06-4469-87af-a1887f55b8fc.png)


## 安装


```console
pip install iwhat
```

## 使用

iwhat ${word}
看截图你就懂了

## 注意

1. 能正常联网的环境或 proxy
2. 如果你遇到了墙需要用 Cloudflare Workers 替换 api_base 请使用 `--api_base ${url}` 来替换。**请注意，此处你输入的api应该是"`https://xxxx/v1`"的字样，域名需要用引号包裹**
3. what 请用单引号包裹
4. export OPENAI_API_KEY=${your_api_key} or --openai_key ${key}

```
export OPENAI_API_KEY=${your_api_key}
iwhat '0x52908400098527886E0F7030069857D2E4169EE7'
```

## 赞赏
谢谢就够了
