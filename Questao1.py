def check(num):
    a, b, = 0, 1

    if num == a or num == b:
         return f"O número {num} pertence à sequência de Fibonacci."
    
    while b < num:
        a, b = b, a + b

    if b == num:
        return f"O número {num} pertence à sequência de Fibonacci."
    else:
        return f"O número {num} não pertence à sequência de Fibonacci."
    
numero = int(input("Digite o numero: "))
resultado = check(numero)
print(resultado)
