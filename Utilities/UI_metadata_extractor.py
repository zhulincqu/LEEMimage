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
        super().__init__(master, relief = 'sunken')
        self.master = master
        self.master.title("Metadata Extractor")
        self.grid()
        self.dirname = "Selected a folder..."

        self.label_1 = ttk.Label(self,text = 'Folder:')
        self.label_1.grid(row=0, column=0, sticky=W)
        
        self.label_2 = ttk.Label(self, text = '')
        self.label_2.grid(row=1, column=1, sticky=W)
        
        self.entry_1 = ttk.Entry(self, width = 50)
        self.entry_1.insert(0, self.dirname)
        self.entry_1.grid(row=0, column=1)
        
        self.botton_1 = ttk.Button(self, width=10, text = "...", command=self.select_directory)
        self.botton_1.grid(row=0, column=2)
        
        self.botton_2 = ttk.Button(self, width=10, text = "Extract", command=self.extract_metadata)
        self.botton_2.grid(row=1, column=2)
        

        
    def select_directory(self):
        self.dirname = filedialog.askdirectory()
        self.entry_1.delete(0, END)
        self.entry_1.insert(0,self.dirname)
    
    def extract_metadata(self):
        keys = ['Camera Exposure','Average Images','Emission Curr.','MCH',
                'Mitutoyo X', 'Mitutoyo Y','Objective','PCH','FOV','Rotation',
                'Projective 3','Sample Temp.','Start Voltage']
        self.label_2['text'] = 'Extracting metadata from .dat files in folder (subfolders):\n {}'.format(self.dirname)
        
        # Get the list of all files in directory tree at given path
        listOfFiles = getListOfFiles(self.dirname)
        for file in listOfFiles:
            file_log = file[:-3]+'txt'
            im = DATImage(file)
            extractMetaData(file_log, im.metadata,keys)           
        

root = Tk()
root.title("Metadata Extractor")
app = Application(master=root)
app.mainloop()