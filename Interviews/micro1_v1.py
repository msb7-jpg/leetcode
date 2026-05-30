"""
Título: Alocação de Blocos em AssentosDescrição: > Você recebe duas listas de inteiros: blocks (representando o tamanho de blocos que precisam de espaço) e seatBlocks (representando a capacidade dos assentos disponíveis).Um bloco só pode ser alocado em um assento se o tamanho do bloco for menor ou igual à capacidade do assento block <= seat. Cada assento pode conter no máximo um bloco.

Objetivo: > Retorne o número máximo de blocos que podem ser alocados com sucesso.

Conceitualmente idêntico a problemas famosos do LeetCode, como o LeetCode 455: Assign Cookies 
"""

def allocate_blocks(blocks: list[int], seatBlocks: list[int]) -> int:
    allocated = 0
    
    if not blocks or not seatBlocks:
        return allocated
    
    for block in sorted(blocks):
        for seat in sorted(seatBlocks):
            if block <= seat:
                allocated += 1
                seatBlocks.remove(seat)
                break
            
    return allocated

assert allocate_blocks([3, 4, 6], [3, 5, 7]) == 3
assert allocate_blocks([4, 6, 8], [3, 5, 7]) == 2
assert allocate_blocks([1, 2, 3], [1, 1]) == 1
assert allocate_blocks([5, 5, 5], [4, 4, 4]) == 0
assert allocate_blocks([], [1, 2, 3]) == 0
assert allocate_blocks([1, 2, 3], []) == 0
assert allocate_blocks([2, 2, 2], [2, 2, 2]) == 3

print("All tests passed")