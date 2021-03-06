# -*- coding: utf-8 -*-
import tkinter as tk
import tkinter.messagebox
class DegreeJudgeManager():
    # 从前端传入

    def __init__(self):
        pass

    def check_input(self,input_seq):
        '''
        输入检查，只允许非负整数，以逗号间隔，
        :param input_seq:输入序列
        :return:1 or 0
        '''

        seq_list = input_seq.split(',')

        for item in seq_list:
            if (item.isdigit() == False):
                tk.messagebox.showerror(message='输入格式错误')
                break
        return 1


    def get_seq(self,input_seq):
        '''
        得到前端输入的序列，以,划分
        :param input_seq: str:5,5,3,3,2,2,2
        :return:list[5,5,3,3,2,2,2]
        '''

        # 输入检测

        seq_list = input_seq()



    def decide_even(self, input_seq):
        pass

