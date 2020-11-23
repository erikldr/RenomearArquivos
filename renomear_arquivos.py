import os ## Biblioteca necessaria

for arquivo in os.listdir('./hora'):   
    nome = str(arquivo).split(".") ## Separa o nome da extensão do arquivo
    numero = nome[0] ## Salva o nome para manipulação
    parte1 = int(numero[:2]) + 12 ## manipulação feita em um caso onde precisava-se modificar ex:(hora 01:10 para 13:10)
    novo_nome  = str(parte1) + numero[2:] + ".mp3" ## Novo nome do arquivo 
    
    os.rename("./hora/"+nome, "./hora/"+novo_nome)
    print("arquivo " + nome + " alterado para " + novo_nome) ## mostra os arquivos que foram alterados