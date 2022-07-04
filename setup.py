from setuptools import setup, find_packages


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="nmod",
    version="0.0.1",
    author="Andrey Golovanov",
    description="A simple network modeling toolkit.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/networmix/netmodel",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_packages(exclude=("tests", "dev", "examples")),
    python_requires=">=3.8",
    tests_require=["pytest"],
)
