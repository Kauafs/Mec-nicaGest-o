import requests
import time
import string

my_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzU1ODcxMjI4LCJpYXQiOjE3NTU4NzA5MjgsImp0aSI6IjgyMGZiMTdmMTY4NzRjM2ViNWFhZTRiMjhlNDcxZTNkIiwidXNlcl9pZCI6IjEifQ.2iDyhP0v6xvjcPp6rAbZBJhERdWACoP_bV7JkEiIAdo"

def main():
    dct = {
        1:get_dados,
        2:post_dados,
        3:sair, 
        }
    while True:
        opc = int(input('[1] - GetDados\n[2] - PostDados\n[3] - Sair\nEscolha uma opção:'))
        if opc in dct:
            dct[opc]()
        else:
            print('Opção inválida')

def get_dados(url = r'http://localhost:8000/api/v1'):
    vetor = [i for i in string.punctuation]
    headers = {'Authorization': f'Bearer {my_token}'}
    try:
        while True:
            e_categoria = (input('Informe a categoria: ')).lower()
            if e_categoria.isnumeric():
                print(f'Formato incorreto: possui números: {e_categoria}')
            if e_categoria == '':
                print(f'Formato incorreto: vazio: {e_categoria}')
            for i in e_categoria:
                if i in vetor:
                    print(f'Formato incorreto: possui caracteres especiais: {e_categoria}')
                    break
            else:
                print('Esperando os dados do corpo: ')
                time.sleep(10)
                get_body =  requests.get(f"{url}/{e_categoria}", headers=headers)
                if get_body.status_code == 401:
                    print('Status:',get_body.status_code,' Token Expirado')
                if get_body.status_code == 404:
                    print(f'Staus: {get_body.status_code} Servidor não existe')
                    break
            data = get_body.json()
            for key, value in data.items():
                print(f'{key}: {value}')   
    except KeyboardInterrupt:
        print('\n[+] Encerrado pelo o usuário')
def post_dados():
    var = {'Authorization':f'Bearer {my_token}'}
    pay = {
        "user":1,
        "peca":9,
        "produto":"testeproduto",
        "quantidade":2,
        "preco": 100.0,
        "data_compra": "2023-01-01",
        "peca_id":2,
        "user_id":1
    }
    send = requests.post('http://localhost:8000/api/v1/compras/', headers=var, json=pay)
    print(send.status_code)
    print(send.json())
    if send.status_code == 201:
        print('[+] Cadastrdo com sucesso')
    else:
        print('[-] Falha ao cadastrar')
    
def sair():
    print('Saindo...')
    exit()
if __name__ == '__main__':
    main()