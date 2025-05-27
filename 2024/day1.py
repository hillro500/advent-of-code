# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 12:13:48 2024

@author: hillr
"""

import glob, os, re
import pandas as pd
import numpy as np
import datetime as dt

#%% Globals

txt_file=r'C:/workspace/my python scripts/advent of code 2024/input_day1.txt'

#%%

def read_txt_file(filepath):
    df=pd.read_csv(filepath, header=None, sep='  ', engine='python')
    for col in df.columns:
        df[col]=df[col].sort_values(ignore_index=True)
    return df

def calculate_distance(df):
    answer=pd.DataFrame(columns=['Distance'])
    for idx, row in df.iterrows():
        answer.loc[idx,'Distance']=abs(row[0]-row[1])
    print(answer['Distance'].sum())
    
def calculate_similarity(df):
    answer=pd.DataFrame(columns=['Number','Occurances'])
    answer['Number']=df[0].unique()
    left_idx=0
    count=0
    for idx, row in df[1].items():
        while answer.loc[left_idx,'Number'] < row and left_idx < len(answer):
            answer.loc[left_idx,'Occurances']=count
            left_idx+=1
            count=0
        check=answer.loc[left_idx,'Number']
        if check==row:
            count+=1
    answer['Similarity_Score']=answer['Number']*answer['Occurances']
    print(answer['Similarity_Score'].sum())

def string_to_ordered_list(string:str)->list:
    order=[]
    for x in string:
        order.append(int(x))
    order.sort()
    return order

#%% Main

def main():
    df=read_txt_file(txt_file)
    # calculate_distance(df)
    calculate_similarity(df)

if __name__=="__main__":
    main()
    # df=pd.DataFrame({0:['342133'],1:['435393']})
    # perform_calculations(df)