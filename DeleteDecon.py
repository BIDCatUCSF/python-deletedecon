# -*- coding: utf-8 -*-
"""
Created on Mon Jan 30 10:59:45 2017

@author: Kyle Marchuk

For use at the Biological Imaging Development Center (BIDC) at UCSF. 

This is a GUI to quickly delete the folder containing the deconvolution and MIPs
data. The raw data is ignored. Intended use is for memory management.

A .bat file is created and run through the command line. User prompts are
from the rmdir command and supressed. 

"""

import os
from tkinter import Tk,Label,BOTH,FALSE,TRUE,W,END
from tkinter import Frame,Button,Entry, filedialog, messagebox

origPath = 'C:/Cuda'

class createGUI(Frame):
    def __init__(self,parent):
        Frame.__init__(self,parent)
        
        self.parent = parent
        self.parent.title("Delete Decon/MIPs")       
        self.pack(fill=BOTH,expand = 1)
        self.centerWindow()
        self.initUI()
        
    def centerWindow(self):
        
        w = 500
        h = 80
        
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        
        x = (sw-w)/2
        y = (sh-h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w,h,x,y))
        
        #self.style = Style()
        #self.style.theme_use("vista")
      
    def initUI(self):
        
        #self.style = Style()
        #self.style.theme_use("vista")
        
        topFrame = Frame(self,borderwidth=1)
        topFrame.pack(fill=BOTH,expand=TRUE)
        
        Label(topFrame, text = "Select Directory for Deletion:").grid(row=0,column=0,padx=5,pady=5)      
        self.entryDelete = Entry(topFrame,width=45)
        self.entryDelete.grid(row=0,column=1,padx=5,pady=5)
        self.entryDelete.insert(END,origPath)
        Button(topFrame,width=2,text="...",command=self.dirOpen).grid(row=0,column=2,sticky=W)
        
        Button(topFrame,width=20,text = "Delete Decons",command=self.runDelete).grid(row=1,column=1,pady=5)
        
        
    def dirOpen(self):

        dirName = filedialog.askdirectory()           
               
        if dirName != '':
            self.entryDelete.delete(0,END)
            self.entryDelete.insert(END,dirName)
            
    def runDelete(self):
        
        deletePath = self.entryDelete.get()
        if deletePath == '':
            messagebox.showwarning("Deletion Path","Deletion Path Must Be Defined")
            return 0
        
        deleteFolders = []
        deletePath = os.path.abspath(deletePath)
        for root, dirs, files in os.walk(deletePath):
            for name in dirs:
                print(name)
                if name == "GPUdecon":
                    deleteFolders.append(os.path.join(root,name))                       
                
        deleteFile = open(deletePath + '\deleteDecon.bat','w')
        deleteFile.write('')
        deleteFile.close()
        
        for paths in deleteFolders:
            deleteFile = open(deletePath + '\deleteDecon.bat','a')
            deleteFile.write('rmdir ' + paths + ' ' + '/s/q ' + '\n')
            deleteFile.close()

                    
        os.system('start ' + deletePath + '\deleteDecon.bat')

    
        
 ##########################       
def main():
    
    root = Tk()
    createGUI(root)
    root.resizable(width=FALSE,height=FALSE)
    root.mainloop()
    
if __name__ == '__main__':
    main()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        