c200  = 200
c100 = 100
c50 = 50
c20 = 20
c10 =10
c5 =5
c1 = 1

class Banco():
def sacar(qtd, dinheiro_sacado=0)
    dinheirof = float(qtd)
    while len(dinheirof) >= c200:
        dinheiro_sacado += c200
        print(f'Sacando {200}, total: {dinheiro_sacado}')
        dinheirof -= 200

    while len(dinheirof) >= c100:
        dinheiro_sacado += c100
        print(f'Sacando {200}, total: {dinheiro_sacado}')

        dinheirof -= 100

    while len(dinheirof) >= c50:
        dinheiro_sacado += c50
        print(f'Sacando {200}, total: {dinheiro_sacado}')

        dinheirof -= 50

    while len(dinheirof) >= c50:
        dinheiro_sacado += c50
        print(f'Sacando {200}, total: {dinheiro_sacado}')

        dinheirof -= 50

    while len(dinheirof) >= c50:
        dinheiro_sacado += c50
        print(f'Sacando {200}, total: {dinheiro_sacado}')

        dinheirof -= 50

    while len(dinheirof) >= c50:
        dinheiro_sacado += c1
        print(f'Sacando {200}, total: {dinheiro_sacado}')

        dinheirof -= 1

sacar(7372)