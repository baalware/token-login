import json
import requests
from selenium import webdriver
import os
from colorama import Fore
from colorama import Style
from pystyle import *
import ctypes
from datetime import datetime
import sys
import sys

if not os.path.exists("chromedriver.exe"):
    res = requests.get("https://chromedriver.storage.googleapis.com/LATEST_RELEASE")
    ver = res.text
    download_url = "https://chromedriver.storage.googleapis.com/" + ver + "/chromedriver_win32.zip"
    print(f"baixe o {Fore.YELLOW}{download_url}{Fore.RESET}")
    exit()

title = "                                                                                 TOKEN LOGIN CREATED BY BAALWARE"
escape_sequence = "\033]2;{0}\x07".format(title)

sys.stdout.write(escape_sequence)

kernel32 = ctypes.windll.kernel32
console_handle = kernel32.GetConsoleWindow()

new_width = 800
ctypes.windll.user32.MoveWindow(console_handle, 0, 0, new_width, 600, True)

alpha = 250
hwnd = ctypes.windll.user32.GetForegroundWindow()
ex_style = ctypes.windll.user32.GetWindowLongW(hwnd, 95)
if (ex_style & 0x80000):
    ex_style ^= 0x80000
ctypes.windll.user32.SetWindowLongW(hwnd, 95, ex_style)
ctypes.windll.user32.SetLayeredWindowAttributes(console_handle, 0, alpha, 2)

os.system("cls")


baalware = """
          .                                                      .
        .n                   .                 .                  n.
  .   .dP                  dP                   9b                 9b.    .
 4    qXb         .       dX                     Xb       .        dXp     t
dX.    9Xb      .dXb    __                         __    dXb.     dXP     .Xb
9XXb._       _.dXXXXb dXXXXbo.                 .odXXXXb dXXXXb._       _.dXXP
 9XXXXXXXXXXXXXXXXXXXVXXXXXXXXOo.           .oOXXXXXXXXVXXXXXXXXXXXXXXXXXXXP
  `9XXXXXXXXXXXXXXXXXXXXX'~   ~`OOO8b   d8OOO'~   ~`XXXXXXXXXXXXXXXXXXXXXP'
    `9XXXXXXXXXXXP' `9XX'   DIE    `98v8P'  HUMAN   `XXP' `9XXXXXXXXXXXP'
        ~~~~~~~       9X.          .db|db.          .XP       ~~~~~~~
                        )b.  .dbo.dP'`v'`9b.odb.  .dX(
                      ,dXXXXXXXXXXXb     dXXXXXXXXXXXb.
                     dXXXXXXXXXXXP'   .   `9XXXXXXXXXXXb
                    dXXXXXXXXXXXXb   d|b   dXXXXXXXXXXXXb
                    9XXb'   `XXXXXb.dX|Xb.dXXXXX'   `dXXP
                     `'      9XXXXXX(   )XXXXXXP      `'
                              XXXX X.`v'.X XXXX
                              XP^X'`b   d'`X^XX
                              X. 9  `   '  P )X
                              `b  `       '  d'
                               `             ' \n                 
"""

def tokenLogin(token):
    opts = webdriver.ChromeOptions()
    opts.add_experimental_option("detach", True)
    driver = webdriver.Chrome('chromedriver.exe', options=opts)
    script = """
          function login(token) {
          setInterval(() => {
          document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
          }, 50);
          setTimeout(() => {
          location.reload();
          }, 2500);
          }
          """
    driver.get("https://discord.com/login")
    driver.execute_script(script + f'\nlogin("{token}")')

def processTokens():
    while True:
        os.system("cls")
        print(Colorate.Horizontal(Colors.red_to_yellow,Center.XCenter(baalware)))
        token = input("Token: ")
        if token.lower() == "sair":
            break
        tokenLogin(token)

print(Colorate.Horizontal(Colors.red_to_yellow,Center.XCenter(baalware)))

initialToken = input("Token: ")
tokenLogin(initialToken)
processTokens()
