
from setuptools import setup, find_namespace_packages

setup(
    name='openrouter_exception_handler',
    packages=find_namespace_packages(where='openrouter_exception_handler/', include=['openrouter_exception_handler.exception_handler']),
    package_dir={'': 'openrouter_exception_handler'},
)