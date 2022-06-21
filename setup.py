from typing import List

from setuptools import setup


def get_requirements() -> List[str]:
    with open("requirements.txt", "r") as f:
        return f.readlines()


def get_long_description() -> str:
    with open("README.md", "r", encoding="utf-8") as f:
        return f.read()


def get_version(fp) -> str:
    with open(fp, "r") as f:
        for line in f:
            if "version" in line:
                delim = '"'
                return line.split(delim)[1]
    raise RuntimeError(f"could not find a valid version string in {fp}.")


setup(
    name="practical-tsa",
    version=get_version("ptsa/__init__.py"),
    description="Classical and DL-based Time Series Analysis, "
    "with pretty visualizations in the browser.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    packages=["ptsa"],
    install_requires=get_requirements(),
    exclude=["tests"],
    author="Nicholas Junge",
    license="Apache-2.0",
    url="https://github.com/nicholasjng/practical-tsa",
)
