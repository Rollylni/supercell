#!/usr/bin/env python

""" Python library for working with supercellAPI
"""

from setuptools import setup
import supercel

setup(
    name="supercel",
    version=supercel.__version__,
    author="RoLLy",
    author_email="dimadersekt@gmail.com",
    description=__doc__,
    license=supercel.__license__,
    url="https://github.com/Rollylni/supercell",
    packages=["supercel"],
    keywords="supercel",
    test_suite="tests",
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Operating System :: POSIX :: Linux',
        'Operating System :: Unix',
        'Intended Audience :: Developers',
        'Natural Language :: English'
    ]
)