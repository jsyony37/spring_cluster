#!/usr/bin/evn python

from distutils.core import setup
from Cython.Build import cythonize

#setup(ext_modules=cythonize("run_montecarlo.pyx"))
setup(ext_modules=[Extension("run_montecarlo", ["run_montecarlo.pyx"],extra_compile_args=['-fstack-protector'])])
