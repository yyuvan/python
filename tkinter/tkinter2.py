# from tkinter import *
# from PIL import Image, ImageTk
# root=Tk()
# root.mainloop()


# #IMAGE IN TKINTER
# root=Tk()
# root.title('image')
# root.geometry('400x400')

# upload=Image.open('leaf.jpg')
# image=ImageTk.PhotoImage(upload)

# lbl=Label(root,image=image, height=350, width=300)
# lbl.place(x=50,y=0)
# lbl2=Label(root,text='This is how you add an image in Tkinter Window')
# lbl2.place(x=40,y=360)

# root.mainloop()




# from tkinter import *
# from tkinter import messagebox
# root=Tk()

# root.geometry("200x200")
# def msg():
#     messagebox.showwarning("Alert", "Stop! Virus Found.")

# button=Button(root,text="Scan for virus", command=msg)
# button.place(x=40,y=80)
# root.mainloop()




from tkinter import *
from PIL import Image, ImageTk
root=Tk()
root.geometry("400x300")

root.title("main")
def topwin():
    top= Toplevel()
    top.geometry("180x100")
    top.title("toplevel")
    l2=Label(top, text="This is toplevel window")
    l2.pack()
    top.mainloop()

l=Label(root,text="This is the root window")
btn=Button(root, text="Click here to open another window",command=topwin)
l.pack()
btn.pack()
















root.mainloop()