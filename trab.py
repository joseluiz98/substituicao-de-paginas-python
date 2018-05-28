tamMemoria = input()

acessos = []
memoriaFIFO = []
memoriaLRU = []
pageMiss = [0,0,0] #pageMiss[0] representa FIFO, pageMiss[1] OTM e pageMiss[2] LRU
existe = False

entrada = input()
# Recebe as entradas que representam acessos à memória
while(entrada != -1):
    acessos.append(entrada)
    entrada = input()

# Algoritmo FIFO
for acesso in acessos:
    for elemento in memoriaFIFO: # Verifica se elemento já está na memória
        if(elemento == acesso): existe = True
    if(not(existe)): # Se não existe na memória
        if(len(memoriaFIFO) != tamMemoria):
            memoriaFIFO.append(acesso) # Insere no fim da memória, caso haja espaço
        else:
            memoriaFIFO.pop(0) # Remove no início da memória, caso ela esteja cheia
            memoriaFIFO.append(acesso)
        pageMiss[0] = pageMiss[0] + 1
    existe = False

# Algoritmo LRU
momento = 0 # Representa o momento em que o acesso ocorre, nesta implementação, o loop do for, ou seja, quanto menor este número, mais antigo foi o acesso ao dado

for acesso in acessos:
    acesso = [acesso, -1] # O vetor de acessos recebe o próprio elemento acessado, e um valor que representa o último momento em que foi acessado

for acesso in acessos:
    for elemento in memoriaLRU:
        if(elemento[0] == acesso):
            existe = True
            acesso = [acesso, momento] # O vetor de acessos recebe o próprio elemento acessado, e o último momento em que foi acessado
            elemento = acesso
    if(not(existe)):
        if(len(memoriaLRU) != tamMemoria):
            acesso = [acesso, momento] # O vetor de acessos recebe o próprio elemento acessado, e o último momento em que foi acessado
            elemento = acesso
            memoriaLRU.append(acesso)
        else:
            menosRecente = memoriaLRU[0][1]
            for elemento in memoriaLRU:
                if(elemento[1] < menosRecente): menosRecente = elemento # Procura o elemento menos recentemente utilizado
            elemento = memoriaLRU.index(elemento) # Recebe o índice do elemento
            memoriaLRU.pop(elemento) # Remove o elemento menos recentemente usado
            
            acesso = [acesso, momento] # Registra o acesso ao elemento na memória
            memoriaLRU.append(acesso) # Insere o elemento na memória
        pageMiss[2] = pageMiss[2] + 1
    existe = False
    momento = momento+1

print pageMiss[0]
print pageMiss[2]