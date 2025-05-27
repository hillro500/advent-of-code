# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 09:47:32 2024

@author: hillr
"""

import glob, os, re, io
import pandas as pd
import numpy as np
import datetime as dt

#%% Globals

filepath=r'C:/workspace/my python scripts/advent of code 2024/day5_input.txt'

#%%

def read_txt_file(filepath):
    with open(filepath, 'r') as f:
        contents=f.read()
        f.close()
    return contents

def read_dataframe(string:str)->pd.DataFrame:
    df=pd.DataFrame(string)
    return df

def read_txt_file_df(filepath='', string=''):
    if string:
        filepath=io.StringIO(string)
    df=pd.read_csv(filepath, header=None, sep='|', engine='python')
    # for col in df.columns:
    #     df[col]=df[col].sort_values(ignore_index=True)
    return df

#%% Main

def main():
    contents=read_txt_file(filepath)
    a=contents.split('\n\n')
    df=read_txt_file_df(string=a[0])
    df=read_dataframe(a[0])
    df2=read_dataframe(a[1])

if __name__=="__main__":
    main()