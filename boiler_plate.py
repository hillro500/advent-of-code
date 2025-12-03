import glob, os, re
import pandas as pd
import numpy as np
import datetime as dt

#%% Globals

file=r''

#%%

def read_txt_file(filepath):
    with open(filepath, 'r') as f:
        
        for l in f:
            pass

def read_txt_file_df(filepath)->pd.DataFrame:
    filepath = os.path.join(os.path.dirname(__file__), file)
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
    answer = f1(df)
    print('Part 1:', answer)
    return answer

def part2(df:pd.DataFrame)->int:
    answer = f2(df)
    print('Part 2:', answer)
    return answer

def main():
    df=read_txt_file_df(file)
    df = format_df(df)
    answer1 = part1(df)
    answer2 = part2(df)

if __name__=="__main__":
    main()