# Advent of Code

https://adventofcode.com/

# Years

- [2022](https://github.com/urda/advent-of-code/blob/master/years/2022/README.md)
  - [![2022 Code Linting & Testing](https://github.com/urda/advent-of-code/actions/workflows/2022.yaml/badge.svg)](https://github.com/urda/advent-of-code/actions/workflows/2022.yaml)
- [2021](https://github.com/urda/advent-of-code/blob/master/years/2021/README.md)
  - [![2021 Code Linting & Testing](https://github.com/urda/advent-of-code/actions/workflows/2021.yaml/badge.svg)](https://github.com/urda/advent-of-code/actions/workflows/2021.yaml)
- [2015](https://github.com/urda/advent-of-code/blob/master/years/2015/README.md)
  - [![2015 Code Linting & Testing](https://github.com/urda/advent-of-code/actions/workflows/2015.yaml/badge.svg)](https://github.com/urda/advent-of-code/actions/workflows/2015.yaml)

# Environment Setup

**The following instructions are designed around `pyenv`, `pyenv-virtualenv`.**

Prepare the base python:

```bash
pyenv install 3.12.0
```

Create a python virtual environment:

```bash
pyenv virtualenv 3.12.0 advent
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
