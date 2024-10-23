import os

def processar_resposta(resposta, nome):
    if   resposta == '1':
        print(f'{os.linesep}{nome}, Você escolheu a opção 1: Carros, Divertidamente, Elementos, Era do gelo. {os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome}, Você escolheu a opção 2: Pipoca, Doces/Balas, Salgadinhos, Hot Dog, Sanduiche. {os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome}, Você escolheu a opção 3: Primeira sessão começa as 12hs e a ultima começa as 22hs. {os.linesep}')
    else:
        print('Digite apenas 1,2 ou 3.')
        

def start():
    # Apresentar o chatbot
    print('Olá! Bem-vindo ao Cinema!')

    # Pedir o nome
    nome = input('Digite seu nome: ')
    
    while True:
     # Oferecer o menu de opções
     resposta = input(f'O que quer saber do cinema hoje ? {os.linesep} 1 - Quais são os filmes da semana ?{os.linesep} 2- Quais são os alimetos que contem no estabelecimento ?{os.linesep} 3- Que horas começam as sessões dos filmes ? ')

     # Processar a resposta enviada
     processar_resposta(resposta, nome)

if __name__ == '__main__':
    start()
