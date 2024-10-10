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
Ejercicio 1: Realizar una tabla similar para la siguiente ecuación lógica (x∨y)∧¬(x∧y), la tabla debe
ser similar a la imagen: 

Ejercicio 2: Similarmente realizar el mismo ejercicio para el siguiente problema: (𝑥 ∧ (¬𝑦 ∧ (𝑧 ∨
(𝑦 ∧ ¬𝑧)))) ∨¬z

Ejercicio 2 parte 2: 
Supongamos que las tablas de verdad están en una lista como sigue:
L = [[False, False, False], [False, True, True],
 [True, False, True], [True, True, True]]
Esta lista representa la operación OR.
Ahora, consideramos el siguiente código:
Que pasa, si ejecutamos el codigo anterior de la siguiente manera:
`imprimir_tabla_verdad(L,['A', 'B', 'A or B'])`
