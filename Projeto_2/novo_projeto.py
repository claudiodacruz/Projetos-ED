class Dado:
    def __init__(self, nome=None, ano=None, id = None):
        self._nome = nome
        self._ano = ano
        self._id = id
    
    # Métodos acessadores
    def get_nome(self):
        return self._nome
    
    def get_ano(self):
        return self._ano
    
    def get_id(self):
        return self._id

    # Métodos modificadores
    def set_nome(self, novoNome):
        self._nome = novoNome
    
    def set_ano(self, novoAno):
        self._ano = novoAno
    
    def set_id(self, novoId):
        self._id = novoId

    # Método para retornar o objeto no formato de string
    def __str__(self):
        return "Título: {} - Ano de Produção: {} - Chave: {}".format(self._nome, self._ano, self._id)

class Chave:
    def __init__(self, chave):
        self._chave = chave
        self._indice = None

    def get_chave(self):
        return self._chave
    
    def get_indice(self):
        return self._indice
    
    def set_chave(self, novaChave):
        self._chave = novaChave
    
    def set_indice(self, novoIndice):
        self._indice = novoIndice

    def __str__(self):
        return "Chave = {} e Indice = {}".format(self._chave, self._indice)

class No:
    def __init__(self, dado):
        self._dado = dado
        self._direita = None
        self._esquerda = None
    
    def get_dado(self):
        return self._dado
    
    def get_direita(self):
        return self._direita
    
    def get_esquerda(self):
        return self._esquerda
    
    def set_dado(self, novoDado):
        self._dado = novoDado

    def set_direita(self, setarDireita):
        self._direita = setarDireita
    
    def set_esquerda(self, setarEsquerda):
        self._esquerda = setarEsquerda
    
    def __str__(self):
        return "{}".format(self._dado)

class Fila:
    def __init__(self):
        self._head = None
        self._size = 0

    def adicionar(self, no):
        p = self._head
        tail = None
        if p == None:
            self._head = no
        else:
            tail = p.get_direita()
            while tail!= None:
                p = p.get_direita()
                tail = tail.get_direita()
            p.set_direita(no)
        self._size += 1

    def caminhar(self):
        p = self._head
        while (p != None):
            print(p) 
            p = p.get_direita()

    def tamanho(self):
        p = self._head
        contador = 0
        while (p != None):
            contador +=1
            p = p.get_direita()
        print(contador)

    def buscaAno(self, ano):
        p = self._head
        q = p
        encontrar = False
        if (p == None):
            print("Não existem filmes cadastrados")
        else:
            while(q != None):
                if(ano == p.get_dado().get_ano()):
                    q = p.get_direita()
                    encontrar = True
                    print(p)
                else:
                    q = p.get_direita()
                p = q
            if (not encontrar):
                print('Não existem filmes cadastrados com este ano')
    
    def buscaId(self,id):
        p = self._head
        q = p
        if (p == None):
            print("Não existem filmes cadastrados")
        else:
            while(q != None):
                if(id == p.get_dado().get_indice()):
                    q = p.get_direita()
                    print(p)
                else:
                    q = p.get_direita()
                p = q

    def ordenar(self):
        for i in range(self._size - 1):
            p = self._head
            q = p.get_direita()
            while q != None:
                if p.get_dado().get_nome() > q.get_dado().get_nome():
                    aux = p.get_dado()
                    p.set_dado(q.get_dado())
                    q.set_dado(aux)
                p = p.get_direita()
                q = q.get_direita() 

class Arvore:
    def __init__(self):
        self._raiz = None
        self._ind = 0

    def inserir(self, no):
        p = self._raiz
        q = None
        chave = no.get_dado().get_chave()

        while (p !=None):
            q = p
            if (chave > p.get_dado().get_chave()):
                p = p.get_esquerda()
            else:
                p = p.get_direita()
        
        if (q ==None):
            self._raiz = no
            no.get_dado().set_indice(self._ind)
        elif (chave > q.get_dado().get_chave()):
            q.set_esquerda(no)
            no.get_dado().set_indice(self._ind)
        elif (chave < q.get_dado().get_chave()):
            q.set_direita(no)
            no.get_dado().set_indice(self._ind)

    def buscaId(self, idProc):
        p = self._raiz
        q = p

        while (q !=None):
            if (idProc == p.get_dado().get_chave()):
                indProc = p.get_dado().get_chave()
                print(indProc)
                q = -1
                break
            elif (idProc > p.get_dado().get_chave()):
                q = p.get_esquerda()
            else:
                q= p.get_direita()
            p = q
        if (q == None):
            print("A chave não foi encontrada - Filme não cadastrado")

    def altura(self, no=None):
        if no == None:
            no = self._raiz
            return 1
        altEsq = 0
        altDir = 0
        if (no.get_esquerda() != None):
            print(altDir)
            altEsq = 1 + self.altura(no.get_esquerda())
            
        if (no.get_direita() != None):
            print(altEsq)
            altDir = 1 + self.altura(no.get_direita())
            
        if altDir > altEsq:
            
            return altDir
        return altEsq
            
    def posOrdem(self, no=None):
        if(no == None):
            no = self._raiz
        if (no.get_esquerda() != None):
            self.posOrdem(no.get_esquerda)
        if (no.get_direita() != None):
            self.posOrdem(no.get_direita)
        print(no)

    def caminhar(self):
        p = self._raiz
        while (p != None):
            print(p) 
            p = p.get_direita()
'''
    def __len__(self):
        return self._size


    def exibirArvore(self):
        # inserir código
'''
'''
for i in range(3):
    titulo = input('Informe o nome do filme: ')
    ano = input('Informe o ano de lançamento: ')
    key = input('Informe o identificador do filme: ')
'''


lista = Fila()
#lista.adicionar(No(Dado('Noite',2012,11)))
#lista.adicionar(No(Dado('Casa',2010,14)))
#lista.adicionar(No(Dado('Dia',2015,2)))
#lista.adicionar(No(Dado('Tarde',2015,13)))
#lista.adicionar(No(Dado('Hora',2013,6)))
#lista.adicionar(No(Dado('Amanhã',2016,12)))
#lista.adicionar(No(Dado('Escuro',2012,9)))
#lista.caminhar()
#print(' ')
#lista.buscaAno(2011)
lista.ordenar()
#print(' ')
#lista.caminhar()

'''
arvore = Arvore()

arvore.inserir(No(Chave(11)))
arvore.inserir(No(Chave(14)))
arvore.inserir(No(Chave(2)))
arvore.inserir(No(Chave(13)))
arvore.inserir(No(Chave(6)))
arvore.inserir(No(Chave(12)))
arvore.inserir(No(Chave(9)))
arvore.caminhar()
arvore.buscaId(14)

'''

def menuList():
    print(f'Menu de Lista Encadeada - :\n', 
            f'1 - Inserir filme\n',
            f'2 - Buscar ID\n',
            f'3 - Buscar ano\n',
            f'4 - Caminhar na árvore\n',
            f'5 - Finalizar o programa\n')

arvore = Arvore()
menuList()

opcao = int(input('Opção:'))
while opcao!= 5:
    if opcao == 1: #Inserir chave
        arvore.inserir(No(Chave(int(input('Inserir chave:')))))
        lista.adicionar(No(Dado(input('Nome:'),input('Ano:'),int(input('ID:')))))
    elif opcao == 2: #Buscar filme por id
        arvore.buscaId(int(input('Buscar ID:')))
        print('Encontrado')
    elif opcao == 3: #Buscar filme por ano
        lista.buscaAno(input('Ano:'))
        lista.caminhar()
    elif opcao == 4: #remover no meio
        lista.ordenar()
        lista.caminhar()
        arvore.caminhar()
    else:
        print('Opção Invalida')
        menuList()
    opcao = int(input('Opção:'))
print('Programa finalizado')