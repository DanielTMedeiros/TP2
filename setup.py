from setuptools import setup, Extension
from Cython.Build import cythonize

ext_modules = [
    Extension(
        "grupo5_q1",
        ["grupo5_q1.pyx"],
        extra_compile_args=['-fopenmp'],
        extra_link_args=['-fopenmp'],
    )
]

setup(
    name="grupo5_q1",
    ext_modules=cythonize(ext_modules),
)