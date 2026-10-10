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

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
export PYTHONPATH="${PROJECT_ROOT}:${PYTHONPATH}"

python3 -B "${PROJECT_ROOT}/testing/test_quran.py"
python3 -B "${PROJECT_ROOT}/testing/test_searchHelper.py"
python3 -B "${PROJECT_ROOT}/testing/test_pyquran.py"
