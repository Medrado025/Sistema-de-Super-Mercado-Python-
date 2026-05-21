from time import sleep
from colorama import  Fore, Style
#===========================
#  SISTEMA DE MERCADO
#===========================
produtos = []

def cabeçalho (titulo):
    print("\n" + "=" * 40)
    print(Fore.GREEN + f'  {titulo}' + Style.RESET_ALL)
    print("=" * 40)

def cadastras_produto():
    cabeçalho('📃 CADASTRAR PRODUTO')

    nome = input('Nome do produto: ').strip()
    if not nome:
        print('⚠️ Nome não pode ser vazio. ')
        return

    while True:
        try:
            preco = float(input('Preço R$: ').replace(',' , '.'))
            if preco < 0:
                print('Preço não poder ser Negativo')
                continue
            break

        except ValueError:
            print('⚠️ Valor Invalido (EX: 19.99)')
    produtos.append({'nome': nome, 'preco': preco})
    print(f'Produto {nome } Cadastrado Com sucesso! 💾')

def listar_produtos():
    cabeçalho('📜 LISTA DE PRODUTOS')

    if not produtos:
        print('⚠️ Nenhum Produto Cadastrado!!')
        return
    print(f'{'#':<4}{'Produto':<25} {'Preço':<10}')
    print(' ' + '-' * 42)
    for i, p in enumerate(produtos , 1):
        print(f'{i:> 4} {p['nome']:<25} R${p['preco']:>8.2f}')

def total_carrinho():
    cabeçalho('💲 VALOR TOTAL')
    if not produtos:
        print('⚠️ Carrinho Vazio')
        return
    total = sum(p['preco'] for p in produtos)
    print(f' Total de {len(produtos)} Produto(s): R${total:.2f}')

def produto_mais_barato():
    cabeçalho('〽️ PRODUTO MAIS BARATO')

    if not produtos:
        print('⚠️ Não á produto cadastrado')
        return

    barato = min(produtos , key=lambda p : p['preco'])
    print(f' {barato['nome']} -> R${barato['preco']:.2f}')

def produtos_acima_de_mil():
    cabeçalho('💹 PRODUTOS ACIMA DE ACIMA DE MIL REAIS')

    caros = [p for p in produtos if p['preco'] > 1000]

    if not caros:
        print('⚠️ Não á Produtos acima de R$: 1.000,00')
        return

    for p in caros:
        print(f' {p['nome']:<25} R${p['preco']:.2f}')

def menu():
    cabeçalho('🛒 SISTEMA DO SUPER MERCADO')
    print(Fore.BLUE + '[1] Cadastrar produto\n'
          '[2] Lista Produtos\n'
          '[3] Ver Total\n'
          '[4] Produtos mais Barato\n'
          '[5] Produtos acima De R$1.000\n'
          '[0] Sair' + Style.RESET_ALL)
    print('-' * 40)
    return input('Escolha uma opção: ').strip()


while True:
    opcao = menu()

    if opcao == '1':
        cadastras_produto()
    elif opcao == '2':
        listar_produtos()
    elif opcao == '3':
        total_carrinho()
    elif opcao == '4':
        produto_mais_barato()
    elif opcao == '5':
        produtos_acima_de_mil()
    elif opcao == '0':
        break
    else:
        print('Comando Invalido. Tente Novamente.')

    continuar = input("\nPressione ENTER para continuar ou Digite 'sair': ").strip().lower()
    if continuar == 'sair':
        break
print('\nEncerrando Sistema. Aguarde...')
sleep(3)
print('\nPrograma Encerrado. Volte Sempre! 👋 ')
