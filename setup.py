#!/usr/bin/env python
# Copyright (c) 2020, Pensando Systems
#
# Permission to use, copy, modify, and/or distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notice and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND THE AUTHOR DISCLAIMS ALL WARRANTIES
# WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF
# MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE FOR
# ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES
# WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN AN
# ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF
# OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.
# Author(s): Ryan Tischer ryan@pensando.io
#            Edward Arcuri edward@pensando.io
#
#

import sys
from setuptools import setup
sys.path[:0] = ['lib']
from pensando.__init__ import __version__

with open('README.rst') as f:
    long_description = f.read()

setup(
    name='pensando-python',
    version=__version__,
    author='Edward Arcuri',
    author_email='edward@pensando.io',
    description='API abstractions for Pensando PSM & DSCs',
    long_description=long_description,
    long_description_content_type='text/x-rst',
    url='https://gitlab.com/Pensando/pen-python',
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
        'pensando',
        'pensando/psmapi',
        'pensando/dscapi'
    ],
    include_package_data=True,
    install_requires=['requests'],
    scripts=[],
)
