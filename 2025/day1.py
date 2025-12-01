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

filepath=r'C:\Users\hillr\OneDrive - Astrion\workspace\my scripts\repositories\advent of code\2025\day_1_input.txt'

dial_start = 50
dial_min = 0
dial_max = 99

#%%

def read_txt_file_df(filepath):
    df=pd.read_csv(filepath, header=None)
    return df

def format_df(df:pd.DataFrame)->pd.DataFrame:
    df['Direction'] = df[0].apply(lambda x: str(x)[0])
    df['Distance'] = df[0].apply(lambda x: int(str(x)[1:])).astype(int)

    df.loc[0, 'Last_Position'] = dial_start

    #  Assuming dial min is 0:
    for i in range(len(df)):
        if i == 0:
            continue
        df.loc[i, 'Last_Position'] = df.loc[i-1, 'New_Position']
        if df.loc[i, 'Direction'] == 'L':
            df.loc[i, 'New_Position'] = (df.loc[i-1, 'Last_Position'] + df.loc[i, 'Distance']) % (dial_max + 1)
        elif df.loc[i, 'Direction'] == 'R':
            df.loc[i, 'New_Position'] = (df.loc[i-1, 'Last_Position'] - df.loc[i, 'Distance']) % (dial_max + 1)
    return df

def calculate_zeros(df:pd.DataFrame)->int:
    return (df['Last_Position'] == 0).sum()

#%% Main

def main():
    df=read_txt_file_df(filepath)
    df = format_df(df)
    zero_count = calculate_zeros(df)
    # print(df['Direction'].unique())
    print(zero_count)

if __name__=="__main__":
    main()