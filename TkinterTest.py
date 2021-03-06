# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.messagebox
from DegreeJudge import DegreeJudgeManager

window = tk.Tk()

window.title("DegreeSquence")
window.geometry('500x300')

e = tk.StringVar()
e2 = tk.Entry(window, show=None, font=('Arial', 14),textvariable = e)  # 显示成明文形式
e2.pack()

sequence = e.get()

def check_input():

    seq_list = sequence.split(',')

    for item in seq_list:
        if (item.isdigit() == False):
            tk.messagebox.showerror(message='输入格式错误')
            break



b = tk.Button(window, text='确认', font=('Arial', 12), width=10, height=1,command = check_input)
b.pack()

# 第6步，主窗口循环显示
window.mainloop()  # 消息循环是什么意思？
