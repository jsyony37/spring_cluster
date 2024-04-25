#!/usr/bin/evn python

from distutils.core import setup
from distutils.extension import Extension

# from setuptools import setup
# from setuptools.extension import Extension


USE_CYTHON = "auto"
# USE_CYTHON = True
# USE_CYTHON = False

filename = "prepare_sym"

if USE_CYTHON == True or USE_CYTHON == "auto":
    try:
        from Cython.Build import cythonize

        USE_CYTHON = True
    except ImportError:
        if USE_CYTHON == "auto":
            USE_CYTHON = False
        else:
            print("WARNING, no cython detected, defaulting to .c")
            print()
            USE_CYTHON = False


if USE_CYTHON:
    #    extensions = [
    #        Extension(
    #            filename,                    # Module name
    #            sources=[filename+".pyx"],      # Cython source file
    #            extra_compile_args=["-I/Users/cpark21/miniconda3/lib/python3.9/site-packages/numpy/core/include"],  # Include path to NumPy's header files
    #        )
    #    ]
    #    setup(ext_modules=cythonize(extensions))
    setup(ext_modules=cythonize(filename + ".pyx"))
else:
    print("COMPILING C VERSION")
    setup(ext_modules=[Extension(filename, [filename + ".c"])])


# done
