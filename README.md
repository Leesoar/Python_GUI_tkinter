# Python GUI：tkinter

> 创建一个 GUI 应用就像艺术家作画一样。传统上，艺术家使用单一的画布开展创作。 其工作方式如下：首先会从一块干净的石板开始，这相当于用来构建其余组件的顶层窗口 对象。可以将其想象为房屋的地基或艺术家的画架。换句话说，必须在浇灌好混凝土或搭 建起画架之后，才能把真实的结构或画布拼装在上面。 

## 布局管理器

> Tk 有 3 种布局管理器来帮助控件集进行定位。 

* *Placer*

> 最原始的一种称为 Placer。它的做法非常直接：你提供控件的大小和摆放位置，然后管理器就会将其摆放好。问题是你必须对 所有控件进行这些操作，这样就会加重编程开发者的负担，因为这些操作本应该是自动完成的。

* *Packer*

> 这个命名十分恰当，因为它会把控件填充到正确的位置（即指定的父控件中），然后对于之后的每个控件，会去寻找剩余的空间
进行填充。这个处理很像是旅行时往行李箱中填充行李的过程。 

* *Grid*

> 第三种布局管理器是 Grid。你可以基于网格坐标，使用 Grid 来指定 GUI 控件的放置。 Grid 会在它们的网格位置上渲染 GUI
 应用中的每个对象。

### Packer的参数

* *fill*

> fill 参数告诉 Packer 让所在标签/按钮占据剩余的水平空间/垂直空间。

* *expand*

> expand 参数会引导使用fill的标签/按钮填充整个水平/垂直可视空间，将标签/按钮拉伸。

**具体参考[**fill与expand演示**](https://github.com/Leesoar/Python_GUI_tkinter/blob/master/helloworld3.py)**

## 其他控件

* *Scale*

**Scale 的使用方法详见[**Sacle与resize演示**](https://github.com/Leesoar/Python_GUI_tkinter/blob/master/helloworld3.py)**

## GUI小工具下载

* *Directory Lister*
> 这个应用是一个自己练手制作的简单目录遍历工具。它会从当前目录开始，提供一个文件列表。双击列表中任意其他目录，就会使得工具切换到新目录中，用新目录中的文件列表代替旧文件列表。 

**下载地址：[Directory Lister](https://github.com/Leesoar/Python_GUI_tkinter/raw/master/listdir.exe)
