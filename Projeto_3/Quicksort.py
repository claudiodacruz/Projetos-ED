def quicksort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1
    if inicio < fim:
        p = partition(lista,inicio,fim)
        quicksort(lista, inicio, p-1)
        quicksort(lista, p+1, fim)

def partition(lista, inicio, fim):
    pivot = lista[fim]
    i = inicio
    for j in range (inicio, fim):
        if lista[j] <= pivot:
            lista[j], lista[i] = lista [i], lista[j]
            i = i + 1
    lista[i], lista[fim] = lista[fim], lista[i]    
    return i

vetor = [50,30,10,85,22,70,35,17,100,45,22,17]

quicksort(vetor)
print(vetor)
