# Advent of Code

https://adventofcode.com/

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
