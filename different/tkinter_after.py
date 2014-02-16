# -*- coding: utf-8 -*-
import tkinter
import time


tm = time.time()

def call_passive(event):
    print("Выполнен шаг процесса.")
    # Будет запускаться 10 секунд через каждую секунду
    if time.time() - tm < 10:
        root.after(1000, call_passive, event)


def call_active(event):
    print("Пассивное нажатие в процессе.")


def keybind(event):
    print("Нажата клавиша - ", event.keysym)


root = tkinter.Tk()
root.geometry("400x400+100+100")
root.bind("<Any-KeyRelease>", keybind)

bt_free = tkinter.Button(root, width=20, text="Свободно нажимаем")
bt_free.place(relx=0.5, rely=0.33, anchor="center")
bt_free.bind("<ButtonRelease-1>", call_active)

bt_proc = tkinter.Button(root, width=20, text=u"Запускаем процесс")
bt_proc.place(relx=0.5, rely=0.66, anchor="center")
bt_proc.bind("<ButtonRelease-1>", call_passive)

root.mainloop()