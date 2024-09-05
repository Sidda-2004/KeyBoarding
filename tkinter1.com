from tkinter import *
root=tk()
root.minsize(height=500,width=900)
def tab1():
  label1.destroy()
  button1.destroy()


label1 = label(root,text='KEYBOARDING',font = ('Times_New_Roman'),35)
label1.pack()
button1 = Button(root,text='Lets Go!',font = ('Times_New_Roman'),25)
button1.pack(side = BOTTOM)
root = mainloop()