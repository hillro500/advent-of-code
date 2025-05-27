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

#%% Main

def main():
    df=read_txt_file_df(filepath)

if __name__=="__main__":
    main()