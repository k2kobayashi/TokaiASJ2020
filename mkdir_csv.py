#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright (c) 2020 Kazuhiro KOBAYASHI <root.4mac@gmail.com>
#
# Distributed under terms of the MIT license.

"""

"""

import numpy as np
import pandas as pd

from pathlib import Path

csvf = Path("./sheet1.csv")
if not csvf.exists():
    raise ValueError("Check csv file")

df = pd.read_csv(csvf)
tdir = Path("slide")

for idx, row in df.iterrows():
    if not np.isnan(row["発表番号"]):
        (tdir / "{} {}".format(int(row["発表番号"]), row["氏名"])).mkdir(exist_ok=True)
