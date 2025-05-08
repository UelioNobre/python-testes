

def selection_sort(numbers):
    n = len(numbers) # Quantidade de elementos da lista

    for index in range(n - 1): # Precisamos ordenar N-1 elementos
        min_element_index = index # Definimos a variável para buscar o menor elemento
        current_element = numbers[index]

        for next_index in range(index + 1, n): # Início da busca pelo menor elemento
            next_element = numbers[next_index]
            
            expression = f"{next_element} < {numbers[min_element_index]} = {next_element < numbers[min_element_index]}"
            result = next_element < numbers[min_element_index]
            
            print(expression, result)
            
            if result:
                min_element_index = next_index # Atualiza o índice atual do menor elemento

        # Troca os elementos de posição
        current_element = numbers[index]
        numbers[index] = numbers[min_element_index]
        numbers[min_element_index] = current_element

    return numbers

sequence = [7, 5, 9, 2, 6, 8]
sequence = ["uelio"]
print(f"Lista inicial: {sequence}")
ordered_numbers = selection_sort(sequence)
print(f"Lista final: {ordered_numbers}")