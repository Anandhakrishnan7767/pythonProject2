from tkinter import *
from tkinter import messagebox
root=Tk()
class myschool:
    def __init__(self,rootone):
        frame=Frame(rootone)
        frame.pack()
        self.pbutton=Button(frame, text ='student name',command=self.std)
        self.pbutton.pack()
        messagebox.askyesno(title='continue')

        # label1=Label(rootone,text='studnts1')
        # label1.grid(row=0,column=1)
        # entery1=Entry(root)
        # entery1.grid(row=0,column=1)
        # label1.grid()
        self.qbutton=Button(frame,text='absent',command=frame.quit)
        self.qbutton.pack()
    def std(self):
        print('attend')


obj=myschool(root)

root.mainloop()