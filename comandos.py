from random import randint


def criarMatriz(alt, lar, pxt=1):
    matriz = []
    for coluna in range(0, alt * pxt, pxt):
        for linha in range(0, lar * pxt, pxt):
            matriz.append((linha, coluna))
    return matriz
def criarFogo(matriz):
    fogo = {}
    for pos in matriz:
        if pos[1] == matriz[-1][1]:
            fogo[pos] = 36
        else:
            fogo[pos] = 0
    return fogo
def fogoProp(fogo):
    fogor = fogo
    for pos, fi in fogor.items:
        try:
            fogor[pos] = fogor[(pos[0], pos[1] - 1)] - randint(0, 5)
            if fogor[pos] < 0:
                fogor[pos] = 0
    print(fogor)
    return fogor