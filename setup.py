# -*- coding: utf-8 -*-
#!/usr/bin/env python

from setuptools import setup, find_packages
import sys

version = '0.0.1'
classifiers = ["Development Status :: 5 - Production/Stable",
               "Environment :: Plugins",
               "Intended Audience :: Developers",
               "Programming Language :: Python",
               "Programming Language :: Python :: 2.7",
               "Programming Language :: Python :: 3",
               "Programming Language :: Python :: 3.4",
               "Programming Language :: Python :: Implementation :: PyPy",
               "License :: OSI Approved :: Apache Software License",
               "Topic :: Software Development :: Testing"]

if sys.version_info >= (2, 7):
    install_requires = ["requests>=2.7.9", "coverage"]
else:
    install_requires = ["requests>=2.7.9", "coverage", "argparse"]

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='Bookya Scraper Microservice',
    version='0.1.0',
    description='Microservice thet work as a scraper for Bookya.',
    long_description=readme,
    author='Bookya Team',
    author_email='hello@bookya.com',
    url='https://github.com/bookyacom/automation',
    license=license,
    packages=find_packages(exclude=('tests', 'docs', 'lib'))
)
