tamMemoria = input()

i = 1
memoria = []
pageMiss = 0
existe = False
elemAInserir = 0
elemAInserir = input()

# Algoritmo FIFO
while(elemAInserir != -1):
    for elemento in memoria:
        if(elemento == elemAInserir): existe = True
    if(existe == False):
        if(len(memoria) != tamMemoria):
            memoria.append(elemAInserir) # Insere no fim da memória, caso haja espaço
        else:
            memoria.pop(0) # Remove no início da memória, caso ela esteja cheia
            memoria.append(elemAInserir)
        pageMiss = pageMiss + 1
    i = i+1
    existe = False
    elemAInserir = input()
print pageMiss