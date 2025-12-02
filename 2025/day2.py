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

filepath=r'day2_input.txt'

#%%

def read_file_df(filepath):
    df=pd.read_csv(filepath, header=None, sep=',', engine='python')
    return df

def format_df(df:pd.DataFrame)->pd.DataFrame:
    df = df.T.rename(columns={0:'Range'})
    df['Split'] = df['Range'].str.split('-')
    df['Start'], df['End'] = df['Split'].apply(lambda x: int(x[0])), df['Split'].apply(lambda x: int(x[1]))
    return df

#%% Part 1

def find_invalid_IDs(df:pd.DataFrame)->[int]:
    invalid_IDs = []
    for idx, row in df.iterrows():
        for i in range(row['Start'], row['End']+1):
            string = str(i)
            # Source - https://stackoverflow.com/a/4789617
            # Posted by Senthil Kumaran, modified by community. See post 'Timeline' for change history
            # Retrieved 2025-12-02, License - CC BY-SA 4.0
            
            firstpart, secondpart = string[:len(string)//2], string[len(string)//2:] # split string in half

            if firstpart == secondpart:
                invalid_IDs.append(int(i))

    return invalid_IDs

#%% Part 2

def check_strings(strings:[str])->bool:
    if len(strings) == 1:
        return False
    first_num = strings[0]
    for i in strings:
        if i != first_num:
            return False
    return True
        
def split_string(string:str, num_splits:int)->[str]:
    size = len(string)
    if size % num_splits > 0:
        return
    else:
        strings=[]
        last_num = 0
        splits = list(range(0, num_splits+1))
        for i in splits:
            split = string[last_num:i]
            if split:
                strings.append(split)
            last_num = i
    return strings

def find_invalid_IDs_2(df:pd.DataFrame)->[int]:
    invalid_IDs = []
    for idx, row in df.iterrows():
        for i in range(row['Start'], row['End']+1):
            string = str(i)
            size = len(string)
            for num_splits in range(1,size):
                strings = split_string(string, num_splits)
                if strings and check_strings(strings):
                    invalid_IDs.append(int(string))
    return invalid_IDs

#%% Main

def part1(df:pd.DataFrame)->int:
    answer = sum(find_invalid_IDs(df))
    print('Part 1:', answer)
    return answer

def part2(df:pd.DataFrame)->int:
    answer = sum(find_invalid_IDs_2(df))
    print('Part 2:', answer)
    return answer

def main():
    df=read_file_df(filepath)
    df = format_df(df)
    # part1(df)
    part2(df)

if __name__=="__main__":
    main()