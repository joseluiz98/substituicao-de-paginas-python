tamMemoria = input()

acessosAMemoria = []
memoriaFIFO = []
memoriaLRU = []
memoriaOTM = []
pageMiss = [0,0,0] #pageMiss[0] representa FIFO, pageMiss[1] OTM e pageMiss[2] LRU
elementoEstaNaMemoria = False

entrada = input()
# Recebe as entradas que representam acessos à memória
while(entrada != -1):
    acessosAMemoria.append(entrada)
    entrada = input()

# Algoritmo FIFO
for acesso in acessosAMemoria:
    for elemento in memoriaFIFO: # Verifica se elemento já está na memória
        if(elemento == acesso): elementoEstaNaMemoria = True
    if(not(elementoEstaNaMemoria)): # Se não existe na memória
        if(len(memoriaFIFO) != tamMemoria):
            memoriaFIFO.append(acesso) # Insere no fim da memória, caso haja espaço
        else:
            memoriaFIFO.pop(0) # Remove no início da memória, caso ela esteja cheia
            memoriaFIFO.append(acesso)
        pageMiss[0] = pageMiss[0] + 1
    elementoEstaNaMemoria = False

def proximaUtilizacao(elemento, acessosAMemoria, elementosJaAnalisados):
    "Procura a próxima utilização do elemento recebido como parâmetro"
    "Parâmetros: elemento a ser buscada próxima utilização, vetor contendo acessos à memória"
    "Retorna: int contendo momento da próxima utilização"
    elementosJaAnalisados = elementosJaAnalisados+1 # Ponteiro para o próximo elemento não analisado dos acessos
    indice = elementosJaAnalisados # Índice começa pelo primeiro elemento não analisado
    acessosAMemoria = acessosAMemoria[elementosJaAnalisados:] # Ponto de partida, excluindo elementos cujos acessos já foram tratados
    for acesso in acessosAMemoria:
        if(acesso == elemento): return indice # Próxima referência no futuro encontrada, retorne-a
        indice = indice + 1

    return -1

# Algoritmo OTM
momento = 0
referenciasFuturas = []
for acesso in acessosAMemoria:
    for elemento in memoriaOTM:
        if(elemento == acesso): elementoEstaNaMemoria = True
    if(not(elementoEstaNaMemoria)):
        if(len(memoriaOTM) != tamMemoria):
            memoriaOTM.append(acesso)
        else: # Se memória cheia, e elemento não está nela, remove o que será referenciado o mais tarde possível
            for elemento in memoriaOTM:
                utilizacao = proximaUtilizacao(elemento,acessosAMemoria,momento)
                referenciasFuturas.append(utilizacao) # Procura referencias futuras de cada elemento e guarda em vetor
                if(utilizacao == -1): # Se encontrou um elemento que nunca mais será referenciado, este é o substituído perfeito
                    existeSubstituicaoPerfeita = True
                    elemento = memoriaOTM.index(elemento) # Descobre o indice do elemento na memória
                    memoriaOTM.pop(elemento) # Remove o respectivo elemento, cujo índice foi descoberto anteriormente
                    memoriaOTM.append(acesso)
                    break
            if(not(existeSubstituicaoPerfeita)): # Se só existem elementos que serão referenciados em algum momento, procure pela ação menos impactante
                referenciaMaisDistante = -1
                for referencia in referenciasFuturas:
                    if(referencia > referenciaMaisDistante): referenciaMaisDistante = referencia
                elemento = referenciasFuturas.index(referenciaMaisDistante) # Descobre o indice daquele elemento na memória
                memoriaOTM.pop(elemento) # Remove o respectivo elemento, cujo índice foi descoberto anteriormente
                memoriaOTM.append(acesso)
        pageMiss[1] = pageMiss[1] + 1
    elementoEstaNaMemoria = False
    existeSubstituicaoPerfeita = False
    momento = momento + 1
    referenciasFuturas = []

# Algoritmo LRU
momento = 0 # Representa o momento em que o acesso ocorre, nesta implementação, o loop do for, ou seja, quanto menor este número, mais antigo foi o acesso ao dado
elementoEstaNaMemoria = False
for acesso in acessosAMemoria:
    acesso = [acesso, 0] # O vetor de acessos recebe o próprio elemento acessado, e um valor que representa o último momento em que foi acessado

for acesso in acessosAMemoria:
    for elemento in memoriaLRU:
        if(elemento[0] == acesso):
            indice = -1
            for i in range(0,tamMemoria): # Recupera o indice do elemento
                if(memoriaLRU[i][0] == elemento[0]):
                    indice = i
                    break
            elementoEstaNaMemoria = True
            elemento = [acesso, momento] # O último momento em que o elemento foi referenciado é atualizado
            memoriaLRU[indice] = elemento # Atualiza o elemento na memória
    if(not(elementoEstaNaMemoria)):
        if(len(memoriaLRU) != tamMemoria):
            acesso = [acesso, momento] # O vetor de acessos recebe o próprio elemento acessado, e o último momento em que foi acessado
            elemento = acesso
            memoriaLRU.append(acesso)
        else:
            menosRecente = memoriaLRU[0]
            for elemento in memoriaLRU:
                if(elemento[1] < menosRecente[1]): menosRecente = elemento # Procura o elemento menos recentemente utilizado
            elemento = memoriaLRU.index(menosRecente) # Recebe o índice do elemento
            memoriaLRU.pop(elemento) # Remove o elemento menos recentemente usado
            
            acesso = [acesso, momento] # Registra o acesso ao elemento na memória
            memoriaLRU.append(acesso) # Insere o elemento na memória
        pageMiss[2] = pageMiss[2] + 1
    elementoEstaNaMemoria = False
    momento = momento+1

print 'FIFO ' + str(pageMiss[0])
print 'OTM ' + str(pageMiss[1])
print 'LRU ' + str(pageMiss[2])