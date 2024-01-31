class Livro():
    
    def __init__(self):
        self.titulo = 'Novelas Exemplares'
        self.isbn = 8540509202
        print('Construtor chamado para criar um objeto desta classe')
        
    def imprime(self):
        print('Foi criado o livro %s com ISBN %d' %(self.titulo, self.isbn))
        
        

Livro01 = Livro()
print(type(Livro01))
Livro01.imprime()