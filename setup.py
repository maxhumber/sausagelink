#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(
    name='sausagelink',
    version='1.0',
    description='Like BlockChain But Tastier™️',
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7'
    ],
    url='https://github.com/maxhumber/sausagelink',
    author='Max Humber',
    author_email='max.humber@gmail.com',
    license='MIT',
    packages=['sausagelink'],
    python_requires='>=3.6',
    setup_requires=['setuptools>=38.6.0']
)
