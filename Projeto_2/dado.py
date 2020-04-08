class Dado:
    def __init__(self, nome=None, ano=None, id = None):
        self._nome = nome
        self._ano = ano
        self._id = id
        self._index = None
    
    # Métodos acessadores
    def get_nome(self):
        return self._nome
    
    def get_ano(self):
        return self._ano
    
    def get_id(self):
        return self._id
    
    def get_index(self):
        return self._index

    # Métodos modificadores
    def set_nome(self, novoNome):
        self._nome = novoNome
    
    def set_ano(self, novoAno):
        self._ano = novoAno
    
    def set_id(self, novoId):
        self._id = novoId
    
    def set_index(self, novoIndex):
        self._index = novoIndex

    # Método para retornar o objeto no formato de string
    def __str__(self):
        return "Título: {} - Ano de Produção: {} - Chave: {} - Indice {}".format(self._nome, self._ano, self._id, self._index)

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
            no.get_dado().set_index(self._size)
        else:
            tail = p.get_direita()
            while tail!= None:
                p = p.get_direita()
                tail = tail.get_direita()
            p.set_direita(no)
            no.get_dado().set_index(self._size)
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
                print('Não existem filmes cadastrados com este ano.')
    
    def buscaRegId(self,id):
        resultado = arvore.buscaId(id)
        if (self._head == None):
            print("Não existem filmes cadastrados.")
        elif (resultado == -1):
            print("Para cadastrar o novo filme use a opção 1.")
        else:
            p = self._head
            if (p.get_dado().get_index() != 0):
                for i in range(self._size - 1,):
                    p = self._head
                    q = p.get_direita()
                    while q != None:
                        if p.get_dado().get_index() > q.get_dado().get_index():
                            aux = p.get_dado()
                            p.set_dado(q.get_dado())
                            q.set_dado(aux)
                        p = p.get_direita()
                        q = q.get_direita() 
            p = self._head
            cont = 0
            while (cont < resultado):
                p = p.get_direita()
                cont+= 1
            print(p)


    def ordenar(self):
        if (self._head == None):
            print("Não existem filmes cadastrados.")
        for i in range(self._size - 1,):
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
                p = p.get_direita()
            else:
                p = p.get_esquerda()
        
        if (q == None):
            self._raiz = no
            no.get_dado().set_indice(self._ind)
        elif (chave > q.get_dado().get_chave()):
            q.set_direita(no)
            no.get_dado().set_indice(self._ind)
        elif (chave < q.get_dado().get_chave()):
            q.set_esquerda(no)
            no.get_dado().set_indice(self._ind)
        self._ind +=1
    
    def balancear(self):
        if self.balanco():
            print('balancear')

    def balanco(self):
        qEsq_Raiz = 0
        qDir_Raiz = 0
        if (self._ind > 1):
            p = self._raiz
            if (p.get_esquerda() != None):
                p = p.get_esquerda()
                qEsq_Raiz = self.altura(p)
                subEsq = p
                print(subEsq)
            else:
                subEsq = None
            p = self._raiz
            if (p.get_direita() != None):
                p = p.get_direita()
                qDir_Raiz = self.altura(p)
                subDir = p
            else:
                subDir = None

        #calcula a altura da subarvore a esquerda
        qEsq_subEsq = 0
        print(subEsq)
        if (subEsq != None):
            p = subEsq
            if (p.get_esquerda() != None):
                p = p.get_esquerda()
                qEsq_subEsq = self.altura(p)
        
            if (p.get_direita() != None):
                p = p.get_direita()
                qDir_SubEsq = self.altura(p)
        
        print("Esquerda = ",qEsq_subEsq)
    
        #calcula a altura da subarvore da direita
        qDir_subDir = 0
        if (subDir != None):
            p = subDir
            if (p.get_esquerda() != None):
                p = p.get_esquerda()
                qEsq_SubDir = self.altura(p)
        
            if (p.get_direita() != None):
                p = p.get_direita()
                qDir_SubDir = self.altura(p)
            
        print("Direita = ",qDir_subDir)
    
        #verifica a necessidade de balanceamento
        if abs(qDir_Raiz-qEsq_Raiz)>1:
            q = qDir_Raiz-qEsq_Raiz
            #print(q)
            if (q > 1):
                if (qEsq_subEsq < 0):
                    print("Rotação dupla esquerda")
                else:
                    print("Rotação a esquerda")
            else: 
                if (qDir_subDir > 0):
                    print("Rotação dupla direita")
                else:
                    print("Rotação a direita")       


    def buscaId(self, idProc):
        p = self._raiz
        q = p
        while (q !=None):
            if (idProc == p.get_dado().get_chave()):
                index = p.get_dado().get_indice()
                q = -1
                return index
            elif (idProc < p.get_dado().get_chave()):
                q = p.get_esquerda()
            else:
                q= p.get_direita()
            p = q
        if (q == None):
            print("A chave não foi encontrada - Filme não cadastrado")
            return -1

    def altura(self, no=None):
        if (self._raiz == None):
            return 0
        if no == None:
            no = self._raiz
        altEsq = 0
        altDir = 0
        if (no.get_esquerda() != None):
            altEsq = self.altura(no.get_esquerda())
            no = no.get_esquerda()
        if (no.get_direita() != None):
            altDir = self.altura(no.get_direita())
            no = no.get_direita()
            
        if altDir > altEsq:
            return altDir + 1
        else:
            return altEsq + 1
    
    def altEsq(self,no=None):
        if no == None:
            no = self._raiz
        altEsq = 0
        if (no.get_esquerda() != None):
            altEsq = self.altura(no.get_esquerda())
            no = no.get_esquerda()
        if (no.get_direita() != None):
            altEsq = self.altura(no.get_direita())
            no = no.get_direita()

    def altDir(self,no=None):
        if no == None:
            no = self._raiz
        altDir = 0
        altEsq = 0
        if (no.get_direita() != None):
            altDir = self.altura(no.get_direita())
            no = no.get_direita()
        if (no.get_esquerda() != None):
            altEsq = self.altura(no.get_esquerda())
            no = no.get_esquerda()
         
        if altDir < altEsq:
            return altDir + 1
        else:
            return altEsq + 1
            
    def posOrdem(self, no=None):
        if(no == None):
            no = self._raiz
        if (no.get_esquerda() != None):
            self.posOrdem(no.get_esquerda())
        if (no.get_direita() != None):
            self.posOrdem(no.get_direita())
        print(no.get_dado())

    def emOrdem(self, no=None):
        if (self._raiz == None):
            print('A árvore está vazia.')
        else:
            if (no==None):
                no = self._raiz
            if(no.get_esquerda() != None):
                self.emOrdem(no.get_esquerda())
            print (no.get_dado())
            if (no.get_direita() != None):
                self.emOrdem(no.get_direita())   
    
    def rotacaoEsquerda(self):
        p = self._raiz
        aux = p.get_direita()
        p.set_direita(aux.set_esquerda())
        aux.set_esquerda(p)

    def rotacaoDireita(self):
        p = self._raiz
        aux = p.get_esquerda()
        p.set_esquerda(aux.set_direita())
        aux.set_direita(p)

    def rotacaoDuplaDir(self):
        self.rotacaoDireita()
        self.rotacaoEsquerda()
        p = self._raiz
        aux = p.get_esquerda()
        p.set_esquerda(aux.set_direita())
        aux.set_direita(p)
        p = self._raiz
        aux = p.get_direita()
        p.set_direita(aux.set_esquerda())
        aux.set_esquerda(p)

    def rotacaoDuplaEsq(self):
        p = self._raiz
        aux = p.get_direita()
        p.set_direita(aux.set_esquerda())
        aux.set_esquerda(p)
        p = self._raiz
        aux = p.get_esquerda()
        p.set_esquerda(aux.set_direita())
        aux.set_direita(p)

'''
# Menu de exibição
def menuList():
    print(f'Menu de Opções:\n', 
            f'1 - Inserir filme\n',
            f'2 - Buscar filme pelo ID\n',
            f'3 - Buscar filmes por ano\n',
            f'4 - Listar filmes em ordem alfabética\n',
            f'5 - Atura da Árvore\n',
            f'6 - Exibir Árvore\n',
            f'7 - Finalizar o programa\n')

arvore = Arvore()
lista = Fila()
menuList()

opcao = int(input('Opção:'))
while opcao!= 7:
    if opcao == 1: #Inserir chave
        id = int(input('Inserir chave:'))
        arvore.inserir(No(Chave(id)))
        lista.adicionar(No(Dado(input('Nome:'),input('Ano:'),id)))
    elif opcao == 2: #Buscar filme por id
        lista.buscaRegId(int(input('Informe o ID:')))
    elif opcao == 3: #Buscar filme por ano
        lista.buscaAno(input('Informe o Ano:'))
    elif opcao == 4: #Listar em Ordem Alfabética
        lista.ordenar()
        lista.caminhar()
    elif opcao == 5: #Altura da Árvore
        altArvore = arvore.altura()
        print(altArvore)
    elif opcao == 6: #Exibir Arvore
        arvore.emOrdem()
    else:
        print('Opção Invalida')
        menuList()
    opcao = int(input('Opção:'))
print('Programa finalizado')




'''
lista = Fila()

lista.adicionar(No(Dado('Noite',2012,2)))
lista.adicionar(No(Dado('Casa',2010,6)))
lista.adicionar(No(Dado('Dia',2015,11)))

'''
lista.adicionar(No(Dado('Tarde',2015,11)))
lista.adicionar(No(Dado('Hora',2013,14)))
lista.adicionar(No(Dado('Amanhã',2016,12)))
lista.adicionar(No(Dado('Escuro',2012,9)))
lista.adicionar(No(Dado('Claro',2014,4)))

lista.caminhar()
print(' ')

lista.buscaAno(2011)
lista.ordenar()
lista.caminhar()
'''


arvore = Arvore()

arvore.inserir(No(Chave(2)))
arvore.inserir(No(Chave(6)))
arvore.inserir(No(Chave(11)))

'''
arvore.inserir(No(Chave(13)))
arvore.inserir(No(Chave(14)))
arvore.inserir(No(Chave(12)))
arvore.inserir(No(Chave(9)))
arvore.inserir(No(Chave(4)))

arvore.emOrdem()

lista.buscaRegId(6)
arvore.posOrdem()



lista.buscaRegId(13)
print('')
lista.caminhar()
'''
arvore.posOrdem()
arvore.balanco()


