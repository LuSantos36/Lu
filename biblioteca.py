class Autor:
    def __init__(self, nome, nacionalidade):
        self._nome = nome
        self._nacionalidade = nacionalidade

    def get_nome(self):
        return self._nome
    def get_nacionalidade(self):
        return self._nacionalidade

class Livro:
    def __init__(self, titulo, autor, isbn):
        self._titulo = titulo
        self._autor = autor
        self._isbn = isbn
        self._disponibilidade = True

    def get_titulo(self):
        return self._titulo
    def get_autor(self):
        return self._autor
    def get_isbn(self):
        return self._isbn
    def get_disponivel(self):
        return self._disponibilidade

    def adicionar(self, biblioteca):
        biblioteca.adicionar_livro(self)

    def buscar(biblioteca, titulo=None, autor=None):
        return biblioteca.buscar_livros(titulo, autor)
    def emprestar(self, usuario):
        if self._disponibilidade:
            self._disponibilidade = False
            usuario.adicionar_livro(self)
            return True
        return False
    def devolver(self, usuario):
        self._disponibilidade = True
        usuario.remover_livro(self)

class Usuario:
    def __init__(self, nome, user_id):
        self._nome = nome
        self._user_id = user_id
        self._livros_emprestados = []

    def get_nome(self):
        return self._nome
    def get_user_id(self):
        return self._user_id
    
    def adicionar_livro(self, livro):
        self._livros_emprestados.append(livro)
    def remover_livro(self, livro):
        self._livros_emprestados.remove(livro)

    @property
    def livros_emprestados(self):
        return self._livros_emprestados


class Biblioteca:
    def __init__(self):
        self._livros = []
        self._usuarios = []

    def adicionar_livro(self, livro):
        self._livros.append(livro)
        print(f"O livro '{livro.get_titulo()}' foi adicionado à biblioteca.")

    def buscar_livros(self, titulo=None, autor=None):
        resultados = []
        for livro in self._livros:
            if (titulo and titulo.lower() in livro.get_titulo().lower()) or \
               (autor and autor.lower() in livro.get_autor().get_nome().lower()):
                resultados.append(livro)
        return resultados

    def adicionar_usuario(self, usuario):
        self._usuarios.append(usuario)
        print(f"O usuário '{usuario.get_nome()}' foi adicionado à biblioteca.")


# Criando biblioteca
biblioteca = Biblioteca()

autor = Autor("Machado de Assis", "Brasileiro")
autor1 = Autor("José de Alencar", "Brasileiro")
livro = Livro("Dom Casmorro", autor, "9788542221091")
livro2 = Livro("Iracema", autor1,"9788542221138")
usuario = Usuario("Carlos", "10")

livro.adicionar(biblioteca)

resultados = Livro.buscar(biblioteca, titulo="Dom Casmurro")
for livro in resultados:
    print(f"Encontrado: {livro.get_titulo()} de {livro.get_autor().get_nome()}")

livro.emprestar(usuario)
print(f"Livros emprestados para {usuario.get_nome()}:")
for livro in usuario.livros_emprestados:
    print(f"- {livro.get_titulo()}")

livro.devolver(usuario)
print(f"Livros emprestados para {usuario.get_nome()} após devolução:")
for livro in usuario.livros_emprestados:
    print(f"- {livro.get_titulo()}")

