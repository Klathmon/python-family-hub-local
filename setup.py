#!/usr/bin/env python3

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

if sys.argv[-1] == 'publish':
    os.system('python3 setup.py sdist upload')
    sys.exit()

license = """
MIT License
Copyright (c) 2018 Gregory Benner
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

setup(name='python-family-hub-local',
      version='0.0.2',
      description='Python API for accessing information from Samsung FamilyHub fridges locally.',
      url='https://github.com/Klathmon/python-family-hub-local',
      download_url='https://github.com/Klathmon/python-family-hub-local/archive/0.0.2.tar.gz',
      author='Gregory Benner',
      author_email='gregbenner1@gmail.com',
      license='MIT',
      install_requires=['aiohttp', 'async_timeout', 'pillow'],
      packages=['pyfamilyhublocal'],
      zip_safe=True)
