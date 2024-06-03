import time
import pyautogui
import pyperclip
from ahk import AHK
import senha as password
import tkinter as tk
from tkinter import ttk, messagebox

# Inicializa o AHK
ahk = AHK(executable_path='C:/Program Files/AutoHotkey/v2/AutoHotkey64.exe')


ahk.start_hotkeys()

# Função chamada ao clicar no botão
def on_button_click():
    senha = password.senha()
    senha_entry.delete(0, tk.END)
    senha_entry.insert(0, senha)
    messagebox.showinfo("Senha Gerada", "A senha foi gerada e enviada com sucesso!")

# Função para adicionar uma nova hotstring
def adicionar_hotstring():
    hotstring = hotstring_entry.get()
    texto = texto_hotstring_entry.get()
    if hotstring and texto:
        ahk.add_hotstring(hotstring, lambda: ahk.send_input(texto), options='*')
        hotstring_list.insert('', 'end', values=(hotstring, texto))
        hotstring_entry.delete(0, tk.END)
        texto_hotstring_entry.delete(0, tk.END)
        messagebox.showinfo("Hotstring Adicionada", f"Hotstring '{hotstring}' adicionada com sucesso!")
    else:
        messagebox.showwarning("Entrada Inválida", "Por favor, insira valores válidos para a hotstring e o texto.")

# Criação da Interface Gráfica
root = tk.Tk()
root.title("Gerador de Senhas")

# Criação do Notebook (Abas)
notebook = ttk.Notebook(root)
notebook.pack(padx=10, pady=10, expand=True)

# Frame para a aba de geração de senha
frame_gerar_senha = ttk.Frame(notebook, padding=10)
notebook.add(frame_gerar_senha, text='Gerar Senha')

label = tk.Label(frame_gerar_senha, text="Clique no botão para gerar uma senha:")
label.pack(pady=5)

# Entrada para a senha gerada
senha_entry = tk.Entry(frame_gerar_senha, width=30)
senha_entry.pack(pady=5)

button = tk.Button(frame_gerar_senha, text="Gerar Senha", command=on_button_click)
button.pack(pady=5)

# Frame para a aba de campo editável e hotstrings
frame_campo_editavel = ttk.Frame(notebook, padding=10)
notebook.add(frame_campo_editavel, text='Campo Editável')

# Entrada para texto arbitrário
label_texto = tk.Label(frame_campo_editavel, text="Texto Teste:")
label_texto.grid(row=0, column=0, padx=5, pady=5, sticky='w')

texto_entry = tk.Entry(frame_campo_editavel, width=30)
texto_entry.grid(row=0, column=1, padx=5, pady=5)

# Entrada para a hotstring
label_hotstring = tk.Label(frame_campo_editavel, text="Hotstring:")
label_hotstring.grid(row=1, column=0, padx=5, pady=5, sticky='w')

hotstring_entry = tk.Entry(frame_campo_editavel, width=30)
hotstring_entry.grid(row=1, column=1, padx=5, pady=5)

# Entrada para o texto da hotstring
label_texto_hotstring = tk.Label(frame_campo_editavel, text="Texto da Hotstring:")
label_texto_hotstring.grid(row=2, column=0, padx=5, pady=5, sticky='w')

texto_hotstring_entry = tk.Entry(frame_campo_editavel, width=30)
texto_hotstring_entry.grid(row=2, column=1, padx=5, pady=5)

# Botão para adicionar a hotstring
button_add_hotstring = tk.Button(frame_campo_editavel, text="Adicionar Hotstring", command=adicionar_hotstring)
button_add_hotstring.grid(row=3, columnspan=2, pady=10)

# Lista para exibir hotstrings adicionadas
hotstring_list = ttk.Treeview(frame_campo_editavel, columns=('Hotstring', 'Texto'), show='headings')
hotstring_list.heading('Hotstring', text='Hotstring')
hotstring_list.heading('Texto', text='Texto')
hotstring_list.grid(row=4, columnspan=2, padx=5, pady=5, sticky='nsew')

# Adicionando a hotstring "go" e o texto "gauuuuuuuuuuu" como exemplo
hotstring_entry.insert(0, 'go')
texto_hotstring_entry.insert(0, 'gauuuuuuuuuuu')

root.mainloop()

ahk.block_forever()
