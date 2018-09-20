import setuptools

from pathlib import Path
from setuptools import find_packages

setuptools.setup(
    name='mutpos2vcf',
    version='0.1.0',
    author='clintval',
    author_email='valentine.clint@gmail.com',
    description='An Illumina Sample Sheet parsing library',
    url='https://github.com/clintval/mutpos2vcf',
    download_url='https://github.com/clintval/mutpos2vcf/archive/v0.8.0.tar.gz',
    long_description=Path('README.md').read_text(),
    long_description_content_type='text/markdown',
    license='MIT',
    zip_safe=True,
    packages=find_packages(),
    install_requires=['click', 'pyfaidx'],
    scripts=['mutpos2vcf'],
    keywords='duplex sequencing mutpos vcf variants mutagenesis mutation',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    project_urls={
        'Documentation': 'https://github.com/clintval/mutpos2vcf/',
        'Issue-Tracker': 'https://github.com/clintval/mutpos2vcf/issues',
    },
)
