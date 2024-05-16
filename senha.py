import secrets
import string

# Definindo a lista de caracteres possíveis
caracteres = string.ascii_lowercase + string.ascii_uppercase + string.digits[1:] + '#@!*&$'

# Inicializando a sequência vazia
sequencia = ""

# Gerando o primeiro caractere (letra minúscula)
sequencia += secrets.choice(string.ascii_lowercase)
print(sequencia)
# Gerando o segundo caractere (letra maiúscula)
sequencia += secrets.choice(string.ascii_uppercase)
print(sequencia)
# Gerando o terceiro caractere (número)
sequencia += secrets.choice(string.digits[1:])
print(sequencia)
# Gerando o quarto caractere (símbolo)
sequencia += secrets.choice('#@!*&$')
print(sequencia)
# Definindo o tamanho desejado da sequência
tamanho_sequencia = 9

# Gerando o restante da sequência de caracteres aleatórios
while len(sequencia) < tamanho_sequencia:
    sequencia += secrets.choice(caracteres)

# Embaralhando a sequência para garantir aleatoriedade
sequencia_embaralhada = ''.join(secrets.choice(sequencia) for _ in range(len(sequencia)))

print(sequencia_embaralhada)
