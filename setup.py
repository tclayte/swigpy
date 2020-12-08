!/usr/bin/env python

"""
adapted from http://www.swig.org/Doc1.3/Python.html
"""

from distutils.core import setup, Extension


greet_module = Extension('_greet',
                           sources=['greet_wrap.cxx', 'greet.cpp'],
                           )

setup (name = "greet",
       version = "0.1",
       author      = "tct",
       description = """first swig compilation""",
       ext_modules = [greet_module],
       py_modules = ["greet"],
       )

