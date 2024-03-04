def insertion_sort(v):
    n = len(v)
    i = 0

    while i < n:
        aux = v[i]
        j = i - 1

        while j >= 0 and v[j] > aux:
            v[j + 1] = v[j]
            
            j = j - 1

        v[j + 1] = aux
        i = i + 1

# Exemplo de uso:
vetor = [4, 2, 1, 5, 3]
insertion_sort(vetor)

print("Vetor ordenado:", vetor)
