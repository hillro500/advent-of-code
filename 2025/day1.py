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

filepath=r'2025\day_1_input.txt'

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
    df['Full_Rotations'] = df['Distance'] // (dial_max + 1)
    #  Assuming dial min is 0:
    for i in range(len(df)):
        if i == 0:
            df.loc[0, 'Last_Position'] = dial_start
        else:
            df.loc[i, 'Last_Position'] = df.loc[i-1, 'New_Position']
        if df.loc[i, 'Direction'] == 'L':
            df.loc[i, 'New_Position'] = (df.loc[i, 'Last_Position'] + df.loc[i, 'Distance']) % (dial_max + 1) # type: ignore
        elif df.loc[i, 'Direction'] == 'R':
            df.loc[i, 'New_Position'] = (df.loc[i, 'Last_Position'] - df.loc[i, 'Distance']) % (dial_max + 1) # type: ignore
    return df

#%% Part 1

def find_zeros(df:pd.DataFrame)->pd.DataFrame:
    return df[df['New_Position'] == 0]

#%% Part 2

def calculate_passed_zeroes(df:pd.DataFrame)->int:
    passed_zeroes = 0
    
    for idx, row in df.iterrows():
        if row['Direction'] == 'L':
            if row['Last_Position'] > row['New_Position']:
                passed_zeroes+=1
        elif row['Direction'] == 'R':
            if row['Last_Position'] < row['New_Position']:
                passed_zeroes+=1
    return passed_zeroes

#%% Main

def part1(df:pd.DataFrame):
    zero_count = len(find_zeros(df))
    # print(df['Direction'].unique())
    print(zero_count)

def part2(df:pd.DataFrame):
    passed_zeroes = df['Full_Rotations'].sum()
    zeroes_index = find_zeros(df).index
    passed_zeroes += calculate_passed_zeroes(df.iloc[zeroes_index])
    passed_zeroes += calculate_passed_zeroes(df.iloc[~zeroes_index])
    passed_zeroes += len(df.iloc[~zeroes_index])
    print(passed_zeroes)

def main():
    df=read_txt_file_df(filepath)
    df = format_df(df)
    part2(df)

if __name__=="__main__":
    main()