# -*- coding: utf-8 -*-
import sys
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

sys.path.insert(0, '.')
from mynewpythonthing import __version__


setup(
    name="mynewpythonthing",
    version=__version__,
    description="Flask based microservice.",
    maintainer="",
    packages=["mynewpythonthing", "mynewpythonthing.myapp"],
    platforms=["any"]
)
