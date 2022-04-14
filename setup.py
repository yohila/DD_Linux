from setuptools.command.build_ext import build_ext
from setuptools import Extension, setup, find_packages

import os, sys
import platform



setup(
    	name="depth",
   	version="1.0.0",
    	author="Pavlo mozharovskyi",
    	author_email="pavlo.mozharovskyi@telecom-paris.fr",
   	description="The package provides many procedures for calculating the depth of points in an empirical distribution for many notions of data depth",
   	long_description="The package provides many procedures for calculating the depth of points in an empirical distribution for many notions of data depth",
   	long_description_content_type="text/markdown",
   	url="https://github.com/pypa",
   	platforms='linux',
    	packages=find_packages(),
    	ext_modules=[
        
   	 ],
    	include_package_data=True,
  	package_data={"depth": ['ddalpha.so','depth_wrapper.so']},
   	zip_safe=False,
	)





	
