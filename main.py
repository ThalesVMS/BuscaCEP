import pip

import requests

def formatar_cep(cep):
    return f'{cep[:5]}-{cep[5:]}'

def consultar_cep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    response = requests.get(url)

    if response.status_code == 200:
        dados = response.json()
        endereco = dados.get('logradouro')
        bairro = dados.get('bairro')
        cidade = dados.get('localidade')
        uf = dados.get('uf')
        cep_formatado = formatar_cep(cep)
        resultado = f'{endereco} - {bairro}, {cidade} - {uf}, {cep_formatado}'
        return resultado
    else:
        return 'CEP não encontrado'

if __name__ == "__main__":
    while True:
        opcao = input("Digite '1' para buscar por CEP ou '2' para buscar por nome de logradouro (ou 's' para sair): ")

        if opcao == '1':
            cep = input("Digite o CEP (com traço): ")
            resultado = consultar_cep(cep)
            print(resultado)
        elif opcao == '2':
            logradouro = input("Digite o nome do logradouro: ")
            url = f'https://viacep.com.br/ws/{logradouro}/json/'
            response = requests.get(url)
            if response.status_code == 200:
                dados = response.json()
                for registro in dados:
                    endereco = registro.get('logradouro')
                    bairro = registro.get('bairro')
                    cidade = registro.get('localidade')
                    uf = registro.get('uf')
                    cep = registro.get('cep')
                    cep_formatado = formatar_cep(cep)
                    resultado = f'{endereco} - {bairro}, {cidade} - {uf}, {cep_formatado}'
                    print(resultado)
            else:
                print('Logradouro não encontrado')
        elif opcao.lower() == 's':
            break
        else:
            print("Opção inválida. Tente novamente.")