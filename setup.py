#! /usr/bin/env python
import os
import sys

import versioneer
from setuptools import find_packages, setup


packages = find_packages()
entry_points = {
    "pymt.plugins": [
        "Ku=pymt_permamodel.bmi:Ku",
        "FrostNumber=pymt_permamodel.bmi:FrostNumber",
    ]
}

setup(
    name="pymt_permamodel",
    author="Eric Hutton",
    description="PyMT plugin permamodel",
    version=versioneer.get_version(),
    packages=packages,
    cmdclass=versioneer.get_cmdclass(),
    entry_points=entry_points,
    include_package_data=True,
)
