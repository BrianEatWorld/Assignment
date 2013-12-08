#! /usr/bin/python
import os.path
from setuptools import setup,find_packages

install_requires = [
'tornado',
]

test_requires = [
'nose',
'selenium',
]

try:
	setup(name='assignment',
	      version='0.1',
	      description='assignment for QA/S I/II',
	      author='Brian Dorn',
	      author_email='bdorn@rmn.com',
	      packages=['assignment','tests',]
	      )

except:
	print("Couldn't find explicit packages, now searching")
	setup(name='assignment',
	      version='0.1',
	      description='assignment for QA/S I/II',
	      author='Brian Dorn',
	      author_email='bdorn@rmn.com',
	      packages= find_packages()
	      )