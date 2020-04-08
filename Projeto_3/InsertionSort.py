def insertion_sort(lista):
    n = len(lista)
    for i in range(1,n):
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

vetor = [22,50,30,10,85,70,35,100,45,22,17]

insertion_sort(vetor)
print(vetor)