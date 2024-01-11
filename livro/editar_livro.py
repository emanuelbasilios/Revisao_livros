from livro.livro_repositorio import *
from livro.buscar_livros import *
from livro.registrar import *
from livro.listar_livros import *

def editarLivro(id: int, titulo: str,editora:str,disponivel:bool):
    livro = buscarLivro(id)
    if livro:
        livro['titulo'] = titulo
        livro['editora'] = editora
        livro['disponivel'] = disponivel
        print('Dados alterados com sucesso!')
    else:
        print('Livro não encontrado!')

if __name__ == "__main__":
    listarLivros()
    editarLivro(1,"As Cronicas de Narnia","Abril",False)
    listarLivros()