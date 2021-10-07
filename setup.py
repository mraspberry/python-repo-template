"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')
pkgname = (here / 'PKGNAME').read_text(encoding='utf-8')
ver = (here / 'VERSION').read_text(encoding='utf-8').strip()
desc = (here / 'DESC').read_text(encoding='utf-8').strip()
source_url = f'https://github.com/mraspberry/{pkgname}', 

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name=pkgname,
    version=ver,
    description=desc,
    long_description=long_description,
    long_description_content_type='text/markdown',
    url=f'https://github.com/mraspberry/{pkgname}', 
    author='Matthew Raspberry',
    author_email='3092450+mraspberry@users.noreply.github.com',
    packages=find_packages(),
    python_requires='>=3.6, <4',
    entry_points={
        'console_scripts': [
            f'{pkgname}={pkgname}.__main__:main',
        ],
    },
    project_urls={
        'Source': source_url,
    },
)
