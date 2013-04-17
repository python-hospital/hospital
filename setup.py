# -*- coding: utf-8 -*-
"""Python packaging."""
import os
from setuptools import setup


def read_relative_file(filename):
    """Returns contents of the given file, which path is supposed relative
    to this module."""
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        return f.read().strip()


NAME = 'hospital'
README = read_relative_file('README')
VERSION = read_relative_file('VERSION')
PACKAGES = ['hospital']
REQUIRES = ['setuptools']


if __name__ == '__main__':  # Don't run setup() when we import this module.
    setup(name=NAME,
          version=VERSION,
          description='Health checks and supervision/monitoring libraries.',
          long_description=README,
          classifiers=['Development Status :: 3 - Alpha',
                       'License :: OSI Approved :: BSD License',
                       'Programming Language :: Python :: 2.7',
                       'Programming Language :: Python :: 2.6',
                       ],
          keywords='test unittest diagnosis healthcheck supervision '
                   'monitoring',
          author='Benoît Bryon',
          author_email='benoit@marmelune.net',
          url='https://github.com/python-hospital/%s' % NAME,
          license='BSD',
          packages=PACKAGES,
          include_package_data=True,
          zip_safe=False,
          install_requires=REQUIRES,
          )
