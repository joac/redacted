#! -*- coding: utf8 -*-
from __future__ import print_function

from distutils.core import setup
from distutils.extension import Extension

USE_CYTHON = False

try:
    from Cython.Build import cythonize
except ImportError:
    print("Cython not available, using pregenerated C files")  # noqa
else:
    USE_CYTHON = True

ext = 'pyx' if USE_CYTHON else 'c'

extensions = [
    Extension("*", ["**/*.{}".format(ext)]),
]

if USE_CYTHON:
    extensions = cythonize(extensions)

setup(
    name='redacted',
    version='0.0.1',
    description=u'Prevent printing your secrets',
    long_description=open('README.rst').read(),
    author=u'Joaquín Sorianello',
    url='https://github.com/joac/redacted',
    packages=['redacted'],
    license='LICENSE.md',
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: Spanish',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Development Status :: 5 - Production/Stable',
        'Topic :: Software Development :: Libraries',
        'Topic :: Utilities'
    ],
    ext_modules=extensions,
)
