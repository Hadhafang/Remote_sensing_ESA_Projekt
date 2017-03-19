# -*- coding: utf-8 -*-
import os
"""
Created on Sun Mar 19 16:25:25 2017

@author: nosklo
on stack owerflow: 
http://stackoverflow.com/questions/229186/os-walk-without-digging-into-directories-below
"""

# -------------------------------------------------------------
# METHOD THAT DEFINES HOW DEEP THE ITERATION WILL GO, IF LEVEL
# IS SET TO 2 THE ITERATION WILL GO 2 FOLDERS DEEP AND NOT FURHTER
# -------------------------------------------------------------
def walklevel(some_dir, level):
    some_dir = some_dir.rstrip(os.path.sep)
    assert os.path.isdir(some_dir)
    num_sep = some_dir.count(os.path.sep)
    for root, dirs, files in os.walk(some_dir):
        yield root, dirs, files
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]