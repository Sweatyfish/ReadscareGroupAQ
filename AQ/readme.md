# Red Scare! - solutions

Each problem has its own program, which reads one graph from stdin and prints the answer to stdout:

- `Alternate.py`
- `Few.py`
- `Many.py`
- `None.py`
- `Some.py`

Requires Python 3 (tested with Python 3.x). Standard library only.

## Running a single instance

    python Few.py < ../red-scare/data/gnm-5000-10000-0.txt

## Running on all instances

`test.py` runs one program on every `.txt` file in `../red-scare/data/`
and prints the answer and running time for each (10 second timeout).
Change the `program` variable at the top of `test.py` to choose
which program to run.
