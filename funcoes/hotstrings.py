from resources.ahk_instance import ahk

def adicionar_hotstring_ahk(hotstring, texto):
    ahk.add_hotstring(hotstring, lambda: ahk.send_input(texto), options='*')