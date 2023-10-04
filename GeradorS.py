# Gerador de Senhas

from random import choice
import string

print('><' * 30)
print('GERADOR DE SENHAS'. center(60))
print('><' * 30)

valores = string.ascii_letters # Minusculas e Maiusculas
valores += string.digits # Nemeros de 0 a 9
valores += string.punctuation # vai juntar com os caracteres especiais

senha = ""

tamanho = int(input('Qual o tamanho de sua senha: '))

# para item de 0 o tamanho senha vai receber um valor do conjunto valores
for i in range(0, tamanho):
  senha += choice(valores)

print(f'Sua senha é: {senha}')