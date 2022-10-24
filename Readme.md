# Rancho test suite

This is a test suite for the Rancho project. It is a collection of
tests that can be run against a certain cases to verify that it
behaves as expected.

## Project structure

The project is structured as follows:

    .
    ├── Makefile
    ├── README.md
    ├── requirements.txt
    ├── rancho
    │   ├── __init__.py
    │   ├── data
    │   │   ├── __init__.py
    │   │   ├── data.txt
    │   │--- wordcount_problem.py
    ├── tests
    │   ├── __init__.py
    │   ├── test_wordcount_problem.py
    ├── main.py

The `rancho` directory contains the code for the project. The
`tests` directory contains the tests for the project.

## Running the main program

The main program can be run by executing the following command:

    make run

## Running the tests

The tests are written in Python and can be run with the `pytest`
command. The tests are located in the `tests` directory.

To run the tests, you need to use make:

    make unit-test

## Expected output

The expected output of the program is as follows:

    Word "non" appears 12 times

