'''
Autor: Clarissa Cruz
Data: 30/10/2024
'''
#Escreva um programa que recebe um inteiro e diga se é par ou ímpar. 
# Use o operador matemático % (resto da divisão ou módulo) e o teste condicional if.

numero = int(input('Digite um número inteiro: '))

if numero %2 == 0:
    print('É um número par!')
else:
    print('É um número impar')