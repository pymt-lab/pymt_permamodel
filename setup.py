#! /usr/bin/env python
import os
import sys

import numpy as np
import versioneer
from setuptools import find_packages, setup

from distutils.extension import Extension

from model_metadata.utils import get_cmdclass, get_entry_points


packages = find_packages()
pymt_components = [
    ("Ku=pymt_permamodel.bmi:Ku", "meta/Ku"),
    ("FrostNumber=pymt_permamodel.bmi:FrostNumber", "meta/FrostNumber"),
]

setup(
    name="pymt_permamodel",
    author="Eric Hutton",
    description="PyMT plugin permamodel",
    version=versioneer.get_version(),
    packages=packages,
    cmdclass=get_cmdclass(pymt_components, cmdclass=versioneer.get_cmdclass()),
    entry_points=get_entry_points(pymt_components),
)
