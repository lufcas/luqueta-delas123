escolha = input('oque deseja fazer [L]istar [A]pagar ou [I]nserir')

lista = []

if escolha == 'I' or escolha == 'i':
    item = input('oque deseja inserir na sua lista: ')
    lista.append(item)
    
if escolha == 'A' or escolha == 'a':
    