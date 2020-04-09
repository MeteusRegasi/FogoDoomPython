def criarMatriz(alt, lar, pxt):
    matriz = []
    for coluna in range(0, alt * pxt, pxt):
        for linha in range(0, lar * pxt, pxt):
            matriz.append((linha, coluna))
    return matriz