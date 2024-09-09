
print("Ejemplo de tuplas")
canciones=("te amo","ElNoNoa","amor eterno")
print(canciones)

y = list(canciones)
y[1] = "la negra"
x = tuple(y)

print(x)