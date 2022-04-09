#! /usr/bin/env python
# -*- coding:utf-8 -*-
"""
@Authors: Manto
@Description:

"""

import datetime
from pandas_datareader import data as pdr
import pandas as pd
import numpy as np
import sys
__copyright__ = "Copyright 2021, Manto Ltd."
__license__ = "Proprietary"


import os
os.system('cls')


# simple function used to obatin open, close, or adjusted closing price of
# equities from yahoo finance
# takes 4 arguments, portfolio list, start date, end date and price type
# (open, close, adj close）

def price_dl(tickers: list, start_date: str, end_date: str, price_type: str):
    data = pdr.get_data_yahoo(
        tickers,
        start=start_date,
        end=end_date)[price_type]
    return data
    print(data)


def price_dl_all(tickers: list, start_date: str, end_date: str):
    data = pdr.get_data_yahoo(
           tickers,
           start=start_date,
           end=end_date)
    return data
    print(data)


def price_dl_csv(tickers: list, start_date: str, end_date: str):
    data = pdr.get_data_yahoo(
        tickers,
        start=start_date,
        end=end_date)
    return data

    data.to_csv(price_dl.csv, index=False)
