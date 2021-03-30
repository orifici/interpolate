#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

setup(
    name='interpolate',
    version='0.0.1',
    description='A python package to interpolate missing matrix elements',
    long_description=readme,
    url='https://internal-bb-repo.com/interpolate',
    author='Lorenzo Orifici',
    author_email='lorenzo.orifici@noreply.com',
    license='MIT License',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'interpolate=interpolate.interpolate:main',
        ],
    },
    install_requires=[],
    test_suite='tests',
    setup_requires=['pytest-runner'],
    tests_require=['setuptools', 'pytest', 'mock', 'tox'],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Engineers',
        'License :: Internal',
        'Operating System :: Linux',
        'Programming Language :: Python :: 3',
    ],
)
