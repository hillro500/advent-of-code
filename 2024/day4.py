# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 14:38:43 2024

@author: hillr
"""

import glob, os, re
import pandas as pd
import numpy as np
import datetime as dt

#%% Globals

txt_file=r'C:/workspace/my python scripts/advent of code 2024/day4_input.txt'
pattern='XMAS'
checks={'up':[''],
        'down':[''],
        'left':[''],
        'right':[pattern],
        'down_left':[''],
        'down_right':[''],
        'up_left':[''],
        'up_right':[''],
        }


#%%

def read_txt_file(filepath):
    with open(filepath, 'r') as f:
        
        for l in f:
        df=pd.read_csv(filepath, header=None)
    return df

def find_XMAS(df):
    count=0
    for idx, row in df.iterrows():
        match=re.findall(pattern, row[0])
        if match:
            count+=len(match)
    print(count)

#%% Main

def main():
    df=read_txt_file_df(txt_file)
    find_XMAS(df)

if __name__=="__main__":
    main()