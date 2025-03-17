from setuptools import setup, find_packages

# read the contents of your README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='openrouter_exception_handler',
    version='0.1.8',
    packages=find_packages(),
    install_requires=[
        'requests'
    ],
    author='Dannybombastic',
    description='handler for exceptions in python with openrouter.ai',
    url='https://github.com/tu_usuario/openrouter_exception_handler',
    long_description=long_description,
    long_description_content_type='text/markdown'
)
