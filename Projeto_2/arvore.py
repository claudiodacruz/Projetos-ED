pifrom dado import Dado
from no import No
from chaves import Chave

class Fila:
    def __init__(self, head):
        self._head = head

    def adicionar(self, no):
        p = self._head
        tail = p.get_direita()
        if p == None:
            self._head = no
        else:
            while tail!= None:
                p = p.get_direita()
                tail = tail.get_direita()
        p.set_direita(no)

    def remover(self):
        self._head = self._head.get_proximo()

    def vazio(self):
        if self._head == None:
            print(True) 
        else:
            print(False)
        
    def caminhar(self):
        p = self._head
        while (p != None):
            print (p) 
            p = p.get_proximo()

    def tamanho(self):
        p = self._head
        contador = 0
        while (p != None):
            contador +=1
            p = p.get_proximo()
        print(contador)

    def mostrar(self):
        print(self._head)



class Arvore:
    def __init__(self):
        self._raiz = None
        self._chave = None
        self._indice = None 
        self._chaves = []   

    def adicionar(self, no):
        p = self._head
        tail = p.get_direita()
        if p == None:
            self._head = no
        else:
            while tail!= None:
                p = p.get_direita()
                tail = tail.get_direita()
        p.set_direita(no) 


    def add(self, node):
        arvore = self._raiz
        p = None
        q = None

        if (arvore == None):
            self._raiz = no
            chave = no.
            no.set_indice(self._size))

        for i in range(0,self._size)):
            p = q = arvore
            while (chaves[i] != p.get_dado().get_chave() and q != None):
                p = q
                if (chaves[i] < p.get_dado().get_chave()):
                    q = p.get_esquerda()
                else:
                    q = p.get_direita()
                
            item = Dado()
            item.set_chave(chaves[i])
            item.set_indice(i)

            q = No(item)
            if (chaves[i] < p.get_dado().get_chave()):
                p.set_esquerda(q)
            else:
                p.set_direita(q)
        return arvore

    def inserirRegistro(self, no):
        p = self._raiz
        q = None
        r = None
        chave == p.get_dado().get_chave()
        
        while (p !=None):
            q = p
            if (chave < p.get_dado().get_chave()):
                p = p.get_esquerda()
            else:
                p = p.get_direita()
            
        item = Dado()
        item.set_chave(chave)
        item.set_indice(len(registros))

        r = No(item)
        
        if (q ==None):
            arvore = range
        elif (chave < q.get_dado().get_chave()):
            q.set_esquerda(r)
        else:
            q.set_direita(r)

        recebe_registro(registros)
        return len(registros)


    def buscaId(self, chave):
        p = self._raiz
        q = None

        while (p !=None):
            if (chave == p.get_dado().get_chave()):
                return p.get_dado()
            q = p
            if (chave < p.get_dado().get_chave()):
                p = p.get_esquerda()
            else:
                p = p.get_direita()
            
        return "A chave não foi encontrada - Filme não cadastrado"
    
    def buscaAno(self, ano):
        # inserir código
    
    def alturaArvore(self):
        # inserir código

    def exibirArvore(self):
        # inserir código
    
    def __tamanho__(self):
        return self._size