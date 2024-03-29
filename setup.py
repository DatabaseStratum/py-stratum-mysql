from codecs import open
from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='PyStratum-MySQL',

    version='1.2.0',

    description='PyStratum-MySQL: MySQL & MariaDB Backend',
    long_description=long_description,

    url='https://github.com/DatabaseStratum/py-stratum-mysql',

    author='Set Based IT Consultancy',
    author_email='info@setbased.nl',

    license='MIT',

    classifiers=[
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Topic :: Software Development :: Code Generators',
        'Topic :: System :: Installation/Setup',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],

    keywords='PyStratum, MySql, MariaDB',

    packages=find_packages(exclude=['build', 'test']),

    install_requires=['mysql-connector-python<9, >=8.0.22',
                      'PyStratum-Backend<2, >=1.0.2',
                      'PyStratum-Common<2, >=1.1.1',
                      'PyStratum-Middle<2, >=1.0.0']
)
