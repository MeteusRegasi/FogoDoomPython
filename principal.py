from pygame import *
from comandos import *
from time import clock

#Definições da janela
tamanhoJanela = altura, largura = 1000, 1000
tela = display.set_mode(tamanhoJanela)
init()

#Define o fps
fps = clock()
#Define o pixel
pixel = (10, 10)

matriz = criarMatriz(100, 100, 10)
print(matriz)

#Loop
while True:
    #Aplica o fps
    fps
    #Loop de eventos
    for eventos in event.get():
        if evento.type == QUIT:
            exit