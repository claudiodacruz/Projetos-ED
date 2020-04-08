class Chave:
    def __init__(self):
        self._chave = None
        self._indice = None
        self._size = 0
    
    def get_chave(self):
        return self._chave
    
    def get_indice(self):
        return self._indice
    
    def set_chave(self, novaChave):
        self._chave = novaChave
    
    def set_indice(self, novoIndice):
        self._indice = novoIndice
