import requests
from prettytable import PrettyTable


def buscar_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)
    return response.json()


def formatar_cep(cep):
    return f'{cep[:5]}-{cep[5:]}'


def exibir_resultados(resultados):
    tabela = PrettyTable(['ID', 'Endereço', 'Bairro', 'Cidade', 'UF', 'CEP'])
    for i, resultado in enumerate(resultados, 1):
        tabela.add_row([i, resultado['logradouro'], resultado['bairro'], resultado['localidade'],
                        resultado['uf'], formatar_cep(resultado['cep'])])
    print(tabela)


def main():
    while True:
        opcao = input("Digite 1 para pesquisar por CEP, 2 para pesquisar por nome do logradouro, ou 0 para sair: ")

        if opcao == '0':
            break

        if opcao == '1':
            cep = input("Digite o CEP (apenas números): ")
            resultado = buscar_cep(cep)
            exibir_resultados([resultado])

        elif opcao == '2':
            logradouro = input("Digite o nome do logradouro: ")
            url = f'https://viacep.com.br/ws/{logradouro}/json/'
            response = requests.get(url)
            resultados = response.json()
            exibir_resultados(resultados)

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
