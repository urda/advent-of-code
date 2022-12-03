# Advent of Code

https://adventofcode.com/

# Environment

- Language of choice: `Python 3.11`
- Built on: macOS `Ventura 13.0`
  - Using Apple `M1 Max`
- Using: PyCharm Professional Edition `2022.2.4`
- With supporting tools:
  - git `2.38.1`
  - iTerm2 `3.4.18`

Versions are tracked in their respective `requirements` file.

- [`flake8`](https://pypi.org/project/flake8/)
- [`ipython`](https://pypi.org/project/ipython/)
- [`pylint`](https://pypi.org/project/pylint/)
- [`pytest`](https://pypi.org/project/pytest/)
- [`pytest-cov`](https://pypi.org/project/pytest-cov/)

# Environment Setup

**The following instructions are designed around `pyenv`, `pyenv-virtualenv`.**

Prepare the base python:

```bash
pyenv install 3.11.0
```

Create a python virtual environment:

```bash
pyenv virtualenv 3.11.0 advent
```

Switch to it after creation:

```bash
pyenv shell advent
```

Go ahead and update `pip`:

```bash
pip install --upgrade pip
```

And install the development requirements:

```bash
pip install -r requirements-dev.txt
```

# Running the "project"

You can launch the `advent-of-code` project with:

```bash
make run
```

# Running the "utilities"

You can launch the project utilities with:

```bash
make utils
```

## Henry Plate Builder - `HPB`

The `HPB` can be used to pre-stage an advent day:

```bash
[HPB]

Enter an advent day number: 1
~~~ Will use value '1' ~~~

This operation is ** D E S T R U C T I V E ** are you sure ?
Enter "Y" to continue, anything else quits: Y

OK I warned you.

Creating directory "/path/to/src/advent_days/day_01" ...
Creating "/path/to/src/advent_days/day_01/__init__.py" ...
Creating "/path/to/src/advent_days/day_01/day_01.py" ...
Creating "/path/to/tests/advent_days/test_day_01.py" ...
Updating "/path/to/src/advent_days/__init__.py" ...
Updating "/path/to/src/main.py" ..
```

After which you can just do:

```bash
git add .

git commit -m "[Day XX] Pre-stage"  # Where XX is your Day number 01-25
```

# Advent Days

- Day 01
  - [Docs](https://github.com/urda/advent-of-code/blob/master/docs/day_01.md)
  - [Code](https://github.com/urda/advent-of-code/tree/master/src/advent_days/day_01)
- Day 02
  - [Docs](https://github.com/urda/advent-of-code/blob/master/docs/day_02.md)
  - [Code](https://github.com/urda/advent-of-code/tree/master/src/advent_days/day_02)
- Day 03
  - [Docs](https://github.com/urda/advent-of-code/blob/master/docs/day_03.md)
  - [Code](https://github.com/urda/advent-of-code/tree/master/src/advent_days/day_03)

## Advent Day Answers

- See [the `docs/answers/README` file](https://github.com/urda/advent-of-code/blob/master/docs/answers/README.md)
