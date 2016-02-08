#!/usr/bin/python

# gymLocker
import os

def change_prob_chars(filename):
    problem_chars = [' ', '(' , ')', "'", '"', '/']

    for char in problem_chars:
        filename = filename.replace(char, '_')

    filename = filename.replace('&', 'AND')

    return filename

def get_files(path):
    return os.listdir(path)

def rename_file(filename, new_filename, path):
    os.rename(os.path.join(path,filename), os.path.join(path, new_filename))

def create_new_filename(path):
    files = get_files(path)
    for filename in files:
        new_filename = change_prob_chars(filename)
        
        rename_file(filename, new_filename, path) 

create_new_filename(os.getcwd())
