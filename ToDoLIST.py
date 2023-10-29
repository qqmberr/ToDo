import customtkinter
from tkinter import *
from PIL import ImageTk



customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')


def add_task():
    window = customtkinter.CTkToplevel(root)
    window.title('Добавить задачу')
    window.geometry('400x100')

    task_tekst = customtkinter.CTkEntry(window, width=250)
    task_tekst.pack(pady=5)

    customtkinter.CTkButton(window, text='Добавить', font=("Roboto", 24), command=lambda: add(task_text.get())).pack()

    window.mainloop()


root = customtkinter.CTk()
root.title('Планировщик задач')
root.geometry('1000x800')

#PhotoImage.photo = 0
#img_del = ImageTk.PhotoImage(file='cross.jpg')



btn_add_task = customtkinter.CTkButton(root, text='Добавить задачу', font=("Roboto", 24), command=add_task())
btn_add_task.pack(anchor=S, side=BOTTOM, pady=5)

root.mainloop()