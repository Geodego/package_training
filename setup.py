from setuptools import setup, find_packages
from version import find_version


setup(
    name='package_training',
    version=find_version("package_training", "__init__.py"),
    license='proprietary',
    description='Example of managing packages using conda',
    author='Me',
    packages=find_packages(),
    #package_dir={'': 'package_training'},
)
