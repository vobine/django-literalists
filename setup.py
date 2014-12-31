import os
from setuptools import setup

with open (os.path.join (os.path.dirname (__file__),
                         'README.md'),
           'rt') as readme:
    README = readme.read ()

# allow setup.py to be run from any path
os.chdir (
    os.path.normpath (
        os.path.join (os.path.abspath (__file__),
                      os.pardir ) ) )

setup (
    name='django-literalists',
    version='0.1',
    packages=['literalists'],
    include_package_data=True,
    license='BSD License',  # example license
    description='A web site for recreational literati.',
    long_description=README,
    url='http://www.literalists.org/',
    author='Hal Peterson',
    author_email='hrp@literalists.org',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Word geeks',
        'License :: MIT',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
