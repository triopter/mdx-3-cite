#!/usr/bin/env python
import os
import sys

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(
    name="mdx_cite",
    version="0.1",
    description="markdown extension for the <cite> tag",
    author="Noemi Millman",
    author_email="noemi@triopter.com",
    py_modules=["mdx_cite"],
    install_requires=[
        "markdown>=3.0"
    ],
    extras_require={'dev': ['pytest']},
    license="MIT",
)
