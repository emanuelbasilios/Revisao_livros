from livro.livro_repositorio import *
from livro.buscar_livros import *
from livro.registrar import *
from livro.listar_livros import *

def emprestarLivro(id:int):
    livro = buscarLivro(id)
    if not livro:
        print("Livro não encontrado!")
        return
    if not livro["disponivel"]:
        print("Livro não encontra-se disponivel!!")
        return
    livro["disponivel"] = False
    print("Emprestimo realizado com sucesso!")

def devolverLivro(id:int):
    livro = buscarLivro(id)
    if not livro:
        print("Livro não encontrado!")
        return
    if livro["disponivel"]:
        print("Livro encontra-se disponivel!!")
        return
    livro["disponivel"] = True
    print("Livro devolvido com sucesso!")

if __name__ == "__main__":
    listarLivros()
    emprestarLivro(2)
    emprestarLivro(1)
    devolverLivro(2)
    devolverLivro(1)
    devolverLivro(2)