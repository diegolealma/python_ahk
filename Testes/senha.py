import secrets
import string



def senha():
    # Definindo a lista de caracteres possíveis
    caracteres = string.ascii_lowercase + \
        string.ascii_uppercase + string.digits[1:] + '*#@$&&@#*$'

    # Inicializando a sequência com os caracteres obrigatórios
    sequencia = [
        secrets.choice(string.ascii_lowercase),  # letra minúscula
        secrets.choice(string.ascii_uppercase),  # letra maiúscula
        secrets.choice(string.digits[1:]),       # número
        secrets.choice('*#@$@#&&*$')                 # símbolo
    ]
    print(sequencia)
    # Definindo o tamanho desejado da sequência
    tamanho_sequencia = 9


    # Gerando o restante da sequência de caracteres aleatórios
    while len(sequencia) < tamanho_sequencia:
        sequencia.append(secrets.choice(caracteres))
    print(sequencia)
    # Embaralhando a sequência para garantir aleatoriedade
    secrets_generator = secrets.SystemRandom()
    secrets_generator.shuffle(sequencia)
    # Convertendo a lista em uma string
    sequencia_embaralhada = ''.join(sequencia)

    print(sequencia_embaralhada)
    return sequencia_embaralhada
