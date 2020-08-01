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


print("### 10:10-11:01 概要講演　前半 (概要講演:Zoom開催)")
for idx, row in df.iterrows():
    if not np.isnan(row["発表番号"]):
        print(
            "- **発表番号{} ({})** [(資料)]({})".format(
                int(row["発表番号"]), row["発表場所"], row["資料"]
            )
        )
        print("\t- {}  ".format(row["タイトル"]))
        print("\t- {} （{} {}）".format(row["氏名"], row["大学"], row["研究室"]))
    else:
        print("")
        print(
            "### 11:15-12:00 概要講演　後半 (概要講演:Zoom開催)"
        )
    print("")
