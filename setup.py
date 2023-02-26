import sys
import os
import pathlib
from setuptools import setup, find_packages

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='',
    version='0.0.1',
    description='',
    author='Jon Robinson',
    author_email='jonrobinson1980@gmail.com',
    long_description=long_description,
    long_description_content_type='text/markdown', 
    license='',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Scientific/Engineering',
    ], 
    packages=find_packages(),
    python_requires='>=3.5',
    url=''
)