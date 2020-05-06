# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 23:07:25 2020

@author: linzhu
"""

from tkinter import filedialog
from tkinter import *

root = Tk()

root.directory = tkFileDialog.askdirectory()
print (root.directory)