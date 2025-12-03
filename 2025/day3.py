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

file=r'day3_input.txt'

bank_slots = 12

#%%

def read_txt_file_df(file)->pd.DataFrame:
    filepath = os.path.join(os.path.dirname(__file__), file)
    df=pd.read_csv(filepath, header=None)
    return df

def format_df(df:pd.DataFrame)->pd.DataFrame:
    df = df.rename(columns={0:'Bank'})
    df['Bank'] = df['Bank'].astype(str)
    return df

#%% Part 1

def calculate_max_joltage(df:pd.DataFrame)->pd.DataFrame:
    df['Max Joltage'] = pd.Series()
    for idx, row in df.iterrows():
        first_digit = None
        second_digit = None
        total = 0
        bank = row['Bank']
        for i in range(0, len(bank)):
            digit = int(bank[i])

            if first_digit is None:
                first_digit = digit
            elif second_digit is None:
                second_digit = digit

            try:
                new_total = int(str(first_digit) + str(second_digit))
            except ValueError:
                new_total = 0

            if new_total == 99:
                df.loc[idx, 'Max Joltage'] = new_total
                break # no sense in looking for a higher number
            elif new_total > total:
                total = new_total

            if i == len(bank)-1: #end of bank
                if digit > second_digit:
                    second_digit = digit
                new_total = int(str(first_digit) + str(second_digit))
                if new_total > total:
                    total = new_total
                df.loc[idx, 'Max Joltage'] = total # save total
            else:
                if digit > first_digit:
                    first_digit = digit
                    second_digit = None # reset second digit along with first digit
                elif second_digit is not None and digit > second_digit:
                    second_digit = digit

    return df

#%% Part 2

def calculate_max_joltage2(df:pd.DataFrame)->pd.DataFrame:
    for idx, row in df.iterrows():
        bank = row['Bank']
    return df

#%% Main

def part1(df:pd.DataFrame)->int:
    answer = calculate_max_joltage(df)['Max Joltage'].sum()
    print('Part 1:', answer)
    return answer

def part2(df:pd.DataFrame)->int:
    answer = calculate_max_joltage2(df)['Max Joltage'].sum()
    print('Part 2:', answer)
    return answer

def main():
    df=read_txt_file_df(file)
    df=format_df(df)
    answer1 = part1(df)
    # answer2 = part2(df)

if __name__=="__main__":
    main()