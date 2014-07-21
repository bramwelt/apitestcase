from os import path

from setuptools import setup
from distutils.command.clean import clean
from distutils.dir_util import remove_tree

import apitestcase

class CustomCleanCommand(clean):
    """
    Customized clean method that removes 'dist' and 'build' directories.
    """

    def run(self):
        clean.run(self)
        if path.exists('dist'):
            remove_tree('dist')
        if path.exists('build'):
            remove_tree('build')

setup(
    name="apitestcase",
    description="An integration test suite for HTTP APIs",
    url="https://github.com/bramwelt/apitestcase",
    version=".".join(apitestcase.__version__),
    author="Trevor Bramwell",
    author_email="trevor@bramwell.net",
    packages=['apitestcase'],
    license="MIT",
    install_requires=['requests'],
    long_description=open("README.rst").read(),
    test_suite="test",
    cmdclass={'clean': CustomCleanCommand},
)
