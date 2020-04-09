from pygame import *
from comandos import *
from time import clock


#Definições da janela
tamanhoJanela = altura, largura = 100, 100
tela = display.set_mode(tamanhoJanela)
#init()

#Define o fps
fps = clock()
#Define o pixel
pixel = (1, 1)

#Define as posições do fogo
matriz = criarMatriz(10, 10, 1)
#Coloca um valor de 0 a 36 em cada valor
fogo = criarFogo(matriz)

fogo = fogoProp(fogo)
print(fogo)

"""
#Loop
while True:
    #Aplica o fps
    fps
    #Loop de eventos
    for eventos in event.get():
        if eventos.type == QUIT:
            exit"""