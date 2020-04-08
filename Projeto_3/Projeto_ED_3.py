import copy
import time
import random
import copy
import os


os.system('clear') or None
print('Aguarde, programa em execução...')

# Gerando a lista para ordenação 

lista = []
for i in range(10000):
    t = random.randint(1, 5000)
    lista.append(t)


# Gerando copias da lista

lista1 = lista.copy()
lista2 = lista.copy()
lista3 = lista.copy()
lista4 = lista.copy()
lista5 = lista.copy()
lista6 = lista.copy()
lista7 = lista.copy()


# BUBBLESORT

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

tempoAntes = time.time()
bubble_sort(lista1) 
tempoDepois = time.time()
tempoExec_BBS = (tempoDepois-tempoAntes)


# INSERTIONSORT 

def insertion_sort(lista):
    tam_lista = len(lista)
    for i in range(1,tam_lista):
        temp = lista[i]
        trocou = False
        j = i - 1
        while j >= 0 and lista[j] > temp:
            lista[j+1] = lista[j]
            trocou = True
            j -=1
        
        if trocou:
            lista[j+1] = temp
        i += 1

tempoAntes = time.time()
insertion_sort(lista2) 
tempoDepois = time.time()
tempoExec_INS = (tempoDepois-tempoAntes)

# COMBSORT 

# Ordenação com CombSort 
def combSort(lista):
    abertura = len(lista)
    troca = True
    while abertura > 1 or troca:
        abertura = max(1, int(abertura / 1.25))  
        troca = False
        for i in range(len(lista) - abertura):
            j = i+abertura
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
                troca = True

tempoAntes = time.time()
combSort(lista3)
tempoDepois = time.time()
tempoExec_CMB = (tempoDepois-tempoAntes)

# SHELLSORT
def shellSort(lista):
    dist = len(lista)//2
    while dist > 0:
        i = dist
        while i < len(lista):
            temp = lista[i]
            trocou = False
            j = i - dist
            while j >= 0 and lista[j] > temp:
                lista[j+dist] = lista[j]
                trocou = True
                j -= dist

            if trocou:
                lista[j+dist] = temp
            i+= 1
        dist = dist // 2

tempoAntes = time.time()
shellSort(lista4) 
tempoDepois = time.time()
tempoExec_SS = (tempoDepois-tempoAntes)

# QUICKSORT 
def quick_sort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1
    if inicio < fim:
        p = partition(lista,inicio,fim)
        quick_sort(lista, inicio, p-1)
        quick_sort(lista, p+1, fim)

def partition(lista, inicio, fim):
    pivot = lista[fim]
    i = inicio
    for j in range (inicio, fim):
        if lista[j] <= pivot:
            lista[j], lista[i] = lista [i], lista[j]
            i = i + 1
    lista[i], lista[fim] = lista[fim], lista[i]    
    return i

tempoAntes = time.time()
quick_sort(lista5, 0, len(lista5)-1)
tempoDepois = time.time()
tempoExec_QCS = (tempoDepois-tempoAntes)


# MERGESORT
def mergeSort(listaR, inicio, fim): 
    if inicio < fim: 
        meio = (inicio+fim) // 2 
        mergeSort(listaR, inicio, meio) 
        mergeSort(listaR, meio+1, fim) 
        intercalar(listaR, inicio, meio, fim)

def intercalar(listaR, pI, pM, pF): 
    listaCopiada = listaR.copy() 
    i = pI 
    j = pM+1 
    k = pI 

    while k <= pF: 
        if i > pM: 
            listaR[k] = listaCopiada[j]
            j += 1
        elif j > pF: 
            listaR[k] = listaCopiada[i]
            i += 1
        elif listaCopiada[i] <= listaCopiada[j]:
            listaR[k] = listaCopiada[i]
            i += 1
        else: 
            listaR[k] = listaCopiada[j]
            j += 1

        k += 1

tempoAntes = time.time()
mergeSort(lista6, 0, len(lista6)-1)
tempoDepois = time.time()
tempoExec_MGS = (tempoDepois-tempoAntes)

# HEAPESORT
def heapify(arr, n, i): 
    largest = i 
    l = 2 * i + 1     
    r = 2 * i + 2     

    if l < n and arr[i] < arr[l]: 
        largest = l 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] 
        heapify(arr, n, largest) 

def heap_sort(arr): 
    n = len(arr)  

    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0) 
  
tempoAntes = time.time()
heap_sort(lista7)
tempoDepois = time.time()
tempoExec_HPS = (tempoDepois-tempoAntes)



os.system('clear') or None

print('########## MENU ###########\n')
print('1 - Lista Desordenada')
print('2 - Resultado BubleSort')
print('3 - Resultado InsertSort')
print('4 - Resultado MergeSort')
print('5 - Resultado HeapSort')
print('6 - Resultado ShellSort')
print('7 - Resultado CombSort')
print('8 - Resultado QuickSort')
print('9 - Comparativo de Resultados')
print('0 - Sair')
print('\n######################\n')
n = int(input('Selecione a opção: '))

while n != 0:
    if n == 1:
        print('\n###########LISTA DESORNDENADA #########\n')
        print('Lista Desordenada:', lista)
    elif n == 2:
        print(f'\nLista - Bubble sort:{lista1}\n')
        print('\nTempo antes:',tempoAntes,'Tempo depois:', tempoDepois)
        print('Tempo de execução - Bubble sort: %f segundos' %tempoExec_BBS)
    elif n == 3:
        print(f'\nLista - Insertion Sort:{lista2}\n')
        print('\nTempo antes:',tempoAntes,'Tempo depois:', tempoDepois)
        print('Tempo de execução - Insertion Sort: %f segundos' %tempoExec_INS)
    elif n == 4:
        print(f'\nLista - Merge Sort:{lista6}\n')
        print('Tempo antes:',tempoAntes,'Tempo depois:', tempoDepois)
        print('Tempo de execução - Merge Sort: %f segundos' %tempoExec_MGS)
    elif n == 5:
        print(f'\nLista - Heap Sort:{lista7}\n')
        print('Tempo antes:',tempoAntes,'Tempo depois:', tempoDepois)
        print('Tempo de execução - Heap Sort: %f segundos' %tempoExec_HPS)
    elif n == 6:
        print(f'\nLista - Shell Sort:{lista4}\n')
        print('Tempo antes:',tempoAntes,'Tempo depois:', tempoDepois)
        print('Tempo de execução - Shell Sort: %f segundos' %tempoExec_SS)
    elif n == 7:
        print(f'\nLista - Comb Sort:{lista3}\n')
        print('\nTempo antes:',tempoAntes,'Tempo depois:', tempoDepois)
        print('Tempo de execução - Comb Sort: %f segundos' %tempoExec_CMB)
    elif n == 8:
        print(f'\nLista - Quick Sort:{lista5}\n')
        print('Tempo antes:',tempoAntes,'Tempo depois:', tempoDepois)
        print('Tempo de execução - Quick Sort: %f segundos' %tempoExec_QCS)
    elif n == 9:   
        print('\n############ COMPARATIVO DE RESUTADOS ############\n')
        print('Tempo de execução BubbleSort: %.2f segundos' %tempoExec_BBS)
        print('Tempo de execução InsertionSort: %.2f segundos' %tempoExec_INS)
        print('Tempo de execução MergeSort: %.2f segundos' %tempoExec_MGS) 
        print('Tempo de execução HeapSort: %.2f segundos' %tempoExec_HPS)
        print('Tempo de execução ShellSort: %.2f segundos' %tempoExec_SS)
        print('Tempo de execução CombSort: %.2f segundos' %tempoExec_CMB)
        print('Tempo de execução QuickSort: %.2f segundos\n' %tempoExec_QCS)
    else:
        print('Opção incorreta!')
        n = int(input('Selecione a opção: '))
    print('\n########## MENU ###########\n')
    print('1 - Lista Desordenada')
    print('2 - Resultado BubleSort')
    print('3 - Resultado InsertSort')
    print('4 - Resultado MergeSort')
    print('5 - Resultado HeapSort')
    print('6 - Resultado ShellSort')
    print('7 - Resultado CombSort')
    print('8 - Resultado QuickSort')
    print('9 - Comparativo de Resultados')
    print('0 - Sair')
    print('\n######################\n')
    n = int(input('Selecione a opção: '))

    os.system('clear') or None

print('\n####### Fim da Execução #########\n.')