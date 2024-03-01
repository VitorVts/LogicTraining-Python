def fibonacci(n):
    fib_sequence = [0, 1]

    while len(fib_sequence) < n:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)

    return fib_sequence

# Exemplo: gerar os primeiros 10 números da sequência
resultado = fibonacci(10)
print(resultado)
