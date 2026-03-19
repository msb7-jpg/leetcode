"""
Lychrel Number Counter

This program implements the Lychrel number algorithm:
1. Take a number and reverse its digits
2. Add the number to its reverse
3. If the result is a palindrome, return it and the iteration count
4. Otherwise, repeat with the result

Returns:
    tuple: (palindrome_number, iterations_count)
"""

numero = int(input())

i = 0
max_attempts = 20


def reverse_number(number: int) -> int:
    return int(str(number)[::-1])

def is_palindrome(number: int) -> bool:
    return number == reverse_number(number)

while i < max_attempts:
    soma = numero + reverse_number(numero)
    
    if is_palindrome(soma):
        print(numero, i)
        break
    
    i += 1
    numero = soma