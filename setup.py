#!/usr/bin/env python

# ./setup.py sdist bdist_wheel

from setuptools import setup
import sys
sys.path[:0] = ['lib']
from pensando.api import __version__

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='pen-python',
    version=__version__,
    author='Edward Arcuri',
    author_email='edward@pensando.io',
    description='API abstractions for Pensando PSM & DSCs',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://github.com/punisherVX/pen-python',
    classifiers=[
        'Development Status :: 1 - Planning'
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    package_dir={'': 'lib'},
    packages=[
        'pen',
        'pen/psmapi',
        'pen/dscapi'
    ],
    scripts=[],
)
