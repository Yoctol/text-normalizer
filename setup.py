from pathlib import Path

from setuptools import setup, find_packages
from utils.setup_utils.get_ext import get_ext_modules_n_cmdclass


ROOT_DIR = Path(__file__).parent


# make description
readme = ROOT_DIR.joinpath('README.md')
if readme.exists():
    with readme.open() as f:
        long_description = f.read()
        try:
            from pypandoc import convert_text
            long_description = convert_text(
                long_description, 'rst', format='md')
        except ImportError:
            print("warning: pypandoc module not found, could not convert Markdown to RST")
else:
    long_description = '-'


# get cython extension
ext_modules, cmdclass = get_ext_modules_n_cmdclass()


setup(
    name="text-normalizer",
    version="0.1.3",
    description="Yoctol Natural Language Text Normalizer",
    license="MIT",
    author="Solumilken",
    author_email="yien.tsai@yoctol.com",
    url="https://github.com/Yoctol/text-normalizer",
    packages=find_packages(),
    install_requires=[
        'pandas;python_version>="3.5"',
        'pandas<0.21;python_version<"3.5"',
    ],
    python_requires=">=3.5",
    long_description=long_description,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    include_package_data=True,
    cmdclass=cmdclass,
    ext_modules=ext_modules,
)
