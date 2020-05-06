# -*- coding: utf-8 -*-
"""
User interface for Metadata Extractor.

Author: linzhu
"""

from tkinter import filedialog
from tkinter import *

root = Tk()

root.directory = tkFileDialog.askdirectory()
print (root.directory)