import secrets
import string

def senha(tamanho=9):
    # Verifica se o tamanho está dentro do intervalo válido (4-40)
    if tamanho < 4 or tamanho > 40:
        raise ValueError("O tamanho da senha deve estar entre 4 e 40 caracteres.")

    # Definindo a lista de caracteres possíveis
    caracteres = string.ascii_letters + string.digits + '*#@$&&@#*$'

    # Inicializando a sequência com os caracteres obrigatórios
    sequencia = [
        secrets.choice(string.ascii_lowercase),  # letra minúscula
        secrets.choice(string.ascii_uppercase),  # letra maiúscula
        secrets.choice(string.digits),           # número
        secrets.choice('*#@$&&@#*$')             # símbolo
    ]

    # Gerando o restante da sequência de caracteres aleatórios
    while len(sequencia) < tamanho:
        sequencia.append(secrets.choice(caracteres))

    # Embaralhando a sequência para garantir aleatoriedade
    secrets.SystemRandom().shuffle(sequencia)

    # Convertendo a lista em uma string
    sequencia_embaralhada = ''.join(sequencia)

    return sequencia_embaralhada
