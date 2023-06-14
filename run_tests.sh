#!/bin/bash

# activate the virtual environment
. ./venv/bin/activate

# run the test suite
python -m pytest test_pink_morsels_sales_visualizer.py

# collect exit code from pytest
PYTEST_EXIT_CODE=$?

# return exit code 0 if all tests pass or 1 otherwise
if [ $PYTEST_EXIT_CODE -eq 0 ]
then
  exit 0
else
  exit 1
fi