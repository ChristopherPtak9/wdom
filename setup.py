#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os import path

from setuptools import setup

readme_file = path.join(path.dirname(path.abspath(__file__)), 'README.rst')
with open(readme_file) as readme_file:
    readme = readme_file.read()

install_requires = ['tornado']
tests_require = ['parameterized', 'selenium', 'syncer']


setup(
    name='wdom',
    version='0.2.0',
    description='GUI library for browser-based desktop applications',
    long_description=readme,
    author='Hiroyuki Takagi',
    author_email='miyako.dev@gmail.com',
    url='https://github.com/miyakogi/wdom',
    packages=[
        'wdom',
        'wdom.examples',
        'wdom.server',
        'wdom.tests',
        'wdom.themes',
    ],
    include_package_data=True,
    license="MIT",
    zip_safe=False,
    keywords='dom browser gui ui',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    python_requires='>=3.5.2',
    install_requires=install_requires,
    tests_require=tests_require,
    test_suite='wdom.tests',
)
