
import random

caracteres = {
    'caracteres_numeros' : "123456789",
    'caracteres_simbolos' : "@#$%&*?!",
    'caracteres_letras' : "abcdefghijklmnopqrstuvwxyz",
    'caracteres_letras_maiusculas' : "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    }


tamanho = 9


caractere_chave_aleatorio = random.choice(list(caracteres.keys()))
print(list(caracteres.keys()))
print(caractere_chave_aleatorio)
caractere_aleatorio = random.choice(caracteres[caractere_chave_aleatorio])
print(caracteres[caractere_chave_aleatorio])
print(caractere_aleatorio)

