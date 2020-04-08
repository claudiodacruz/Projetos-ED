# bubble sort
def bubble_sort(lista):
    tam_lista = len(lista)
    for i in range (tam_lista):
        troca = False
        for j in range (1,tam_lista-i):
            if lista[j] < lista[j-1]:
                lista[j], lista[j-1] = lista[j-1], lista[j]
                troca = True
        if not troca:
            break

vetor = [50,30, 22,10,85,70,35,100,45,22,17]

bubble_sort(vetor)
print(vetor)
