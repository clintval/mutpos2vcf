# mutpos2vcf

[![Testing Status](https://travis-ci.org/clintval/mutpos2vcf.svg?branch=master)](https://travis-ci.org/clintval/mutpos2vcf)
[![Code Coverage](https://codecov.io/gh/clintval/mutpos2vcf/branch/master/graph/badge.svg)](https://codecov.io/gh/clintval/mutpos2vcf)
[![PyPi Release](https://badge.fury.io/py/mutpos2vcf.svg)](https://badge.fury.io/py/mutpos2vcf)
[![License](https://img.shields.io/pypi/l/mutpos2vcf.svg)](https://github.com/clintval/mutpos2vcf/blob/master/LICENSE)
[![Python Versions](https://img.shields.io/pypi/pyversions/mutpos2vcf.svg)](https://pypi.python.org/pypi/mutpos2vcf/)
[![MyPy Checked](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)

Script to convert Duplex Sequencing `.mutpos` file formats into valid VCF files.

```bash
❯ pip install git+git@github.com:clintval/mutpos2vcf.git
```

Features:

- Convert [Loeb Lab](https://github.com/loeblab/Duplex-Sequencing) Duplex Sequencing `.mutpos` files to valid VCF (`v4.2`)
- Safely avoid many bugs that are known to exist in the original `.mutpos` format
