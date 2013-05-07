# -*- coding: utf-8 -*-
"""Utilities related to packaging.

This module may be packaged as a standalone library.

"""
import email.parser


def get_metadata(distribution):
    """Return metadata of installed ``distribution``, as a dictionary.

    >>> import pkg_resources
    >>> dist = pkg_resources.get_distribution('hospital')
    >>> from hospital.packaging import get_metadata
    >>> metadata = get_metadata(dist)
    >>> metadata['Name']
    ['hospital']
    >>> metadata['License']
    ['BSD']

    """
    raw_metadata = distribution.get_metadata(distribution.PKG_INFO)
    parsed_metadata = email.parser.Parser().parsestr(raw_metadata)
    metadata = {}
    for key, value in parsed_metadata.items():
        try:
            metadata[key].append(value)
        except KeyError:
            metadata[key] = [value]
    return metadata


def get_classifiers(distribution):
    """Return list of classifiers metadata of ``distribution``.

    >>> import pkg_resources
    >>> dist = pkg_resources.get_distribution('hospital')
    >>> from hospital.packaging import get_classifiers
    >>> get_classifiers(dist)
    ['Development Status :: 3 - Alpha', 'License :: OSI Approved :: BSD License', 'Programming Language :: Python :: 2.6', 'Programming Language :: Python :: 2.7', 'Programming Language :: Python :: Implementation :: CPython']

    """
    classifiers = get_metadata(distribution)['Classifier']
    classifiers.sort()
    return classifiers


def get_supported_python_versions(distribution):
    """Return list of supported Python version of ``distribution``.

    >>> import pkg_resources
    >>> dist = pkg_resources.get_distribution('hospital')
    >>> from hospital.packaging import get_supported_python_versions
    >>> get_supported_python_versions(dist)
    ['2.6', '2.7']

    """
    classifiers = get_classifiers(distribution)
    version_prefix = 'Programming Language :: Python :: '
    version_prefix_length = len(version_prefix)
    implementation_prefix = 'Programming Language :: Python :: Implementation'
    versions = [classifier[version_prefix_length:]
                for classifier in classifiers
                if classifier.startswith(version_prefix)
                and not classifier.startswith(implementation_prefix)]
    versions.sort()
    return versions


def supports_python_version(distribution, python_version):
    """Return True if ``distribution`` claims support of ``python_version``.

    >>> import pkg_resources
    >>> dist = pkg_resources.get_distribution('hospital')
    >>> from hospital.packaging import supports_python_version
    >>> supports_python_version(dist, '2.6')
    True
    >>> supports_python_version(dist, '2.5')
    False

    """
    return python_version in get_supported_python_versions(distribution)
