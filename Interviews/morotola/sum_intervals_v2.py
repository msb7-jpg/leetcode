"""
Ordenação (Sorting): Como os intervalos podem vir totalmente bagunçados (ex: um que começa em 1, depois um que começa em 7, depois um que começa em 3), o primeiro passo lógico é colocá-los em ordem. Mas ordenar pelo quê? Pelo início de cada intervalo.

Abordagem Ambiciosa (Greedy) com Varredura Linear: Depois de ordenados, você consegue percorrer a lista uma única vez de forma linear. Você mantém o controle do intervalo atual e, ao olhar para o próximo, só precisa checar se o início dele "atropela" ou não o fim do intervalo anterior.
"""


# TODO -> griddy logic

def sum_intervals(intervals: list[list[int]]):
    if not intervals:
        return 0
    
    sorted_intervals = sorted(intervals)
    
    size = 0
    current_start = sorted_intervals[0][0]
    current_end = sorted_intervals[0][1]
    
    for start, end in sorted_intervals[1:]:
        # Se o próximo intervalo começa antes ou exatamente onde o atual termina: SOBREPOSIÇÃO
        if start <= current_end:
            # O fim do meu intervalo atual passa a ser o maior entre os dois
            # Isso resolve o problema do "intervalo engolido"
            current_end = max(current_end, end)
        else:
            # Se não sobrepõe, o intervalo atual fechou! Calculamos o tamanho dele.
            size += current_end - current_start
            # E começamos um novo intervalo com os dados do atual
            current_start = start
            current_end = end
            
    # Não esqueça de somar o último intervalo que ficou aberto após o loop terminar
    size += current_end - current_start
    
    return size

assert sum_intervals([[1, 4], [7, 10], [3, 5]]) == 7
assert sum_intervals([[1, 2], [6, 10], [11, 15]]) == 9
assert sum_intervals([[-1, 1], [2, 8], [3, 10]]) == 10
assert sum_intervals([[1, 10], [2, 5]]) == 9
assert sum_intervals([[1, 5], [5, 8]]) == 7

print("All tests passed")