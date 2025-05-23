# O(n²)
# algoritmo de ordem quadrática
def bubble_sort(numbers):
    n = len(numbers) # Quantidade de elementos na lista

    for ordered_elements in range(n - 1): # Precisamos ordenar n-1 elementos
        for item in range(0, n - 1 - ordered_elements): # Vamos percorrer até o elemento anterior ao ordenado
            if numbers[item] > numbers[item + 1]: # se um elemento for maior, flutuamos ele para cima
                current_element = numbers[item]
                # numbers[item] = numbers[item + 1]
                # numbers[item + 1] = current_element
                
                # Lembra da troca com desempacotamento?
                numbers[item], numbers[item + 1] = numbers[item + 1], current_element
    return numbers

if __name__ == '__main__': 
  numbers = [7, 5, 9, 2, 6, 8]
  numbers = [8, 5, 9, 7, 6, 2]
  print(bubble_sort(numbers))