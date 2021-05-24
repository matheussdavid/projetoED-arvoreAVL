from musica import *
from feeder import *
from arvoreAVL import *

arvore = Arvore()
while True:
    print("1 - Inserir Música")
    print("2 - Buscar Música pelo ID")
    print("3 - Listar Músicas pelo ano")
    print("4 - Imprimir as músicas em ordem alfabética")
    print("5 - Exibir a altura da árvore")
    print("6 - Exibir a árvore")
    print("7 - Sair do programa")
    opcao = input("Informe o que opção desejada: ")
    if opcao == '1':
        print("Entre com as informações a respeito da música:")
        nome = str(input("Nome(s): "))
        album = str(input("album: "))
        ano = int(input("Ano: "))
        idMusica = int(input("IdMusica: "))
        musica = Musica(nome, album, ano, idMusica)
        teste = arvore.inserir(musica)
        if teste:
            print("Musica adicionada com sucesso: {}".format(musica.nome))
        else:
            print("Já existe uma música com o ID informado")
            
            
    elif opcao == '2':
        valor_idMusica = int(input("Informe o ID da música que deseja consultar: "))
        teste = encontraMusica(arvore, valor_idMusica)
        if teste == None:
            print("Nenhuma música foi encontrada para o ID informado\n")
        elif valor_idMusica == teste.idMusica:
            print("Musica encontrada!")
            print(f'Música: {teste}\n')
            
            
    elif opcao == '3':
        ano_Musica = int(input("Informe o ano da música que deseja consultar: "))
        musicas = encontra_ano(ano_Musica, arvore)
        if len(musicas) != 0:
            print("Músicas em ordem alfabética:")         
            for x in musicas:
                print(f'{x}')
        else:
            print("Não foram encontradas músicas para esse ano")
        lista  = []
                
    elif opcao == '4':
        print("Músicas em ordem alfabética: ")
        musicas = ordenarMusicas(arvore)   
        for x in musicas:
            print(f'{x}\n')
        musicasOrd  = []
            
            
    elif opcao == '5':
        altura = arvore.altura
        print(f'Altura da árvore: {altura}\n')
    elif opcao == '6':
        print(imprimirArvore(arvore))
        
    elif opcao == '7':
        break    
    elif opcao == '8':
        for musica in array_Musicas:
            arvore.inserir(musica) 
    else:
        print("Opção inválida, informar um valor entre os listados")