dinheiro = input('Quanto dinheiro voce tem agora para sacar: ')
dinheirof = float(dinheiro)

c200  = 200
c100 = 100
c50 = 50
c20 = 20
c10 =10
c5 =5
c1 = 1

def sacar(qtd, dinheiro_sacado=0)
    dinheirof = float(qtd)
    while len(dinheirof) >= c200:
        dinheiro_sacado += c200
        dinheirof -= 200

    while len(dinheirof) >= c100:
        dinheiro_sacado += c100
        dinheirof -= 100

    while len(dinheirof) >= c50:
        dinheiro_sacado += c50
        dinheirof -= 50

    while len(dinheirof) >= c50:
        dinheiro_sacado += c50
        dinheirof -= 50

    while len(dinheirof) >= c50:
        dinheiro_sacado += c50
        dinheirof -= 50

    while len(dinheirof) >= c50:
        dinheiro_sacado += c1
        dinheirof -= 1