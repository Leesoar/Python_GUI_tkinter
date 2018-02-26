#!/usr/bin/env python
# -*- coding: utf-8 -*-
#Button版Helloworld

import tkinter

top = tkinter.Tk()        #创建顶层窗口
quit = tkinter.Button(top, text='Hello World', command=top.quit)       #创建一个具有关闭主窗口功能的helloworld按钮
quit.pack()        #让packer自己寻找适合的位置来放置Button
tkinter.mainloop()        #进入主循环