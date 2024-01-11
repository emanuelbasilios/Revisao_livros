from cliente.cliente_repositorio import *

id_atual = 1

def gerarCliente(nome: str):
    global id_atual
    id_atual += 1
    pessoa = {
        "id": id_atual,
        "nome": nome,
    }
    return pessoa

def registrarcliente(nome: str):
    pessoa = gerarCliente(nome)
    clientes.append(pessoa)
    print("Cliente cadastrado com sucesso!")

if __name__ == "__main__":
    registrarcliente("Joana")
    print(clientes)