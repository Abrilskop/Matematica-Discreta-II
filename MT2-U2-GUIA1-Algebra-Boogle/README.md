# ALGEBRA DE BOOLE
## LINK de repaso: https://ellibrodepython.com/operadores-logicos

## Ejecución manual del ejercicio:

### Primera iteración del bucle exterior (A = True):
- **Primera iteración del bucle interior (B = True):**
  - Imprime: `True AND True = True`
- **Segunda iteración del bucle interior (B = False):**
  - Imprime: `True AND False = False`

### Segunda iteración del bucle exterior (A = False):
- **Primera iteración del bucle interior (B = True):**
  - Imprime: `False AND True = False`
- **Segunda iteración del bucle interior (B = False):**
  - Imprime: `False AND False = False`

## La función `and` en Python

La función `and` en Python es un operador lógico que se utiliza para combinar expresiones booleanas. Su resultado es `True` solo si ambas expresiones son verdaderas. Aquí te dejo un resumen:

- `True and True` → `True`
- `True and False` → `False`
- `False and True` → `False`
- `False and False` → `False`

## ¿Que es iterar?
"Irriterar" se refiere a repetir un proceso varias veces. En el contexto de programación, significa pasar por cada elemento de una colección, como una lista. Por ejemplo, en el bucle for, se itera sobre los valores de la lista uno por uno. 
```
Inicio
 └── for A in [True, False]:
        ├── A = True
        │   └── for B in [True, False]:
        │           ├── B = True
        │           │    └── Imprime: True AND True = True
        │           └── B = False
        │                └── Imprime: True AND False = False
        └── A = False
            └── for B in [True, False]:
                    ├── B = True
                    │    └── Imprime: False AND True = False
                    └── B = False
                         └── Imprime: False AND False = False
```
## Ejercicios de la GUIA:
### Ejercicio 1: Realizar una tabla similar para la siguiente ecuación lógica (x∨y)∧¬(x∧y)

### Ejercicio 2: Similarmente realizar el mismo ejercicio para el siguiente problema: (𝑥 ∧ (¬𝑦 ∧ (𝑧 ∨ (𝑦 ∧ ¬𝑧)))) ∨¬z

### Ejercicio 3: Bansandote en la aplicacion de esta funcion, adecua el ejercicio 2 con esta funcion.
```
# Esta lista representa la operación OR.
# Supongamos que las tablas de verdad están en una lista como sigue:
L = [
      [False, False, False],
      [False, True, True],
      [True, False, True],
      [True, True, True]
    ]

# Ahora, consideramos el siguiente código:
def imprimir_tabla_verdad(tabla_verdad, variables):
    encabezado = variables + ["Resultado"]
    separador = "+" + "-" * (len(encabezado) * 7 - 1) + "+"
    print(separador)
    print("|", end="")
    for enc in encabezado:
        print(f" {enc.center(5)} |", end="")
    print("\n" + separador)
    for fila in tabla_verdad:
        print("|", end="")
        for valor in fila:
            print(f" {str(int(valor)).center(5)} |", end="")
        print("\n" + separador)

# Que pasa, si ejecutamos el codigo anterior de la siguiente manera:
imprimir_tabla_verdad(L, ['A','B','A or B'])
```
### Ejercicio 4: Utilizando el teorema de De Morgan, simplifica la expresión F = (̅𝐴̅̅+̅̅̅̅𝐵̅).(𝐶̅̅̅+̅̅̅̅𝐷̅) y luego implementa un programa en Python para verificar la equivalencia entre la expresión original y la expresión simplificada (utiliza el algoritmo anterior)
