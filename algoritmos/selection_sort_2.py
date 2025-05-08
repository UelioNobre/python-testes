def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Encontra o índice do menor elemento restante na lista não ordenada
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        # Troca o menor elemento com o primeiro elemento não ordenado
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

sequence = [17, 5, 9, 22, 6, 18]
print(f"Lista inicial: {sequence}")

ordered_numbers = selection_sort(sequence)
print(f"Lista final: {ordered_numbers}")