#!/usr/bin/env python

from setuptools import setup, find_packages

entry_points = {}
entry_points['console_scripts'] = ['onedataextractor=onedatacustom.metadataextractor:main']

setup(

    name='onedatacustom',

    version=1.2,

    packages=find_packages(),

    author="F.Gillardo",
	
    install_requires= ["h5pY","simplejson"],

    entry_points=entry_points,

)
