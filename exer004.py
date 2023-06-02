numtxt = input('Digite um numero: ')

if numtxt.isnumeric():
    num = int(numtxt)

    while num != -1:
        print(num)
        num = num - 1

else:
    print('Não é inteiro')