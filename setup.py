#!/usr/bin/env python
# -*- coding: utf-8 -*-\

from setuptools import find_packages
from setuptools.command.test import test as TestCommand
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
    # TODO: put package requirements here
]

test_requirements = ['tox']


class Tox(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import tox
        errcode = tox.cmdline(self.test_args)
        sys.exit(errcode)


setup(
    name='fibonacci',
    version='0.1.0',
    description="A minimal python project for integration test purposes.",
    long_description=readme + '\n\n' + history,
    author="Maik Figura",
    author_email='maiksensi@gmail.com',
    url='https://github.com/maiksensi/fibonacci',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    install_requires=requirements,
    cmdclass={'test': Tox},
    license="BSD",
    zip_safe=False,
    keywords='fibonacci',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
