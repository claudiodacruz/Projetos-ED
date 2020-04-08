class No:
    def __init__(self, dado):
        self._dado = dado
        self._direita = None
        self._esquerda = None
        self._pai = None
    
    def get_dado(self):
        return self._dado
    
    def get_direita(self):
        return self._direita
    
    def get_esquerda(self):
        return self._esquerda
    
    def get_pai(self):
        return self._pai

    def set_dado(self, novoDado):
        self._dado = novoDado
    
    def set_direita(self, setarDireita):
        self._direita = setarDireita
    
    def set_esquerda(self, setarEsquerda):
        self._esquerda = setarEsquerda
    
    def set_pai(self, novoPai):
        self._pai = novoPai
