#!/usr/bin/env python3

import sys
from setuptools import setup

if sys.version_info < (3, 6):
    raise RuntimeError("icoextract requires Python 3.6 or higher.")

with open('VERSION', encoding='utf-8') as f:
    VERSION = f.read().strip()

with open('src/version.py', 'w') as f:
    f.write( '# Autogenerated by setup.py\n')
    f.write(f"__version__ = '{VERSION}'\n")

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name="icoextract",
    description="Windows PE EXE icon extractor",
    version=VERSION,
    long_description=long_description,
    long_description_content_type='text/markdown',

    url="https://github.com/jlu5/icoextract",

    author="James Lu",
    author_email="james@overdrivenetworks.com",

    license="MIT/Expat",
    classifiers=[
        # https://pypi.org/classifiers/
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Operating System :: POSIX',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    packages=["icoextract"],
    package_dir={"icoextract": "src"},

    # Executable scripts
    scripts=["icoextract", "icolist", "exe-thumbnailer"],
)
