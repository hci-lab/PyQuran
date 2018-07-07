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

python3 -B test_quran.py
python3 -B test_searchHelper.py
python3 -B test_pyquran.py
