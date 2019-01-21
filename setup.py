# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

try:
    long_description = open("README.rst").read()
except IOError:
    long_description = ""

setup(
    name="guess_indian_gender",
    version="1.0.1",
    description="Guess gender from indian names",
    license="MIT",
    author="v-adhithyan",
    author_email="pollachi.developer@gmail.com",
    url="https://github.com/v-adhithyan/gender-guess-indiannames",
    packages=find_packages(),
    install_requires=[
                        "nltk",
                        "pandas",
                      ],
    include_package_data=True,
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
