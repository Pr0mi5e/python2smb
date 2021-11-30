#coding=utf-8

#!/usr/bin/python

import os
import json
import time
import win32gui
import win32api
import win32con
from pykeyboard import PyKeyboard


config = json.load(open("./config.json"))
print(config['path'])
path = config["path"]
qq = config['qq']
pwd = config['pwd']
def login():
  os.system(path)
  time.sleep(5)

  a = win32gui.FindWindow(None, 'QQ')
  #获取QQ登录窗口的位置
  loginid = win32gui.GetWindowPlacement(a)
  print (loginid)
  print (loginid[4][0])
  print (loginid[4][1])
  #定义一个键盘对象
  k = PyKeyboard()
  #把鼠标放置到登陆框的输入处
  win32api.SetCursorPos([loginid[4][0]+192,loginid[4][1]+112])
  #按下鼠标再释放
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0) # press mouse
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0) # release mouse
  k.type_string(qq)
  win32api.SetCursorPos([loginid[4][0]+192,loginid[4][1]+280])
  #按下鼠标再释放
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0,0,0) # press mouse
  win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0,0,0) # release mouse
  k.type_string(pwd)
  win32api.keybd_event(13,0,0,0)
  win32api.keybd_event(13,0,win32con.KEYEVENTF_KEYUP,0)


def open_app(app_dir):

  os.startfile(app_dir)

if __name__ == "__main__":

  app_dir = path
  login()
  # open_app(app_dir)
