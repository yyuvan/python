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




# from tkinter import *
# from PIL import Image, ImageTk
# root=Tk()
# root.geometry("400x300")

# root.title("main")
# def topwin():
#     top= Toplevel()
#     top.geometry("180x100")
#     top.title("toplevel")
#     l2=Label(top, text="This is toplevel window")
#     l2.pack()
#     top.mainloop()

# l=Label(root,text="This is the root window")
# btn=Button(root, text="Click here to open another window",command=topwin)
# l.pack()
# btn.pack()

# import tkinter as tk
# from tkinter import messagebox
# from PIL import Image, ImageTk

# root = tk.Tk()
# root.geometry("400x400")
# root.title("Image in Tkinter")
# root.configure(bg='white')

# upload=Image.open('leaf.jpg')
# rimage=upload.resize((50,50))
# image=ImageTk.PhotoImage(upload)

# lbl=tk.Label(root,image=image, height=350, width=300)
# lbl.place(x=50,y=0)

# lbl= tk.Label(root, text="Welcome to Denomination Calculator")
# lbl.place(x=50,y=360)

# def topwin():
#     top= tk.Toplevel()
#     top.geometry("300x400")
#     top.title("Denominations")
#     top.configure(bg='lightblue')
#     l2=tk.Label(top, text="Denominations Calculated Successfully!")
#     l2.pack()
#     e=tk.Entry(top, width=30)
#     e.pack()
#     b=tk.Button(top, text="Close", command=top.destroy)
#     b.pack()
#     top.mainloop()
# def calculate():
#     x=messagebox.showinfo("Denominations Calculated","Press here")
#     if x=="ok":
#         topwin()

# btn=tk.Button(root, text="Calculate Denominations", command=calculate)
# btn.place(x=120,y=320)

# root.mainloop()


# import tkinter as tk
# root=tk.Tk()
# root.geometry("500x400")
# root.title("Main Window")

# lbl=tk.Label(root, text="Welcome to the Main Window")
# lbl.pack(pady=20)

# root.mainloop()

import tkinter as tk

def calculate_notes():
    try:
        amount = int(entry.get())

        notes_2000 = amount // 2000
        amount = amount % 2000

        notes_1000 = amount // 1000
        amount = amount % 1000

        notes_500 = amount // 500

        result_label.config(
            text=f"2000 notes: {notes_2000}\n"
                 f"1000 notes: {notes_1000}\n"
                 f"500 notes: {notes_500}"
        )
    except ValueError:
        result_label.config(text="Please enter a valid number")

# Create window
root = tk.Tk()
root.title("Currency Note Calculator")
root.geometry("300x250")

# Label at top
label = tk.Label(root, text="Enter Amount", font=("Arial", 14))
label.pack(pady=10)

# Input box
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=5)

# Button
btn = tk.Button(root, text="Calculate", command=calculate_notes)
btn.pack(pady=10)

# Result display
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Run app
root.mainloop()