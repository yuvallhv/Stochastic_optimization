from distutils.core import setup, Extension

module = Extension("patience_sort_alg", sources = ["patienceSortingModule.c"])
setup(name="PackageName",
	version="1.0",
	description="patience_sort_alg package",
	ext_modules=[module])

