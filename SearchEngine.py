"""
Aluno: Rafael Sávio Loureiro de Oliveira
Criado em Sábado Outubro 30 09:29:02 2020

"""

import lib_trata_dados as tratarDados
import os
from os.path import isfile, join

print('\n***** Bem vindo ao SearchEngine *****\n')

vermelho = '\033[91m'
amarelo = '\033[33m'
sucesso = '\33[32m'
end = '\033[0m'
finalizar = False

while finalizar == False:

    opcao = str(tratarDados.validaOpcaoMenuPrincipal())

    if opcao == '1':
        finalizarCriacao = False

        while finalizarCriacao != True:

            arquivos = [f for f in os.listdir('FilesToSearch/') if isfile(join('FilesToSearch/', f))]
            print('\nAqui está a lista de arquivos já existentes:\n')
            for arquivo in arquivos:
                print(arquivo.strip(".txt"))

            userInput = input('\nDigite o nome do arquivo que deseja criar? ')
            response = tratarDados.criar_arquivo(userInput)

            if response == False:
                print('\n' + vermelho + 'Arquivo já existente' + end + '\n')
            else:
                print(sucesso + f'\n{userInput} criado com sucesso!\n' + end)

            continuar = tratarDados.validaOpcaoInterno()

            if continuar == '0':
                finalizarCriacao = True


    elif opcao == '2':
        finalizarPesquisa = False

        while finalizarPesquisa != True:
            termos = str(input("Entre com os termos a serem pesquisados (separados por espaço):"))
            mapaDePalavras = tratarDados.pesquisar_termos(termos)
            mapaVazio = not bool(mapaDePalavras) 

            if mapaVazio == True:
                print('\n' + vermelho + 'Termo não encontrado' + end + '\n')
            else:
                for termoRelevancia in mapaDePalavras:
                    print(amarelo ,'\nArquivo:',termoRelevancia[0],'->', 'Relevância:', termoRelevancia[1], end)

            continuar = tratarDados.validaOpcaoInterno()

            if continuar == '0':
                finalizarPesquisa = True

    elif opcao == '3':
        finalizarInsercao = False

        while finalizarInsercao != True:
            arquivos = [f for f in os.listdir('FilesToSearch/') if isfile(join('FilesToSearch/', f))]
            print('\nAqui está a lista de arquivos disponíveis:\n')
            for arquivo in arquivos:
                print(arquivo.strip(".txt"))

            arq = input('\nDigite o nome do arquivo (sem extensão .txt): ')
            word = input('\nDigite o termo que deseja inserir: ')
            qtda = input('\nQuantas vezes? ')
            tratarDados.inserir_termos(arq, word, qtda)

            continuar = tratarDados.validaOpcaoInterno()

            if continuar == '0':
                finalizarInsercao = True

    elif opcao == '4':
        finalizarLeitura = False

        while finalizarLeitura != True:
            arquivos = [f for f in os.listdir('FilesToSearch/') if isfile(join('FilesToSearch/', f))]
            print('\nAqui está a lista de arquivos disponíveis:\n')
            for arquivo in arquivos:
                print(arquivo.strip(".txt"))      

            entrada = input('\nDigite o nome do arquivo que deseja ler (sem extensão .txt): ')
            arq = tratarDados.ler_arquivo(entrada)
            vazio = not bool(arq) 
            if vazio == True:
                print(vermelho + '\nArquivo inexistente, digite o nome de um arquivo disponível.' + end)
            else:
                for a in arq:
                    print(*a, sep=', ')
            
            continuar = tratarDados.validaOpcaoInterno()

            if continuar == '0':
                finalizarLeitura = True

    elif opcao == '0':
        finalizar = True

