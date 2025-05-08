def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Divide a lista em duas partes aproximadamente iguais
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Recursivamente aplica o Merge Sort em cada metade
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)
    
    # Combina as duas metades ordenadas em uma lista ordenada
    return merge(left_half, right_half)

def merge(left, right):
    merged_list = []
    left_index, right_index = 0, 0
    
    # Compara os elementos das duas listas e adiciona o menor elemento à lista mesclada
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged_list.append(left[left_index])
            left_index += 1
        else:
            merged_list.append(right[right_index])
            right_index += 1
    
    # Adiciona os elementos restantes, se houver, de ambas as listas à lista mesclada
    merged_list.extend(left[left_index:])
    merged_list.extend(right[right_index:])
    
    return merged_list

if __name__ == '__main__': 
  numbers = [6, 5, 3, 1, 8, 7, 2, 4]
  ordered = merge_sort(numbers)
  print(numbers)
  print(ordered)
