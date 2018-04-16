# -*- coding: utf-8 -*-
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

try:
    long_description = open("README.md").read()
except IOError:
    long_description = ""

about = {}
with open(os.path.join(here, "text_normalizer", "__version__.py")) as f:
    exec(f.read(), about)

setup(
    name="text-normalizer",
    version=about["__version__"],
    description="Yoctol Natural Language Text Normalizer",
    license="MIT",
    author="Solumilken",
    packages=find_packages(),
    install_requires=[
        'pandas;python_version>="3.5"',
        'pandas<0.21;python_version<"3.5"',
    ],
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    include_package_data=True,
)
