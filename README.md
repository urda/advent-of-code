# Advent of Code

https://adventofcode.com/

## Environment Setup

### Prerequisites

**The following instructions are designed around a few tools. Make sure you have:**

- `direnv`
- `pyenv`
- `pyenv-virtualenv`
- `uv`

Please make sure you have these available first.

### Configure the Environment

Prepare the base python:

```bash
pyenv install 3.14.1
```

Create a python virtual environment:

```bash
pyenv virtualenv 3.14.1 advent
```

Switch to it after creation by leaving and returning to the directory. `direnv` should switch to and from `advent`.

Go ahead and update `pip`:

```bash
uv pip install --upgrade pip
```

And install the development requirements:

```bash
uv pip install -r requirements-dev.txt
```

## Running the "project"

You can launch the `advent-of-code` project with:

```bash
make run
```

## Running the "utilities"

You can launch the project utilities with:

```bash
make utils
```
