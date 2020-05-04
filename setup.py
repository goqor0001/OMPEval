from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
from Cython.Distutils import build_ext


class PreInstall(build_ext):
    @staticmethod
    def script(directory):
        from subprocess import call
        call(['make'], cwd='.')

    def run(self):
        self.execute(PreInstall.script, (self.build_lib,), msg="Running pre install script")
        build_ext.run(self)


examples_extension = Extension(
    name="pyomp",
    sources=["pyomp.pyx"],
    libraries=["ompeval"],
    library_dirs=["lib"],
    include_dirs=["lib"]
)

setup(
    name="pyomp",
    ext_modules=cythonize([examples_extension]),
    cmdclass={
        'build_ext': PreInstall,    
    },
    version='0.0.1',
)

