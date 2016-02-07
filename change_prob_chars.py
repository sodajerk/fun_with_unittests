#!/usr/bin/python

# gymLocker
import os
from os import listdir, getcwd

def change_prob_chars(path):
    problem_chars = [' ', '(' , ')', '&', "'", '"', '/'] 
    i = 0

    while i <= len(problem_chars) - 1:
        dirs = os.listdir(path)
    
        for filename in dirs:
            if problem_chars[i] == '&':
                os.rename(filename,filename.replace(problem_chars[i],'AND'))
            else:
                os.rename(filename,filename.replace(problem_chars[i],'_'))
       
        i+=1

change_prob_chars(os.getcwd())
