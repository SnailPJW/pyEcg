# -*- coding: utf-8 -*-
"""
Created on Mon Jul 15 20:29:40 2019
@author: bryan
"""
from tkinter import*
import sqlite3
import cgi, os, sys
root = Tk()
root.title("中原電機碩專班:施振民 心電圖分析程式")
root.geometry("1000x720")#自行定義大小
#root.state("zoomed")#最大化畫面
root.configure(bg='pink')#設定背景顏色
root.resizable(0,0)#設(0,0)鎖放大畫面
root.iconbitmap("ecg.ico")
root.mainloop() 
