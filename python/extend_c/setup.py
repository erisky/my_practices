from setuptools import setup, Extension
setup(
    name='sample',
    version='1.0',
    description='Python Package with Hello World C Extension',
    ext_modules=[
        Extension(
            'sample',
            sources=['samplemodule.c'],
            py_limited_api=True)
    ],
)
