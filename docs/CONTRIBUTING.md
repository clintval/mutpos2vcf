# How to Contribute

The complete test suite is configured through `Tox`:

```bash
❯ cd mutpos2vcf
❯ pip install tox
❯ tox
```

List all environments with:

```
❯ tox -av
using tox.ini: .../mutpos2vcf/tox.ini
using tox-3.1.2 from ../tox/__init__.py
default environments:
py36      -> run the test suite with (basepython)
py36-lint -> check the code style
py36-type -> type check the library
docs      -> test building of HTML docs

additional environments:
dev       -> the official mutpos2vcf development environment
```

To run just one environment:

```bash
❯ tox -e py36
```

To build and activate a development virtual environment:

```bash
❯ tox -e dev
❯ source venv/bin/activate
```

To build the documentation:

```bash
❯ tox -e py36-docs
❯ open .tox/docs/_build/index.html
```

To pass in positional arguments to a specified environment:

```bash
❯ tox -e py36 -- -x tests/test_mutpos2vcf.py
```
