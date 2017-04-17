from sqlg import __version__
from setuptools import setup

setup(
    name='sqlg',
    version='0.0',
    author='Raja Simon',
    author_email='rajasimon@icloud.com',
    packages=['sqlg'],
    include_package_data=True,
    entry_points={'console_scripts': [
        'sqlg = sqlg.cli:CommandLineInterface.entrypoint',
    ]},
)
