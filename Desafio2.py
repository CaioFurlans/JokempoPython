from random import randint

pedra = 1
papel = 2
tesoura = 3

numAleat = randint(1,3)

nomeUsu = str(input('Digite o seu nome: '))
print(f'Bem Vindo {nomeUsu} ')

usuJoga = int(input('Digite um numero entre 1 e 3: '))

if usuJoga == 1 and numAleat == 1:
    print('Empate')
elif usuJoga == 1 and numAleat == 2:
    print('PC ganhou')
elif usuJoga == 1 and numAleat == 3:
    print(f'{nomeUsu} ganhou')

elif usuJoga == 2 and numAleat == 1:
    print(f'{nomeUsu} ganhou')
elif usuJoga == 2 and numAleat == 2:
    print('Empate')
elif usuJoga == 2 and numAleat == 3:
    print('PC ganhou')

elif usuJoga == 3 and numAleat == 1:
    print('PC ganhou')
elif usuJoga == 3 and numAleat == 2:
    print(f'{nomeUsu} ganhou')
elif usuJoga == 3 and numAleat == 3:
    print('Empate')
