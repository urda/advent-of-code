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
  - [Tests](https://github.com/urda/advent-of-code/blob/master/tests/advent_days/test_day_01.py)
- Day 02
  - [Docs](https://github.com/urda/advent-of-code/blob/master/docs/day_02.md)
  - [Code](https://github.com/urda/advent-of-code/tree/master/src/advent_days/day_02)
  - [Tests](https://github.com/urda/advent-of-code/blob/master/tests/advent_days/test_day_02.py)
- Day 03
  - [Docs](https://github.com/urda/advent-of-code/blob/master/docs/day_03.md)
  - [Code](https://github.com/urda/advent-of-code/tree/master/src/advent_days/day_03)
  - [Tests](https://github.com/urda/advent-of-code/blob/master/tests/advent_days/test_day_03.py)
- Day 04
  - [Docs](https://github.com/urda/advent-of-code/blob/master/docs/day_04.md)
  - [Code](https://github.com/urda/advent-of-code/tree/master/src/advent_days/day_04)
  - [Tests](https://github.com/urda/advent-of-code/blob/master/tests/advent_days/test_day_04.py)
- Day 05
  - [Docs](https://github.com/urda/advent-of-code/blob/master/docs/day_05.md)
  - [Code](https://github.com/urda/advent-of-code/tree/master/src/advent_days/day_05)
  - [Tests](https://github.com/urda/advent-of-code/blob/master/tests/advent_days/test_day_05.py)
- Day 06
  - [Docs](https://github.com/urda/advent-of-code/blob/master/docs/day_06.md)
  - [Code](https://github.com/urda/advent-of-code/tree/master/src/advent_days/day_06)
  - [Tests](https://github.com/urda/advent-of-code/blob/master/tests/advent_days/test_day_06.py)
- Day 07
  - [Docs](https://github.com/urda/advent-of-code/blob/master/docs/day_07.md)
  - [Code](https://github.com/urda/advent-of-code/tree/master/src/advent_days/day_07)
  - [Tests](https://github.com/urda/advent-of-code/blob/master/tests/advent_days/test_day_07.py)
- Day 08
  - [Docs](https://github.com/urda/advent-of-code/blob/master/docs/day_08.md)
  - [Code](https://github.com/urda/advent-of-code/tree/master/src/advent_days/day_08)
  - [Tests](https://github.com/urda/advent-of-code/blob/master/tests/advent_days/test_day_08.py)
- Day 09
  - [Docs](https://github.com/urda/advent-of-code/blob/master/docs/day_09.md)
  - [Code](https://github.com/urda/advent-of-code/tree/master/src/advent_days/day_09)
  - [Tests](https://github.com/urda/advent-of-code/blob/master/tests/advent_days/test_day_09.py)
- Day 10
  - [Docs](https://github.com/urda/advent-of-code/blob/master/docs/day_10.md)
  - [Code](https://github.com/urda/advent-of-code/tree/master/src/advent_days/day_10)
  - [Tests](https://github.com/urda/advent-of-code/blob/master/tests/advent_days/test_day_10.py)
- Day 11
  - [Docs](https://github.com/urda/advent-of-code/blob/master/docs/day_11.md)
  - [Code](https://github.com/urda/advent-of-code/tree/master/src/advent_days/day_11)
  - [Tests](https://github.com/urda/advent-of-code/blob/master/tests/advent_days/test_day_11.py)
- Day 12
  - [Docs](https://github.com/urda/advent-of-code/blob/master/docs/day_12.md)
  - [Code](https://github.com/urda/advent-of-code/tree/master/src/advent_days/day_12)
  - [Tests](https://github.com/urda/advent-of-code/blob/master/tests/advent_days/test_day_12.py)
- Day 13
  - [Docs](https://github.com/urda/advent-of-code/blob/master/docs/day_13.md)
  - [Code](https://github.com/urda/advent-of-code/tree/master/src/advent_days/day_13)
  - [Tests](https://github.com/urda/advent-of-code/blob/master/tests/advent_days/test_day_13.py)
- Day 14
  - [Docs](https://github.com/urda/advent-of-code/blob/master/docs/day_14.md)
  - [Code](https://github.com/urda/advent-of-code/tree/master/src/advent_days/day_14)
  - [Tests](https://github.com/urda/advent-of-code/blob/master/tests/advent_days/test_day_14.py)
- Day 15
  - [Docs](https://github.com/urda/advent-of-code/blob/master/docs/day_15.md)
  - [Code](https://github.com/urda/advent-of-code/tree/master/src/advent_days/day_15)
  - [Tests](https://github.com/urda/advent-of-code/blob/master/tests/advent_days/test_day_15.py)
- Day 16
  - [Docs](https://github.com/urda/advent-of-code/blob/master/docs/day_16.md)
  - [Code](https://github.com/urda/advent-of-code/tree/master/src/advent_days/day_16)
  - [Tests](https://github.com/urda/advent-of-code/blob/master/tests/advent_days/test_day_16.py)

## Advent Day Answers

- See [the `docs/answers/README` file](https://github.com/urda/advent-of-code/blob/master/docs/answers/README.md)
