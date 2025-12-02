# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 09:47:32 2024

@author: hillr
"""

import glob, os, re
import pandas as pd
import numpy as np
import datetime as dt

#%% Globals

filepath=r''

#%%

def read_txt_file(filepath):
    with open(filepath, 'r') as f:
        
        for l in f:
            pass

def read_txt_file_df(filepath):
    df=pd.read_csv(filepath, header=None, sep='|', engine='python')
    for col in df.columns:
        df[col]=df[col].sort_values(ignore_index=True)
    return df

def format_df(df:pd.DataFrame)->pd.DataFrame:
    return df

#%% Part 1

def f1(df:pd.DataFrame)->pd.DataFrame:
    return df

#%% Part 2

def f2(df:pd.DataFrame)->pd.DataFrame:
    return df

#%% Main

def part1(df:pd.DataFrame)->int:
    return f1(df)

def part2(df:pd.DataFrame)->int:
    return f2(df)

def main():
    df=read_txt_file_df(filepath)
    df = format_df(df)
    answer1 = part1(df)
    answer2 = part2(df)
    print('Part 1:', answer1)
    print('Part 2:', answer2)


if __name__=="__main__":
    main()