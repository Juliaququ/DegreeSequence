# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.messagebox
from DegreeJudge import DegreeJudgeManager

window = tk.Tk()

window.title("DegreeSquence")
window.geometry('500x300')

tk.Label(window, text='请输入度序列，以逗号间隔，如：7,7,6,6,3,2',font=('Arial', 12), ).place(x=19, y=35)
userName = tk.StringVar()
tk.Entry(window, highlightthickness=1, textvariable=userName).place(x=20, y=60, width=320, height=30)

def check_input():
    seq_list = userName.get().split(',')
    print(seq_list)
    for item in seq_list:
        if (item.isdigit() == False):
            tk.messagebox.showerror(message='输入格式错误')
            break

    pass

b = tk.Button(window, text='确认', font=('Arial', 12), width=10, height=1, command=check_input).place(x = 20,y = 100)


# 第6步，主窗口循环显示
window.mainloop()  # 消息循环是什么意思？
