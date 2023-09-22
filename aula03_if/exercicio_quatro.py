"""
Exercicio 04

Escreva um programa que sempre escolhe o menor caminho a ser percorrido pelo usuário em
função do local onde se encontra e as opções de caminho a serem seguidas. O usuário sempre
parte do ponto A. O usuário deverá fornecer os valores de distância entre os pontos e o programa
deverá apresentar o caminho a ser percorrido e a distância, conforme o exemplo. Sua solução
deve utilizar apenas estruturas condicionais.
"""

escolhas = []
b = int(input("Digite a distancia de B: "))
c = int(input("Digite a distancia de C: "))
d = int(input("Digite a distancia de D: "))
e = int(input("Digite a distancia de E: "))
f = int(input("Digite a distancia de F: "))
g = int(input("Digite a distancia de G: "))

if b < c:
  escolhas.append(b)
  if d < e:
    escolhas.append(d)
  else:
    escolhas.append(e)

else:
  escolhas.append(c)
  if f < g:
    escolhas.append(f)
  else:
    escolhas.append(g)

print(escolhas)