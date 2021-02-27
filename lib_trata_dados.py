"""
Aluno: Rafael Sávio Loureiro de Oliveira
Criado em Sábado Outubro 30 20:33:32 2020

"""

import os
from collections import Counter

falha = '\033[91m'
sucesso = '\33[32m'
end = '\033[0m'

def inserir_termos(nomeArq, termo, quantidade):
    nomeDoArquivo = 'FilesToSearch/' + str(nomeArq) + '.txt'
    termo = str(termo).upper()

    try:
        quantidade = int(quantidade)
    except ValueError:
        print('Quantidade não é um inteiro!')

    arquivo = open(nomeDoArquivo, 'a+')
    arquivo.writelines((termo + ' \n') * quantidade)
    print('\n' + sucesso + f'{termo} inserido com sucesso' + end)
    arquivo.close()
    
def pesquisar_termos(termos):
    termosUpper = termos.upper()
    termosEntrada = termosUpper.split()
    listaArquivos = os.listdir('FilesToSearch/')
    mapeamento = dict()
    listaTermos = []

    for termo in termosEntrada:
        for arquivo in listaArquivos:
            try:
                with open('FilesToSearch/' + arquivo, 'r+') as file:
                    listaTermos = file.read().split()
                    numeroDeTermos = listaTermos.count(termo)
                    if numeroDeTermos != 0:
                        try:
                            mapeamento[arquivo] = mapeamento[arquivo] + numeroDeTermos
                        except KeyError:
                            mapeamento[arquivo] = numeroDeTermos
                    file.close()
            except FileNotFoundError:
                print('Não encontramos esse arquivo')
    mapeamento = sorted(mapeamento.items(), key=lambda x: x[1], reverse=True)
    return mapeamento


def ler_arquivo(nomeDoArquivo):
    arquivoEntrada = 'FilesToSearch/' + str(nomeDoArquivo) + '.txt'
    listaTermos = []

    try:
        arquivo = open(arquivoEntrada, 'r+')
        with open(arquivoEntrada) as file:
            listaTermos.append([word for line in file for word in line.split()])
        arquivo.close()

    except FileNotFoundError:
        pass
    return listaTermos


def criar_arquivo(nomeDoArquivo):
    arquivoEntrada = 'FilesToSearch/' + str(nomeDoArquivo) + '.txt'

    try:
        arquivo = open(arquivoEntrada, 'r+')
        return False
    except FileNotFoundError:
        arquivo = open(arquivoEntrada, 'w+')
    arquivo.close()
    return True


def validaOpcaoMenuPrincipal():
    listaOpcoes = ['1','2','3','4','0']

    while True:
        validacao = str(input('\nEscolha uma das opções abaixo:\n\n[1] - Criar arquivo\n[2] - Pesquisar por termos\n[3] - Inserir termo em arquivo\n[4] - Ler arquivo completo\n[0] - Sair\n\n'))

        if validacao not in listaOpcoes:
            print(falha + '\nValor inválido, tente novamente' + end)
        else:
            break
    return validacao


def validaOpcaoInterno():
    listaOpcoes = ['1','0']

    while True:
            print('\nDeseja fazer a mesma ação novamente? \n')
            validacao = str(input("""[1] - Sim\n[0] - Não\n\n"""))

            if validacao not in listaOpcoes:
                print(falha + '\nValor inválido, tente novamente' + end)
            else:
                break
    return validacao
