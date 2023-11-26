from setuptools import setup

setup(
    name="iwhat",
    author="yihong0618",
    author_email="zouzou0208@gmail.com",
    url="https://github.com/yihong0618/iWhat",
    license="MIT",
    version="0.2.0",
    install_requires=["rich", "openai==1.1.1"],
    entry_points={
        "console_scripts": ["iwhat = what.cli:main"],
    },
)
