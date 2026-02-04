"""Setup for pumukit XBlock."""


import os
import re

from setuptools import setup


def package_data(pkg, roots):
    """Generic function to find package_data.

    All of the files under each of the `roots` will be declared as package
    data for package `pkg`.

    """
    data = []
    for root in roots:
        for dirname, _, files in os.walk(os.path.join(pkg, root)):
            for fname in files:
                data.append(os.path.relpath(os.path.join(dirname, fname), pkg))

    return {pkg: data}


def get_version(file_path):
    """
    Extract the version string from the file at the given relative path fragments.
    """
    filename = os.path.join(os.path.dirname(__file__), file_path)
    with open(filename, encoding='utf-8') as opened_file:
        version_file = opened_file.read()
        version_match = re.search(r"(?m)^__version__ = ['\"]([^'\"]+)['\"]", version_file)
    if version_match:
        return version_match.group(1)
    raise RuntimeError('Unable to find version string.')


VERSION = get_version("pumukit/__init__.py")


setup(
    name='pumukit-xblock',
    version=VERSION,
    author='Teltek Video Research',
    author_email='info@teltek.es',
    description='Pumukit platform XBlock for openedx',
    license='AGPLv3',
    packages=[
        'pumukit',
    ],
    install_requires=[
        'XBlock',
    ],
    entry_points={
        'xblock.v1': [
            'pumukit = pumukit:PumukitXBlock',
        ]
    },
    package_data=package_data("pumukit", ["static", "public"]),
)
