# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name="a3rt-sdk-py",
    packages=["a3rt"],
    version="0.0.3",
    description="Python SDK for A3RT",
    install_requires=["requests"],
    url="https://a3rt.recruit-tech.co.jp/",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
