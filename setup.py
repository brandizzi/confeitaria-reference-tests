#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name="confeitaria-reference-tests",
    version="0.1dev",
    author='Adam Victor Brandizzi',
    author_email='adam@brandizzi.com.br',
    description='Tests for implementations of Confeitaria',
    license='LGPLv3',
    url='http://bitbucket.com/brandizzi/confeitaria-reference-tests',

    packages=find_packages(),
    namespace_packages=['confeitaria', 'confeitaria.reference']
)
