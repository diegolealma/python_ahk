import tkinter as tk
from tkinter import ttk, messagebox
from funcoes.senha import senha
from funcoes.hotstrings import adicionar_hotstring_ahk
from resources.ahk_instance import ahk


def on_button_click(senha_entry):
    senha_gerada = senha()
    senha_entry.delete(0, tk.END)
    senha_entry.insert(0, senha_gerada)
    messagebox.showinfo("Senha Gerada", "A senha foi gerada e enviada com sucesso!")

def adicionar_hotstring_interface(hotstring_entry, texto_hotstring_entry, hotstring_list):
    hotstring = hotstring_entry.get()
    texto = texto_hotstring_entry.get()
    if hotstring and texto:
        adicionar_hotstring_ahk(hotstring, texto)
        hotstring_list.insert('', 'end', values=(hotstring, texto))
        hotstring_entry.delete(0, tk.END)
        texto_hotstring_entry.delete(0, tk.END)
        messagebox.showinfo("Hotstring Adicionada", f"Hotstring '{hotstring}' adicionada com sucesso!")
    else:
        messagebox.showwarning("Entrada Inválida", "Por favor, insira valores válidos para a hotstring e o texto.")

def iniciar_interface():
    root = tk.Tk()
    root.title("Gerador de Senhas")

    notebook = ttk.Notebook(root)
    notebook.pack(padx=10, pady=10, expand=True)

    frame_gerar_senha = ttk.Frame(notebook, padding=10)
    notebook.add(frame_gerar_senha, text='Gerar Senha')

    label = tk.Label(frame_gerar_senha, text="Clique no botão para gerar uma senha:")
    label.pack(pady=5)

    senha_entry = tk.Entry(frame_gerar_senha, width=30)
    senha_entry.pack(pady=5)

    button = tk.Button(frame_gerar_senha, text="Gerar Senha", command=lambda: on_button_click(senha_entry))
    button.pack(pady=5)

    frame_campo_editavel = ttk.Frame(notebook, padding=10)
    notebook.add(frame_campo_editavel, text='Campo Editável')

    label_texto = tk.Label(frame_campo_editavel, text="Texto Teste:")
    label_texto.grid(row=0, column=0, padx=5, pady=5, sticky='w')

    texto_entry = tk.Entry(frame_campo_editavel, width=30)
    texto_entry.grid(row=0, column=1, padx=5, pady=5)

    label_hotstring = tk.Label(frame_campo_editavel, text="Hotstring:")
    label_hotstring.grid(row=1, column=0, padx=5, pady=5, sticky='w')

    hotstring_entry = tk.Entry(frame_campo_editavel, width=30)
    hotstring_entry.grid(row=1, column=1, padx=5, pady=5)

    label_texto_hotstring = tk.Label(frame_campo_editavel, text="Texto da Hotstring:")
    label_texto_hotstring.grid(row=2, column=0, padx=5, pady=5, sticky='w')

    texto_hotstring_entry = tk.Entry(frame_campo_editavel, width=30)
    texto_hotstring_entry.grid(row=2, column=1, padx=5, pady=5)

    button_add_hotstring = tk.Button(frame_campo_editavel, text="Adicionar Hotstring", command=lambda: adicionar_hotstring_interface(hotstring_entry, texto_hotstring_entry, hotstring_list))
    button_add_hotstring.grid(row=3, columnspan=2, pady=10)

    hotstring_list = ttk.Treeview(frame_campo_editavel, columns=('Hotstring', 'Texto'), show='headings')
    hotstring_list.heading('Hotstring', text='Hotstring')
    hotstring_list.heading('Texto', text='Texto')
    hotstring_list.grid(row=4, columnspan=2, padx=5, pady=5, sticky='nsew')

    root.mainloop()
