import json
import string
from rich.console import Console
from rich.table import Table
from rich.style import Style
from rich.text import Text

from openai import OpenAI


class What:
    def __init__(self, what, is_en=False, api_base=None):
        self.client = OpenAI()
        if api_base:
            self.client = OpenAI(base_url=api_base)
        else:
            self.client = OpenAI()

        self.what = what
        self.is_en = is_en
        self.what_prompt = """
            f这个 `{what}` 可能是什么，请按照json格式回答，key值有Maybe和Desc，Maybe回答他最可能是的东西（要求精确些），Desc回答这个东西的描述;
            答案应该使用中文。
            """.format(
            what=what
        )
        if is_en:
            self.what_prompt = """
                What is`{what}` might be? please answer in JSON format with key values of 'Maybe' and 'Desc'. 
                'Maybe' should provide the most likely thing it is (be more precise), 
                while 'Desc' should describe what this thing is. 
                And you answer must be english.
                """.format(
                what=what
            )

    def _to_what(self):
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": self.what_prompt}],
        )
        return completion.choices[0].message.content.encode("utf8").decode()

    @staticmethod
    def _is_all_punctuations(s):
        return all(c in string.punctuation for c in s)

    def _handle_exception_answer(self):
        if self.is_en:
            maybe_prompt = "What is`{what}` most likely to be? (Please try to answer more precisely.)".format(
                what=self.what
            )
            desc_prompt = "Describe what `{what}` most likely to be".format(
                what=self.what
            )
        else:
            maybe_prompt = "这个 `{what}` 最可能是什么？（要求精确些）".format(what=self.what)
            desc_prompt = "描述`{what}`最可能是什么".format(what=self.what)
        self.what_prompt = maybe_prompt
        maybe_what = self._to_what()
        self.what_prompt = desc_prompt
        desc_what = self._to_what()
        what_json = {"Maybe": maybe_what, "Desc": desc_what}
        return what_json

    @staticmethod
    def _change_line_by_comma_period(in_str):
        return (
            in_str.replace("，", "，\r\n")
            .replace("。", "。\r\n")
            .replace(",", ",\r\n")
            .replace(".", ".\r\n")
        )

    def show_what(self):
        what = self._to_what()
        try:
            what_json = json.loads(what)
            if "Maybe" not in what_json or "Desc" not in what_json:
                raise Exception("Keys incomplete In JSON")
        except Exception:
            # handle exception when gpt answer is not json format
            what_json = self._handle_exception_answer()

        if not what_json:
            raise Exception("No what JSON!")

        console = Console()
        title = Text("What is it AI", style=Style(color="#268bd2", bold=True))
        table = Table(title=title, show_lines=False, style="dim")
        table.add_column("What", style=Style(color="#b58900"))
        table.add_column("Maybe", style=Style(color="#d33682"), justify="middle")
        table.add_column("Desc", style=Style(color="#859900"), justify="left")
        maybe = self._change_line_by_comma_period(what_json["Maybe"].strip())
        desc = self._change_line_by_comma_period(what_json["Desc"].strip())
        table.add_row(self.what, maybe, desc)
        console.print(table)
