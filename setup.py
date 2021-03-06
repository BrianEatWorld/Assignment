#! /usr/bin/python
from os.path import join
from os import walk
from setuptools import setup, find_packages


def get_package_data(dir):
    root = 'assignment/'
    paths = [p.replace(root, '') for p, _, f in walk(root + dir) if f]
    extensions = ['html', 'js', 'css', 'less', 'xml', 'txt', 'png', 'jpg', 'jpeg', 'gif']
    return [join(path, '*.' + ext) for path in paths for ext in extensions]

setup(name='Assignment',
      version='0.1',
      description='assignment for QA/S I/II',
      author='Brian Dorn',
      author_email='bdorn@rmn.com',
      packages=find_packages(),
      package_data={'assignment': get_package_data('semanticUIDocs')},
      install_requires=['tornado', ],
      tests_require=['requests', 'pytest', 'selenium', ],
      entry_points={'console_scripts': ['start-tornado = assignment.basic:start_tornado']},
      )
