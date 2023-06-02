senha = '12345'
cont = 4

for c in range(5):
    tentativa = input('Digite a senha: ')
    if tentativa == senha:
        print('Você acertou a senha')
        break
    else:
        print('Senha incorreta')
        print(f'Você usou {c+1} tentativas, lhe resta {cont} tentativas ')
        cont -=1
else:
    print('Você excedeu o numero de tentativas,Bloqueou a conta')