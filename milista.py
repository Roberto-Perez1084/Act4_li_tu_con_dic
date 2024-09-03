Misnovias=["Dayana","Dynn","Lili"]
Misnumeros=[666,69,777]
print(Misnovias)
print(Misnumeros)
print("---accediendo a los elementos de la lista---")
print(Misnovias[0])
if "Dayana" in Misnovias:
    print("Si, 'Dayana' esta en mi lista")
else:
    print("No eres mi novia, que suertuda")
print("Numero de novias")
Nnovias=len(Misnovias)
print(f"Numero de novias{Nnovias}")
print("ciclo for en listas")
posicion=0
for medianaranja in Misnovias:
    print(posicion," ",medianaranja)
    posicion=posicion+1