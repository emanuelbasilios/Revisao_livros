from cliente.cliente_repositorio import *
from cliente.buscar_cliente import *
from cliente.listar_clientes import *

def editarCliente(id: int, nome: str,livros:str):
    cliente = buscarCliente(id)
    if cliente:
        cliente['nome'] = nome
        cliente['livros'] = livros
        print('Dados alterados com sucesso!')
    else:
        print('Cliente não encontrado!')

if __name__ == "__main__":
    listarClientes()
    editarCliente(1,"Joana","Harry Potter")
    listarClientes()