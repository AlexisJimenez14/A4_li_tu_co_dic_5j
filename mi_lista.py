
print("Ejemplo de listas")
arcoiris=["verde" , "azul" , "morado"]
print(arcoiris)
longitud=len(arcoiris)
print("elementos que tiene la lista arcoiris ",longitud)
print(f"elementos que tiene la lista arcoiris v2: {longitud}")

print("accediendo a un elemento de las listas")
print(arcoiris[1])
print(f"elemento en la posicion 0 es {arcoiris[0]}")
print(f"el tercer color del arcoiris es ",arcoiris[2])
print("agregar a un elemento de las listas")
print(arcoiris)
arcoiris.append("naranja")
print(arcoiris)
print("listar los elementos de la lista ciclo for")
for alexis in arcoiris:
    print(alexis)