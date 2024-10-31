# Ejercicio 1
variables1 = ['A', 'B', 'C']

def expr1(A, B, C):
    # Expresión booleana
    return (A and B and C) or (not A and B and not C) or (A and not B and C)

# Generar tabla de verdad
print("A B C | A' B' C' | ABC A'BC' AB'C | Resultado | Complemento")
for A in [0, 1]:
    for B in [0, 1]:
        for C in [0, 1]:
            # Calcular los complementos
            A_complement = 1 - A
            B_complement = 1 - B
            C_complement = 1 - C

            # Calcular cada parte de la expresión
            part1 = A and B and C
            part2 = not A and B and not C
            part3 = A and not B and C

            # Resultado total
            result = part1 or part2 or part3

            # Calcular el complemento
            complement = 1 - result

            # Imprimir todos los pasos
            print(f"{A} {B} {C} | {A_complement} {B_complement} {C_complement} | {int(part1)} {int(part2)} {int(part3)} | {int(result)} | {int(complement)}")
