##Jogo de adivinhar número

import random
import numpy as np

# Função para obter a quantidade de dígitos do número a ser adivinhado
def introdução():
    digitos = int(input("Quantos dígitos? (Min 1) "))
    while digitos < 1:
        digitos = int(input("Quantidade inválida de dígitos, insira um valor igual ou maior a 1.\nQuantos dígitos? (Min 1) "))
    tamNum = np.arange(digitos)
    return tamNum

# Função para sortear um número aleatório
def sortearNum(tamNum):
    for i in tamNum:
        aleatorio = int(random.random() * 10)
        tamNum[tamNum == i] = aleatorio
    return tamNum

# Função para obter o chute do usuário
def chutar():
    chute = np.fromiter(input("Chute um valor! "), dtype=int)
    return chute

# Função para verificar quais dígitos estão na posição correta
def verificar_posicao_correta(numSorteado, chute):
    posicao_correta = []
    for i, num in enumerate(numSorteado):
        if num == chute[i]:
            posicao_correta.append(i)
    return posicao_correta

# Obter a quantidade de dígitos e sortear o número
tamNum = introdução()
numSorteado = sortearNum(tamNum.copy())
tamSorteado = len(numSorteado)

# Inicializar as tentativas como 1 e entrar em um loop até o usuário acertar o número sorteado
tentativas = 1
while (True):
    # Obter o chute do usuário
    chute = chutar()
    tamChute = len(chute)
    while tamChute != tamSorteado:
        print("O valor chutado não tem o mesmo tamanho do número sorteado.")
        chute = chutar()
        tamChute = len(chute)

    # Se o usuário acertou, sair do loop
    if (chute == numSorteado).all() == True:
        break
    
    # Inicializar a quantidade de dígitos na posição correta e na posição errada como 0
    posicaoCerta = 0
    numCerto = 0
    numSorteadoTemp = numSorteado.copy()
    
    # Verificar quais dígitos estão na posição correta
    posicao_correta = verificar_posicao_correta(numSorteado, chute)
    if len(posicao_correta) > 0:
        print("O(s) número(s) " + ", ".join(str(numSorteado[i]) for i in posicao_correta) + " está(ão) na posição correta!")
        posicaoCerta = len(posicao_correta)
        for i in posicao_correta:
            numSorteadoTemp[i] = 10
    
    # Verificar quais dígitos estão corretos, mas na posição errada
    for i in tamNum:
        for j in tamNum:            
            if chute[i] == numSorteadoTemp[j]:
                numCerto +=1
                numSorteadoTemp[j] = 10
                break
    tentativas += 1

    # Imprimir o resultado da tentativa
    if posicaoCerta > 0:
        print("Você acertou " + str(posicaoCerta) + " dos números!")
    if numCerto > 1:
        print(str(numCerto) + " números estão corretos, mas na posição errada!")
    elif numCerto == 1:
        print("1 número está correto, mas na posição errada!")
    if posicaoCerta == 0 and numCerto == 0:
        print("Nenhum dos números está correto!")

if tentativas > 1:
    print("Você acertou o número sorteado! em " + str(tentativas) + " tentativas!")
else:
    print("Você acertou o número sorteado! em " + str(tentativas) + " tentativas!70")