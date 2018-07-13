#!/bin/bash

# Overwite files_template.md   > files.md
cat templates/analysis_tools_template.md > docs/analysis_tools.md
cat templates/arabic_tools_template.md   > docs/arabic_tools.md
cat templates/quran_tools_template.md    > docs/quran_tools.md
cat docs/index.md                        > ../README.md # For the repo; Readme
cat docs/index.md                        > ../../README.md # for the PyPI Readme
cat docs/CONTRIBUTING.md                 > ../CONTRIBUTING.md


# Generate docs
./auto_gen_docs.py
