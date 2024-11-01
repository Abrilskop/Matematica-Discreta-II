print("Ejercicio 2 - Tabla de Verdad:")
print("X Y Z | X' Y' Z' | X'Y'Z' X'YZ XYZ' | Resultado | Complemento")
for X in [0, 1]:
    for Y in [0, 1]:
        for Z in [0, 1]:
            X_complement = 1 - X
            Y_complement = 1 - Y
            Z_complement = 1 - Z

            part1 = X_complement and Y_complement and Z_complement
            part2 = X_complement and Y and Z
            part3 = X and Y and Z_complement

            result = part1 or part2 or part3
            complement = 1 - result

            print(f"{X} {Y} {Z} | {X_complement} {Y_complement} {Z_complement} | {int(part1)} {int(part2)} {int(part3)} | {int(result)} | {int(complement)}")
