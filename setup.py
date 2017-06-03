import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "sqlNice",
    version = "0.0.1",
    author = "Thiago Baldim",
    author_email = "thiagorbaldim@gmail.com",
    description = ("A simple model of running queries with sqlite3 in a more beautiful way"),
    license = "Apache-2.0",
    keywords = "sqlite3 REST",
    url = "https://github.com/TRBaldim/sqlNice",
    packages=find_packages(),
    test_suite='tests',
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: Development",
        "Topic :: Utilities",
        "License :: Apache-2.0",
    ],
)
