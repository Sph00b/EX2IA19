from graphGenerator import graphGenerator
from customGraph import CustomGraph
from customGraph import TypeQueue
from time import time

'''
casi d'uso
'''
def printNodeList(l):
    s = "["
    for node in l:
        s += "("+str(node.weight)+")"
    print(f"{s}]")

'''
studiare in modo sperimentale visitaInPriorita
confrontando l’andamento dell’algoritmo utilizzando diverse code con priorita
al variare della grandezza dell’input (numero di vertici e/o archi maggiori)
'''

# Decorator per calcolare il tempo di esecuzione di una funzione

def timer(func):
    def wrapping_function(*args, **kwargs):
        start = time()
        func(*args, **kwargs) # chiamiamo da funzione da analizzare
        elapsed = time() - start
        return elapsed # dobbiamo ritornare il valore calcolato dalla funzione
    return wrapping_function

@timer
def test(G):
    '''
    :param G:
    :return: time elaplsed for run the function
    '''
    G.visitaInPriorita()

def fillEdges(G):
    for n in G.getNodes():
        for m in G.getNodes():
            if n is not m:
                G.insertEdge(n, m)

def foo(fullE):
    for i in [10,100,1000]:
        m = 100 #numero delle visite su cui fare la media
        t = 0
        for j in range(0,m):
            G = CustomGraph(TypeQueue.BINOMH)
            gen = graphGenerator(G)
            for _ in range(i):
                next(gen)
            if fullE:
                fillEdges(G)
            t += test(G)
        print(f"Tempo medio per {i} visite (max_#Archi={fullE}) : {t/m}")

if __name__ == "__main__":
    foo(False)
    foo(True)
