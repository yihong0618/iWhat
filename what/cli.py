from what.what import What

import argparse
import os
from os import environ as env


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("what", help="what is it")
    parser.add_argument(
        "--openai_key", dest="openai_key", type=str, default="", help="OpenAI api key"
    )
    parser.add_argument(
        "-p",
        "--proxy",
        dest="proxy",
        type=str,
        default="",
        help="use proxy like http://127.0.0.1:7890",
    )
    # args to change api_base
    parser.add_argument(
        "--api_base",
        dest="api_base",
        type=str,
        help="specify base url other than the OpenAI's official API address",
    )
    parser.add_argument(
        "--en", dest="en", action="store_true", help="If use English to answer"
    )

    options = parser.parse_args()
    PROXY = options.proxy
    if PROXY != "":
        os.environ["http_proxy"] = PROXY
        os.environ["https_proxy"] = PROXY

    OPENAI_API_KEY = options.openai_key or env.get("OPENAI_API_KEY")
    if not OPENAI_API_KEY:
        raise Exception("OpenAI API key not provided, please google how to obtain it")

    what = What(options.what, is_en=options.en, api_base=options.api_base)
    what.show_what()


if __name__ == "__main__":
    main()
