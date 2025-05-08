

def selection_sort_string(sequence):
    n = len(sequence) # Quantidade de elementos da lista
    
    sequence = list(sequence)
    print("")
    print("sequence_list: ", sequence)
    print("")
    # raise ValueError("The correct format is String.")
    
    for index in range(n - 1): # Precisamos ordenar N-1 elementos
        min_element_index = index # Definimos a variável para buscar o menor elemento
        current_element = sequence[index]

        for next_index in range(index + 1, n): # Início da busca pelo menor elemento
            next_element = sequence[next_index]
            result = next_element < sequence[min_element_index]
            
            if result:
                min_element_index = next_index # Atualiza o índice atual do menor elemento

        # Troca os elementos de posição
        current_element = sequence[index]
        sequence[index] = sequence[min_element_index]
        sequence[min_element_index] = current_element

    return sequence

sequence1 = "roma"
sequence2 = "amor"


sequence1_sorted = selection_sort_string(sequence1)
sequence2_sorted = selection_sort_string(sequence2)
is_the_same_string = sequence1_sorted ==  sequence2_sorted
results = sequence1_sorted, sequence2_sorted, is_the_same_string

print("")
print("")
print(f"sequence1_sorted: {sequence1_sorted}, type: {type(sequence1_sorted)}")
print(f"sequence2_sorted: {sequence2_sorted}, type: {type(sequence2_sorted)}")
print(f"is_the_same_string: {is_the_same_string}")
print(f"results: {results}")
print("")