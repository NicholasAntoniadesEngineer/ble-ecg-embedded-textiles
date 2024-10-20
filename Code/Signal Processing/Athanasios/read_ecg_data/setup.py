#!/usr/bin/env python

import os
import sys
from setuptools import setup, find_packages


setup(
    name="kymira_data_in",
    version="0.0.1",
    description="Kymira ECG data retrieval algorithms",
    long_description=open("README.md").read(),
    author="Athanasios Anastasiou, Soma Chakrabotry",
    author_email="a.anastasiou@kymira.co.uk",
    zip_safe=True,
    url='',
    packages=["kymira_data_in", ],
    scripts=["kymira_data_in/clouddb_import.py"],
    setup_requires=["pytest-runner"] if any(x in ("pytest", "test") for x in sys.argv) else [],
    tests_require=["pytest"],
    install_requires=["sphinx", "numpyencoder", "pandas", "numpy", "pymongo", "click"],
    classifiers=["Development Status :: 4 - Beta",
                 "Topic :: Scientific/Engineering",
                 "Topic :: Software Development :: Libraries :: Python Modules",
                 "Intended Audience :: Science/Research",
                 "Natural Language :: English",
                 "Programming Language :: Python :: 3",
                 ]
    )
