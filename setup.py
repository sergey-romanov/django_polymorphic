#!/usr/bin/env python
from setuptools import setup, find_packages
from os import path
import codecs
import os
import re
import sys


def read(*parts):
    file_path = path.join(path.dirname(__file__), *parts)
    return codecs.open(file_path, encoding='utf-8').read()


def find_version(*parts):
    version_file = read(*parts)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
    if version_match:
        return str(version_match.group(1))
    raise RuntimeError("Unable to find version string.")


setup(
    name = 'django_polymorphic',
    version = find_version('polymorphic', '__version__.py'),
    license = 'BSD',

    description = 'Seamless Polymorphic Inheritance for Django Models',
    long_description = read('README.rst'),
    url = 'https://github.com/sergey-romanov/django_polymorphic',

    author = 'Bert Constantin',
    author_email = 'bert.constantin@gmx.de',

    maintainer = 'Christopher Glass',
    maintainer_email = 'tribaal@gmail.com',

    include_package_data = True,

    packages = find_packages(),
    package_data = {
        'polymorphic': [
            'templates/admin/polymorphic/*.html',
        ],
    },

    install_requires=['setuptools'],
    test_suite='runtests',

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
