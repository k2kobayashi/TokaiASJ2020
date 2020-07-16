#! /bin/sh
#
# run.sh
# Copyright (C) 2020 Kazuhiro KOBAYASHI <root.4mac@gmail.com>
#
# Distributed under terms of the MIT license.
#

# # download csv from google spreadsheets
# curl -L -o sheet1.csv \
#     'https://docs.google.com/spreadsheets/d/1epd7pzJdWIFO0hKivWZOpIbLSfUHGzdCAoiIueGRApc/export?format=csv'

# parse spreadsheets
python parse_csv.py > middle.md

# concate as markdown
cat top.md middle.md bottom.md > README.md
