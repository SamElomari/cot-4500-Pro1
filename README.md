# Programming Assignment 1

## Description
This assignment implements several numerical methods for solving equations and approximations:
- **Approximation Algorithm**: Computes the square root of 2 using an iterative method as per the slides.
- **Bisection Method**: Finds a root of a given function within a specified interval.
- **Fixed-Point Iteration**: Iteratively solves for a fixed point of a function.
- **Newton-Raphson Method**: Uses derivatives to quickly approximate a root of a function.

## Requirements
Python must be installed on the machine.
### Installing Dependencies
Code to download the dependencies
```bash
pip install -r requirements.txt
```

## Running the Program
Each of the required functions are implemented in `assignment_1.py`. These functions can be imported into a script or tested  interactively.

To run the script directly, (won't produce outputs):
```bash
python src/main/assignment_1.py
```

## Running the Tests
The test cases are located in `test_assignment_1.py` as per the instructions and verify the correctness of each algorithm against slide examples.

To run tests using `unittest`:
```bash
python -m unittest discover src/test
```

