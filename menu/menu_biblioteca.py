from livro.livro_repositorio import *
from livro.buscar_livros import *
from livro.registrar import *
from livro.listar_livros import *
from livro.deletar_livro import *
from livro.editar_livro import *

def menuBiblioteca():

        print(" --- Menu Biblioteca ---")
        print("1 - Cadastrar Livro")
        print("2 - Editar Livro")
        print("3 - Remover Livro")
        print("4 - Buscar Livro")
        print("5 - Listar todos os livros")
        print("6 - Sair")


        while True:
            opcao = input("Selecione uma opção: ")
            if opcao == "1":
                titulo = input("Digite o titulo do livro: ")
                editora= input("Digite a editora: ")
                registrarlivro(titulo,editora)
            elif opcao == "2":
                id = int(input("Informe o id do Livro: "))
                titulo = input("Digite o titulo do livro: ")
                editora = input("Digite a editora: ")
                disponivel = input("Qual a disponibilidade: 1 - True / 2 - False")
                if disponivel == "1":
                    editarLivro(id, titulo, editora, True)
                else:
                    editarLivro(id, titulo, editora, False)
            elif opcao == "3":
                id = int(input("Informe o id do Livro: "))
                deletarLivro(id)
            elif opcao == "4":
                id = int(input("Informe o id do Livro: "))
                print(buscarLivro(id))
            elif opcao == "5":
                listarLivros()
            elif opcao == "6":
                print("Volte Sempre!!")
                break
            else:
                print("Opção não encontrada")
if __name__ == "__main__":
    menuBiblioteca()




