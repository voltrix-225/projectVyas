from setuptools import setup, find_packages

setup(
    name = "cra-analyzer",
    version='1.0',
    packages = find_packages(),
    install_requires = ["pylint", ],
    description = "Code analyzer",
    entry_points = {
        "console_scripts" : ["analyze = src.main:main"],
    },
)