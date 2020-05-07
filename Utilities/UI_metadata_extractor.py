# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 20:24:39 2020

Author: linzhu
"""

from tkinter import *
from tkinter import ttk, filedialog
from extract_metadata import getListOfFiles, extractMetaData
import sys 
sys.path.append('../base/')
from DATImage import DATImage

class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master, padding = (5,10), relief = 'sunken')
        self.master = master
        self.master.title("Metadata Extractor")
        self.dirname = ""
        self.grid()
        self.create_widgets()    

    def create_widgets(self):
        self.label_1 = ttk.Label(self,text = 'Select a folder:')
        self.label_1.grid()
        
        self.botton_1 = ttk.Button(self, text = "...", command=self.select_directory)
        self.botton_1.grid()
        
        self.botton_2 = ttk.Button(self, text = "submit", command=self.extract_metadata)
        self.botton_2.grid()
        
    def select_directory(self):
        self.dirname = filedialog.askdirectory()
        print(self.dirname)
    
    def extract_metadata(self):
        keys = []
        print('Extract metadata from the files in folder: {}'.format(self.dirname))
        print('''Extract metadata from dat image file\nSave the metadata into a text file with same name''' )
        # Get the list of all files in directory tree at given path
        listOfFiles = getListOfFiles(self.dirname)
        for file in listOfFiles:
            file_log = file[:-3]+'txt'
            im = DATImage(file)
            extractMetaData(file_log, im.metadata)           
        

root = Tk()
app = Application(master=root)
app.mainloop()