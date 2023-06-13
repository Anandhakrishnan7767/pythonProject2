from tkinter import  *

from tkinter import messagebox

root=Tk()
def __init__(self,root):
    self.qbutton=Button(viewmenu,text='absent',command=fun11().quit)
    frame = Frame(root)
    frame.pack()
    self.pbutton = Button(frame, text='student name', command=self.std)
    self.pbutton.pack()
    messagebox.askyesno(title='continue')


def fun1():
    print('new project')

def fun2():
    print('new file')

def fun3():
    print('scratch file')
def fun4():
    print('open')
def fun5():
    print('save as')

def fun6():
        print('undo')
def fun7():
    print('cut')
def fun8():
    print('copy')
def fun9():
    print('paste')
def fun10():
    print('delete')
def fun11():
        print('tool')
def fun12():
    print('appearence')
def fun13():
    print('quick')
def fun14():
    print('quick type')
def fun15():
    print('parameter')
def fun16():
        print('back')
def fun17():
    print('search every whwre')
def fun18():
    print('class')
def fun19():
    print('file')
def fun20():
    print('symbol')




pymenu=Menu(root)
root.config(menu=pymenu)
filemenu=Menu(pymenu)
pymenu.add_cascade(label="file",menu=filemenu)
filemenu.add_command(label="new project",command=fun1)
# messagebox.showinfo('file','new')
filemenu.add_command(label="new file",command=fun2)
filemenu.add_separator()
filemenu.add_command(label="scratch file",command=fun3)
filemenu.add_command(label="open",command=fun4)
filemenu.add_command(label="save as",command=fun5)


editmenu=Menu(pymenu)
pymenu.add_cascade(label="view",menu=editmenu)
editmenu.add_command(label="tool window",command=fun6)
# messagebox.askquestion('undo','undo',)
editmenu.add_command(label="appearence",command=fun7)
editmenu.add_separator()
editmenu.add_command(label="quick  defenition",command=fun8)
editmenu.add_command(label="quick type  defenition",command=fun9)
editmenu.add_command(label="parameter info",command=fun10)


viewmenu=Menu(pymenu)
pymenu.add_cascade(label="edit",menu=viewmenu)
viewmenu.add_command(label="undo",command=fun11)
messagebox.askquestion('undo','undo',)
viewmenu.add_command(label="cut",command=fun12)
viewmenu.add_separator()
viewmenu.add_command(label="copy ",command=fun13)
viewmenu.add_command(label="paste",command=fun14)
viewmenu.add_command(label="delete",command=fun15)


navigatemenu=Menu(pymenu)
pymenu.add_cascade(label="naviggate",menu=navigatemenu)
navigatemenu.add_command(label="back",command=fun16)
# messagebox.askquestion('undo','undo',)
navigatemenu.add_command(label="search every where",command=fun17)
navigatemenu.add_separator()
navigatemenu.add_command(label="class ",command=fun18)
navigatemenu.add_command(label="file",command=fun19)
navigatemenu.add_command(label="symbol",command=fun20)


root.mainloop()















