"""""
#1-я запись
import tkinter as tk
from tkinter import ttk

#2-я запись
window = tk.Tk()
window.geometry("700x200")


#3-я запись
def delete_text_now():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    text_aria.delete('1.0', tk.END)


#4-я запсь
def show_message():
    text_aria.insert('1.0', entry1.get()+'\n')
    text_aria.insert(tk.END, entry2.get()+'\n')


#5-я запись
label1 = tk.Label(master=window, text="ФИО")
label1.pack()
label1.place(x=40, y=40)

#6-я запись
entry1 = tk.Entry(master=window, text="ФИО")
entry1.pack()
entry1.place(x=100, y=40)

#7-я запись
label2 = tk.Label(master=window, text="Полных лет")
label2.pack()
label2.place(x=20, y=70)

#8-я запись
entry2 = tk.Entry(master=window, text="Полных лет")
entry2.pack()
entry2.place(x=100, y=70)

#9-я запись
button1 = tk.Button(master=window, text="Сохранить текст", command=show_message)
button1.pack()
button1.place(x=80, y=100)

#10-я запись
button2 = tk.Button(master=window, text="Удалить текст", command=delete_text_now)
button2.pack()
button2.place(x=85, y=130)

#11-я запись
text_aria = tk.Text(master=window, width=50, height=10)
text_aria.pack()
text_aria.place(x=240, y=20)

#12-я запись
window.mainloop()
"""