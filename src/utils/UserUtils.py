# -*- coding:utf-8 -*-
import sys
import time
import os
from os import sep
from tkinter import filedialog, Tk, TclError


def choose_directory():
    """
    请用户在对话框中选择要处理的文件夹

    如果当前系统不支持对话框，则让用户输入

    Returns:
        用户选择的目录路径
    """
    print('请选择要处理的文件夹: ', end='')
    for _ in range(2):
        try:
            tk = Tk()
            tk.withdraw()
            dir_choose = filedialog.askdirectory()
            if dir_choose == '':
                print('你没有选择目录! 请重新选: ')
                time.sleep(2)
                continue
            else:
                print(dir_choose)
                # askdirectory()得到的是正斜杠，替换为系统默认路径分隔符
                return dir_choose.replace('/', sep)

        # 没有图形界面的系统，让用户输入路径
        except TclError:
            try:
                dir_choose = input("请输入你需要整理的文件夹路径: ")
            except KeyboardInterrupt:
                sys.exit('输入终止，马上退出！')

            if not os.path.exists(dir_choose) or not os.path.isdir(dir_choose):
                print('不存在当前目录或者输入错误，请重新输入:', dir_choose)
                time.sleep(2)
                continue
            else:
                print(dir_choose)
                return dir_choose

    input('你可能不需要我了，请关闭我吧！')


def choose_file():
    """
        请用户在对话框中选择要处理的文件夹

        如果当前系统不支持对话框，则让用户输入

        Returns:
            用户选择的文件路径
        """
    print('请选择要处理的文件夹: ', end='')
    for _ in range(2):
        try:
            tk = Tk()
            tk.withdraw()
            path_choose = filedialog.askopenfilename()
            if path_choose == '':
                print('你没有选择目录! 请重新选: ')
                time.sleep(2)
                continue
            else:
                print(path_choose)
                # askdirectory()得到的是正斜杠，替换为系统默认路径分隔符
                return path_choose.replace('/', sep)

        # 没有图形界面的系统，让用户输入路径
        except TclError:
            try:
                path_choose = input("请输入你需要整理的文件夹路径: ")
            except KeyboardInterrupt:
                sys.exit('输入终止，马上退出！')

            if not os.path.exists(path_choose) or not os.path.isdir(path_choose):
                print('不存在当前目录或者输入错误，请重新输入:', path_choose)
                time.sleep(2)
                continue
            else:
                print(path_choose)
                return path_choose

    input('你可能不需要我了，请关闭我吧！')
