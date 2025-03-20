
def registrar_livro(titulo, autor, ano):
    return {
        "titulo":titulo,
        "autor":autor,
        "ano":ano
    }

def exibir_livro(livro):
    for key,livros in livro.items():
        print(f"{key}: {livros}")


meu_livro = registrar_livro("sua prima é minha","lauricio mestre",1992)
exibir_livro(meu_livro)