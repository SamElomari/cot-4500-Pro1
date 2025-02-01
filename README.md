# Programming Assignment 1

## Description
This assignment implements several numerical methods for solving equations and approximations:
- **Approximation Algorithm**: Computes the square root of 2 using an iterative method.
- **Bisection Method**: Finds a root of a given function within a specified interval.
- **Fixed-Point Iteration**: Iteratively solves for a fixed point of a function.
- **Newton-Raphson Method**: Uses derivatives to quickly approximate a root of a function.

## Requirements
Before running the program or tests, ensure you have Python installed and install the required dependencies.

### Installing Dependencies
Run the following command to install required packages:
```bash
pip install -r requirements.txt
```

## Running the Program
Each function is implemented in `assignment_1.py`. You can import these functions into your own script or test them interactively.

To run the script directly:
```bash
python src/main/assignment_1.py
```

## Running the Tests
The test cases are located in `test_assignment_1.py` and verify the correctness of each algorithm.

To run all tests using `pytest`:
```bash
pytest src/test/test_assignment_1.py
```

To run tests using `unittest`:
```bash
python -m unittest discover src/test
```

