produtos = []
print('Bem vindo ao estoque')

while True:
    print('1 - adicionar item ao estoque\n2 - Atualizar quantidade de items já existente\n3 - Verificar a disponibilidade dos produtos\n4 - Listar items por nome\n5 - Remover item\n6 - Sair')
    escolha = int(input('Escolha: '))
    match escolha:
        case 1:
            p = {}
            p['nome'] = input('Digite o nome do produto: ')
            p['preco'] = float(input('Digite o preço do produto: '))
            p['quantidade'] = int(input('A quantidade em estoque: '))
            produtos.append(p)
        case 2:
            atualizar = int(input(f'Digite o indice do produto de 0 a {len(produtos)-1}: '))
            print(f'{produtos[atualizar]["nome"]} foi selecionado')
            a2 = int(input('Digite a quantidade do estoque: '))
            produtos[atualizar]["quantidade"] = a2
        case 3:
            indice = int(input(f'Digite o indice do produto de 0 a {len(produtos)-1}: '))
            print(f'O produto {produtos[indice]["nome"]} tem {produtos[indice]["quantidade"]} unidade')
        case 4:
            lista_ordenada = sorted(produtos, key=lambda item: item['nome'])
            for v,d in enumerate(lista_ordenada):
                print(f'{v}    O {d["nome"]} tem {d["quantidade"]} quantidade e custam {d["preco"]} cada')
        case 5:
            deletar = int(input(f'Digite o indice do produto de 0 a {len(produtos)-1}: '))
            print(f'O produto {produtos[deletar]["nome"]} foi apagado com sucesso')
            del produtos[deletar]
        case 6:
            break
        case _:
            print('Opção inexistente')

quantidade = 0
valor = 0

for c in produtos:
    quantidade += c['quantidade']
    valor += c['preco']


print(f'O estoque tem {quantidade} produtos\nAo todo custam {valor}')

