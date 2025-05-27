# -*- coding: utf-8 -*-
"""
Created on Wed Dec  6 09:57:22 2023

@author: hillr
"""

import numpy as np

def solve_problem(problem):
    answer = sum(np.random.randint(1,100,8))
    return answer

if __name__ == "__main__":
    print(solve_problem("https://adventofcode.com/2023/day/2/input"))

