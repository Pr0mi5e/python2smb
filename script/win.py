#coding=utf-8

#!/usr/bin/python

import os
import json
import time
import win32gui
import win32api
import win32con
from pykeyboard import PyKeyboard
import pydirectinput


config = json.load(open("./config.json", 'rb'))
print(config['path'])
path = config["path"]
account = config['account']
pwd = config['pwd']
def login():
  # os.system(path)
  # time.sleep(5)

  # handle = win32gui.FindWindow(None, 'QQ')
  # print(handle)
  # #获取QQ登录窗口的位置
  # loginid = win32gui.GetWindowPlacement(handle)
  # print (loginid)
  # b = win32gui.GetDlgItem(handle, 00000000)
  # print('b', b)
  # ctrlid=win32gui.GetDlgCtrlID(b)
  # print('ctrlid', ctrlid)
  # #获取某个句柄的类名和标题
  # # title = win32gui.GetWindowText(handle)
  # # clsname = win32gui.GetClassName(handle)
  # # print(title, clsname)
  # # list = get_windows()
  # list = get_child_windows(handle)
  # # print(list)
  # for i in list:
  #   print(i)
  #   sub = win32gui.GetWindowPlacement(i)
  #   print (sub)
  #   #获取某个句柄的类名和标题
  #   sub_title = win32gui.GetWindowText(i)     
  #   sub_clsname = win32gui.GetClassName(i)
  #   print(sub_title, sub_clsname)
  # get_child_windows(handle)
  # get_title(handle)
  # 搜索子窗口
  # 枚举子窗口
  # hwndChildList = []     
  # win32gui.EnumChildWindows(handle, lambda hwnd, param: param.append(hwnd),  hwndChildList)
  # subHandle = win32api.FindWindowEx(handle, 0, "Button", None)
  # print('subHandle')
  # print(subHandle)
  
  # win32gui.PostMessage(subHandle, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, 0)

  # win32gui.PostMessage(subHandle, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, 0)

  # 根据控件id 0x3F8
  # E_Ssymbol = win32gui.GetDlgItem(F_Bentrust, 00000000)
  # buff =ctypes.create_unicode_buffer(64)
  # win32gui.SendMessage(E_Ssymbol, win32con.WM_GETTEXT, 32, buff)
  # print (buff.value)
  # w=win32ui.FindWindow(clsname,windowtitle)
  
  # b=win32gui.GetDlgCtrlID(list[0])
  # b.postMessage(win32con.BM_CLICK)

  # # 获得窗口的菜单句柄
  # menuHandle = win32gui.GetMenu(subHandle)
  # # 获得子菜单或下拉菜单句柄   
  # # 参数：菜单句柄 子菜单索引号
  # subMenuHandle = win32gui.GetSubMenu(menuHandle, 0)
  # # 获得菜单项中的的标志符，注意，分隔符是被编入索引的  
  # # 参数：子菜单句柄 项目索引号
  # menuItemHandle = win32gui.GetMenuItemID(subMenuHandle, 0)
  # print(menuItemHandle)




  # print (loginid[4][0])
  # print (loginid[4][1])
  #定义一个键盘对象
  # k = PyKeyboard()
  #把鼠标放置到登陆框的输入处
  # #按下鼠标再释放
  win32api.SetCursorPos([860,600])
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0) # press mouse
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0) # release mouse
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0) # press mouse
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0) # release mouse
  time.sleep(2)
  # win32api.SetCursorPos([880,600])
  # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0) # press mouse
  # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0) # release mouse
  time.sleep(2)
  # win32api.SetCursorPos([920,600])
  # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0) # press mouse
  # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0) # release mouse
  # time.sleep(2)
  # win32api.SetCursorPos([1040,600])
  # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0) # press mouse
  # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0) # release mouse
  pydirectinput.moveTo(920, 600)
  pydirectinput.click()
  # k.type_string()
  # win32api.SetCursorPos([loginid[4][0]+192,loginid[4][1]+280])
  # #按下鼠标再释放
  # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0) # press mouse
  # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0) # release mouse
  # k.type_string(pwd)
  # win32api.SetCursorPos([loginid[4][0]+192,660])
  #按下鼠标再释放
  # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0) # press mouse
  # win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0) # release mouse
  # win32api.keybd_event(13,0,0,0)
  # win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)
  # pos = win32gui.GetCursor()
  # print('pos', pos)


def open_app(app_dir):
  os.startfile(app_dir)

def get_windows():
  hwnd_list = []
  win32gui.EnumWindows(lambda hWnd, param: param.append(hWnd), hwnd_list)
  print(hwnd_list)
  return hwnd_list

def get_child_windows(parent):
  hwnd_child_list = []
  win32gui.EnumChildWindows(parent, lambda hWnd, param: param.append(hWnd), hwnd_child_list)
  print(hwnd_child_list)
  # if (hwnd_child_list[0]):
    # get_child_windows(hwnd_child_list[0])
  # get_title(hwnd_child_list)
  return hwnd_child_list

def get_title(hwnd):
  title = win32gui.GetWindowText(hwnd)
  print('窗口标题：%s' %(title))
  return title

if __name__ == "__main__":

  app_dir = path
  login()
  # open_app(app_dir)
