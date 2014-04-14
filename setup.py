# -*- coding: utf-8 -*-
"""Python packaging."""
import os
import sys

from setuptools import setup


#: Absolute path to directory containing setup.py file.
here = os.path.abspath(os.path.dirname(__file__))
#: Boolean, ``True`` if environment is running Python version 2.
IS_PYTHON2 = sys.version_info[0] == 2


NAME = 'hospital'
DESCRIPTION = 'Framework around health checks, smoke tests and diagnoses: ' \
              'monitor your applications and services at runtime.'
README = open(os.path.join(here, 'README.rst')).read()
VERSION = open(os.path.join(here, 'VERSION')).read().strip()
AUTHOR = u'Benoît Bryon'
EMAIL = u'benoit@marmelune.net'
URL = 'https://{name}.readthedocs.org/'.format(name=NAME)
CLASSIFIERS = [
    'Development Status :: 3 - Alpha',
    'License :: OSI Approved :: BSD License',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.3',
]
KEYWORDS = [
    'diagnosis',
    'healthcheck',
    'monitoring',
    'probe',
    'smoketest',
    'supervision',
    'testing',
]
PACKAGES = [NAME.replace('-', '_')]
REQUIREMENTS = [
    'setuptools>=0.7',
    'requests',
    'six',
]
if IS_PYTHON2:
    REQUIREMENTS.extend(['mock'])
ENTRY_POINTS = {
    'console_scripts': [
        'hospital-cli = hospital.cli:main',
        'hospital-serve = hospital.wsgi:main',
    ],
}


if __name__ == '__main__':  # Don't run setup() when we import this module.
    setup(name=NAME,
          version=VERSION,
          description=DESCRIPTION,
          long_description=README,
          classifiers=CLASSIFIERS,
          keywords=' '.join(KEYWORDS),
          author=AUTHOR,
          author_email=EMAIL,
          url=URL,
          license='BSD',
          packages=PACKAGES,
          include_package_data=True,
          zip_safe=False,
          install_requires=REQUIREMENTS,
          entry_points=ENTRY_POINTS)
