# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


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
