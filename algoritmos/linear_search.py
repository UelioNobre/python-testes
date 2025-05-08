# Ordenado
# Tempo Linear - O(n)
def linear_search(data, value): 
    for index in range(len(data)): 
        if value == data[index]: 
            return index 
    raise ValueError('Valor não encontrado na lista') 
    
if __name__ == '__main__': 
    data = [1, 2, 9, 8, 3, 4, 7, 6, 5] 
    print(linear_search(data, 7))