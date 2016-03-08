#! -*- coding: utf8 -*-
from distutils.core import setup

setup(
    name='redacted',
    version='0.0.1',
    description=u'Prevent printing your secrets',
    long_description=open('README.rst').read(),
    author=u'Joaquín Sorianello',
    url='https://github.com/joac/redacted',
    packages=['redacted'],
    license='LICENSE.md',
    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Spanish',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Development Status :: 5 - Production/Stable',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities'
    ],
)
