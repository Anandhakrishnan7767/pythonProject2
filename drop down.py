from tkinter import  *
root = Tk()

mymenu=Menu(root)
root.config(menu=mymenu)
submenu=Menu(mymenu)
mymenu.add_cascade(label="file",menu=submenu)
submenu.add_command(label="save")
newmenu=Menu(mymenu)
mymenu.add_cascade(label="edit",menu=newmenu)
newmenu.add_command(label="undo")
root.mainloop()