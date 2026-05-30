"""
A Lógica Ambiciosa (Greedy)
Se pegarmos o menor bloco possível, o melhor assento para ele é o menor assento que consiga abrigá-lo. Se um assento não serve nem para o menor bloco, ele não servirá para nenhum outro bloco maior, então podemos descartar esse assento.
"""

# Two pointer
def allocate_blocks(blocks: list[int], seatBlocks: list[int]) -> int:
    block_ptr = 0
    seat_ptr = 0
    allocated = 0
    
    while block_ptr < len(blocks) and seat_ptr < len(seatBlocks):
        if blocks[block_ptr] <= seatBlocks[seat_ptr]:
            allocated += 1
            block_ptr += 1
            seat_ptr +=1
            continue
        
        seat_ptr += 1
            
    return allocated

# TODO

assert allocate_blocks([3, 4, 6], [3, 5, 7]) == 3
assert (result := allocate_blocks([4, 6, 8], [3, 5, 7])) == 2, f"Expected 2, got {result}"
assert (result := allocate_blocks([1, 2, 3], [1, 1])) == 1, f"Expected 2, got {result}"
assert allocate_blocks([5, 5, 5], [4, 4, 4]) == 0
assert allocate_blocks([], [1, 2, 3]) == 0
assert allocate_blocks([1, 2, 3], []) == 0
assert allocate_blocks([2, 2, 2], [2, 2, 2]) == 3

print("All tests passed")