from livro.livro_repositorio import livros

id_atual = 1

def gerarLivro(titulo: str, editora: str):
    global id_atual
    id_atual += 1
    livro = {
        "id": id_atual,
        "titulo": titulo,
        "editora": editora,
        "disponivel": True
    }
    return livro

def registrarlivro(titulo: str, editora: str):
    livro = gerarLivro(titulo, editora)
    livros.append(livro)
    print("Livro cadastrado com sucesso!")

if __name__ == "__main__":
    registrarlivro("Código limpo", "Space")
    print(livros)