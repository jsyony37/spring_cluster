#!/usr/bin/evn python

from distutils.core import setup
from Cython.Build import cythonize

#setup(ext_modules=cythonize("find_nonzero_highdim.pyx"))
setup(ext_modules=[Extension("find_nonzero_highdim", ["find_nonzero_highdim.pyx"],extra_compile_args=['-fstack-protector'])])
