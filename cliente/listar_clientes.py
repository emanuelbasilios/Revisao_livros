from cliente.cliente_repositorio import *

def listarClientes():
    print("--- Lista de Clientes ---")
    for cliente in clientes:
        print(f"Id: {cliente['id']}")
        print(f"Nome: {cliente['nome']}")
        print(f"Livros:{cliente['livros']}")
        print("*"*50)

if __name__ == "__main__":
    listarClientes()