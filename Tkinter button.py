from tkinter import *
from tkinter import messagebox
def button_1():
    messagebox.showinfo('Результат', int(a.get())*15)
root=Tk()
root.title('Приложение')
root.geometry('500x300')
a=Entry(root, width=10,  bg='grey', fg='white', font='consolas')
a.pack()
Button(root, text='Посчитать', width=10, height=2, bg='cyan',
command=button_1).pack()
root.mainloop()