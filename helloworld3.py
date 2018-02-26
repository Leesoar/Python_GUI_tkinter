#!/usr/bin/env python
# -*- coding: utf-8 -*-
#介绍的控件是Scale，此外还会重点了解控件是如何通过回调函数（如resize()）与其他控件进行通信的。 Label控件中的文本会受到Scale控件上操作的影响。 

from tkinter import * 

def resize(ev=None):
	label.config(font='Helvetica -%d bold' % scale.get())          #Helvetica是一种广泛使用的西文无衬线字体

top = Tk()
top.geometry('250x150')     #定义顶层窗口大小为250*150

label = Label(top, text='Hello World!', font='Helvetica -12 bold')
label.pack(fill=Y, expand=1)               #fill 参数告诉 Packer 让 label 占据剩余的垂直空间，而 expand 参数则会引导它填充整个垂直可视空间，进行拉伸

scale = Scale(top, from_=10, to=40, orient=HORIZONTAL, command=resize)      #比例大小范围为10到40，位置为水平的，命令为resize即调整label标签大小
scale.set(12)        #设定应用启动的字体初始大小为12
scale.pack(fill=X, expand=1)

quit = Button(top, text='QUIT', command=top.quit, activeforeground='white', activebackground='#878787')   #设置按钮前景色为white，背景色(按下后的颜色)为#878787
quit.pack()

mainloop()       #进入主循环