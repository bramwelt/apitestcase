from setuptools import setup

import apitestcase

setup(
    name="apitestcase",
    description="An integration test suite for HTTP APIs",
    version=".".join(apitestcase.__version__),
    author="Trevor Bramwell",
    author_email="trevor@bramwell.net",
    packages=['apitestcase'],
    license="MIT",
    install_requires=['requests'],
    long_description=open("README.rst").read(),
    test_suite="test",
)
