from os.path import join, dirname

from setuptools import setup, find_packages

from pbrf import api


setup(
    name='pbrf',
    version=api.__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    author='Rebranch',
    url='https://github.com/rebranch/python-pbrf',
)