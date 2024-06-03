import time
import pyautogui
import pyperclip
from ahk import AHK
import senha as password

ahk = AHK(executable_path='C:/Program Files/AutoHotkey/v2/AutoHotkey64.exe')

mensagem = ''


def digitar_mensagem():
    mensagem = password.senha()
    pyperclip.copy(mensagem)
    pyautogui.hotkey('ctrl', 'v')



def gerarsenha():
    senha = password.senha()
    time.sleep(0.2)
    mensagem = f"Aqui está a sua senha de 9 caracteres: {senha} "
    ahk.send_input(mensagem)
    
   

ahk.add_hotkey('^1', callback=digitar_mensagem)
ahk.add_hotstring('gerarsenha', gerarsenha, options='*') 
ahk.start_hotkeys()
ahk.block_forever()

