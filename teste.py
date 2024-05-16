import time
import pyautogui
import pyperclip
from ahk import AHK


mensagem = "Hello World"


def digitar_mensagem():
    # time.sleep(0.9) 
    # pyautogui.typewrite(mensagem)
    pyperclip.copy(mensagem)
    pyautogui.hotkey('ctrl', 'v')

ahk = AHK(executable_path='D:/Diego/AutoHotKey/v2/AutoHotkey64.exe')

ahk.add_hotkey('^1', callback=digitar_mensagem)
ahk.start_hotkeys()  
ahk.block_forever()  

