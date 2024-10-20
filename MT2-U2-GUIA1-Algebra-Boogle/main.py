# AND
# tenemos un bucle que repetira su proceso 2 veces en una a=true
for A in [True, False]:
 for B in [True, False]:
  print(A," AND ", B," = ", A and B)

# OR
for A in [True, False]:
 for B in [True, False]:
  print(A," OR ", B," = ", A or B)

# NOT
# tenemos un bucle que repetira su proceso 2 veces en una a=true
for A in [True, False]:
 for B in [True, False]:
  print(A," NOT ", B," = ", not B)

# Ejercicio 1
print("X | Y |XvY|¬(x?y)|(x?y)?¬(x?y)")
for X in [1, 0]:
  for Y in [1, 0]:
    print(X,"|",Y,"|",X or Y,"|",int(not(X and Y)),"   | ",int((X or Y) and (not(X and Y))))

# Ejercicio 2
print("X | Y | Z |¬X |¬Y |¬Z |Y?¬Z|(X?(¬Y?(Z?(Y?¬Z))))?¬X)")
for X in [1, 0]:
  for Y in [1, 0]:
    for Z in [1, 0]:
      print(X,"|",Y,"|",Z,"|",int(not(X)),"|",int(not(Y)),"|",int(not(Z)),"|",int(X and not(Z))," |",int((X and(not(Y) and (Z or(X and not(Z)))))or not(X)))

# Ejercicio 3: Resuelto 

# Definimos las combinaciones de X, Y y Z
L = [
    [True, True, True, False, False, False, True, False, False, False],
    [True, True, False, False, True, True, True, False, False, True],
    [True, False, True, True, False, False, True, True, True, True],
    [True, False, False, True, True, False, False, False, False, True],
    [False, True, True, False, False, False, True, False, False, False],
    [False, True, False, False, True, True, True, False, False, True],
    [False, False, True, True, False, False, True, True, False, False],
    [False, False, False, True, True, False, False, False, False, True],
]
# Función para imprimir la tabla de verdad
def imprimir_tabla_verdad(tabla_verdad, variables):
    encabezado = variables + ["Resultado"]
    separador = "+" + "-" * (len(encabezado) * 26 - 1) + "+"
    print(separador)
    print("|", end="")
    for enc in encabezado:
        print(f" {enc.center(24)} |", end="")
    print("\n" + separador)
    for fila in tabla_verdad:
        print("|", end="")
        for valor in fila:
            print(f" {str(int(valor)).center(24)} |", end="")
        print("\n" + separador)

# Llamamos a la función para imprimir la tabla de verdad con los resultados
imprimir_tabla_verdad(L, ['X','Y','Z','¬Y','¬Z','Y∧¬Z','(Z∨(Y∧¬Z))','(¬Y∧(Z∨(Y∧¬Z)))','(X∧(¬Y∧(Z∨(Y∧¬Z))))','(X∧(¬Y∧(Z∨(Y∧¬Z))))∨¬Z'])

# Ejercicio 4: 
tabla_verdad = []
for A in [0, 1]:
    for B in [0, 1]:
        for C in [0, 1]:
            for D in [0, 1]:
              tabla_verdad.append((A, B, C, D,
                                   not (A or B), 
                                   not (C or D),
                                   (not (A or B) and not (C or D)),
                                   (not A and not B and not C and not D)))

def imprimir_tabla_verdad(tabla_verdad, variables):
    encabezado = variables + ["-(A+B)", "-(C+D)", "-(A+B)-(C+D)","-A-B*-C*-D"]
    separador = "+" + "-" * ((len(encabezado) * 23) - 1) + "+"
    print(separador)
    print("|", end="")
    for enc in encabezado:
        print(f"{enc.center(22)}|", end="")
    print("\n" + separador)
    for fila in tabla_verdad:
        print("|", end="")
        for valor in fila:
            print(f"{str(int(valor)).center(22)}|", end="")
        print("\n" + separador)

imprimir_tabla_verdad(tabla_verdad, ['A', 'B', 'C', 'D'])
