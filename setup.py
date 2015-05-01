#!/usr/bin/env python

"""
distutils/setuptools install script.
"""
import os
import re
#import sys

from setuptools import setup, find_packages


ROOT = os.path.dirname(__file__)
VERSION_RE = re.compile(r'''__version__ = ['"]([0-9.]+)['"]''')


requires = [
    'yieldfrom.botocore>=0.1.4,<0.2.0',
    #'bcdoc==0.12.2',
    'jmespath>=0.6.2,<1.0.0',
]


# def get_version():
#     init = open(os.path.join(ROOT, 'boto3', '__init__.py')).read()
#     return VERSION_RE.search(init).group(1)


setup(
    name='yieldfrom.boto3',
    version='0.1.5',
    description='asyncio port of boto3, the The AWS SDK for Python',
    long_description=open('README.rst').read(),

    author='Amazon Web Services',
    maintainer='David Keeney',
    maintainer_email='dkeeney@rdbhost.com',

    url='https://github.com/rdbhost/yieldfromBoto3',
    scripts=[],
    packages=find_packages(exclude=['tests*']),
    package_data={'': ['LICENSE', 'NOTICE'],
                  'yieldfrom.boto3': ['data/*.json', 'data/resources/*.json']},
                  #'yieldfrom': ['data/*.json', 'data/aws/*.json']},

    package_dir={'yieldfrom': 'yieldfrom'},
    include_package_data=True,
    namespace_packages=['yieldfrom'],
    install_requires=requires,
    license="Apache License 2.0",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
)
