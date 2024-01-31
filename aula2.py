class Livro():
    
    def __init__(self, titulo, isbn):
        self.titulo = titulo
        self.isbn = isbn
        print('Construtor chamado para criar um objeto desta classe')
        
    def imprime(self, titulo, isbn):
        print('Foi criado o livro %s com ISBN %d' %(titulo, isbn))
        

Livro01 = Livro("O Caminho da Servidão", 251457863)
Livro01.imprime("O Caminho da Servidão", 251457863)
