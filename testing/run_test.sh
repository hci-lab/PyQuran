#!/bin/bash

# a shell script to test `PyQuran` comprehensively 
#
# Usage:
#  $ ./run_test.sh
#
# ToDo:
#  * Array of file names
#  * loop to run them
#  * add commend line arguments to test a single module.

python3 test_quran.py
python3 test_searchHelper.py
python3 test_pyquran.py
