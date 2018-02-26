#!/usr/bin/env python
# -*- coding: utf-8 -*-
#创建一个Tk版的Helloworld

import tkinter

top = tkinter.Tk()
label = tkinter.Label(top, text = 'Hello World')
label.pack()
tkinter.mainloop()