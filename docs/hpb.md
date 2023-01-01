# Henry Plate Builder - `HPB`

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
