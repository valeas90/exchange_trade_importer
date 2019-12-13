"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open(path.join(here, 'VERSION.txt'), encoding='utf-8') as f:
    version = f.read()

setup(
    name='exchange_trade_importer',
    version=version,
    description='No description yet',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/valeas90/exchange_trade_importer',
    author='Jhon Company',
    author_email='jonvaleas@gmail.com',
    packages=find_packages(include=['src.exchange_trade_importer']),
    package_dir = {'': 'src'},
    python_requires='>=3.7',
    entry_points={
        'console_scripts': [
            'exchange_trade_importer=exchange_trade_importer:main',
        ],
    },
    project_urls={
        'Source': 'https://github.com/valeas90/exchange_trade_importer/',
    },
)
