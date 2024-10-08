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