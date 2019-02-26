#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup
import os

with open('README.md') as f:
    long_description = f.read()

setup(
    name='sausagelink',
    version='1.5.2',
    description='Like Blockchain But Tastier™️',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Topic :: Database',
        'Topic :: Security',
        'Topic :: Security :: Cryptography'
    ],
    keywords=[
        'blockchain', 'ledger', 'sha256'
    ],
    url='https://github.com/maxhumber/sausagelink',
    author='Max Humber',
    author_email='max.humber@gmail.com',
    license='MIT',
    packages=['sausagelink'],
    python_requires='>=3.6',
    setup_requires=['setuptools>=38.6.0']
)
