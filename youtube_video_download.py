#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 11 12:54:29 2022

@author: trycatchclasses
"""
from tkinter import *
from pytube import YouTube


root = Tk()

root.title('Youtube video Downloader')
root.geometry('400x200')

myLabel1 = Label(root,text='enter the link')
myLabel1.pack()

Enter1 = Entry(root)
Enter1.pack()

def down(enter):
    my_video = YouTube(enter)
    myLabel2 = Label(root,text='Title is:- '+my_video.title)
    myLabel2.pack()

    my_video = my_video.streams.get_highest_resolution()
    my_video.download()

    myLabel3 = Label(root,text='Download Complete !!')
    myLabel3.pack()
    
myButton = Button(root,text='Download',command=lambda : down(Enter1.get()))
myButton.pack()

root.mainloop()





























    
    
    
    
    
    
    
    
