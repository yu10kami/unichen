# Author: Yuto Kamiwaki <yutokamiwaki@gmail.com>
# Copyright (c) 2023 Yuto Kamiwaki
# Released under the MIT license
# https://opensource.org/license/mit/

from setuptools import setup
import unichen

DESCRIPTION = 'unichen: Unit conversion library for Japanese Yen'
NAME = 'unichen'
AUTHOR = 'Yuto Kamiwaki'
AUTHOR_EMAIL = 'yutokamiwaki@gmail.com'
URL = 'https://github.com/yu10kami/unichen'
LICENSE = 'MIT'
DOWNLOAD_URL = 'https://github.com/yu10kami/unichen'
VERSION = unichen.__version__
PYTHON_REQUIRES = '>=3.6'

INSTALL_REQUIRES = [
]

PACKAGES = [
    'unichen'
]

CLASSIFIERS = [
    'Intended Audience :: Financial and Insurance Industry',
    'Intended Audience :: Science/Research',
    'Intended Audience :: Information Technology',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3 :: Only',
    'Topic :: Scientific/Engineering',
    'Topic :: Scientific/Engineering :: Mathematics',
    'Topic :: Scientific/Engineering :: Artificial Intelligence',
    'Natural Language :: Japanese',
]

with open('README.md', 'r') as fp:
    readme = fp.read()
with open('CONTACT.txt', 'r') as fp:
    contacts = fp.read()
long_description = readme + '\n\n' + contacts


setup(name=NAME,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      maintainer=AUTHOR,
      maintainer_email=AUTHOR_EMAIL,
      description=DESCRIPTION,
      long_description=long_description,
      license=LICENSE,
      url=URL,
      version=VERSION,
      download_url=DOWNLOAD_URL,
      python_requires=PYTHON_REQUIRES,
      install_requires=INSTALL_REQUIRES,
      packages=PACKAGES,
      classifiers=CLASSIFIERS
)