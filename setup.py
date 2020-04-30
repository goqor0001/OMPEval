from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize

examples_extension = Extension(
    name="pyomp",
    sources=["pyomp.pyx"],
    libraries=["ompeval"],
    library_dirs=["lib"],
    include_dirs=["lib"]
)
setup(
    name="pyomp",
    ext_modules=cythonize([examples_extension], language="c++")
)
