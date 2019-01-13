from graphGenerator import graphGenerator
from customGraph import CustomGraph
from priorityQueue import TypeQueue
from time import time

timer = 0

'''
casi d'uso
'''
def printNodeList(l):
    s = "["
    for node in l:
        s += "("+str(node.weight)+")"
    print(f"{s}]")

# Decorator per calcolare il tempo di esecuzione di una funzione
def timer(func):
    def wrapping_function(*args, **kwargs):
        global timer
        start = time()
        value = func(*args, **kwargs) # chiamiamo da funzione da analizzare
        timer = time() - start
        return value # dobbiamo ritornare il valore calcolato dalla funzione
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

def foo(qtype, fullE):
    for i in [10]:#,100,1000]:
        m = 100 #numero delle visite su cui fare la media
        t = 0
        for j in range(0,m):
            G = CustomGraph(qtype)
            gen = graphGenerator(G)
            for _ in range(i):
                next(gen)
            if fullE:
                fillEdges(G)
            test(G)
            t = t + timer
        print(f"Media di {m} tempi su {i} visite (Queue_type={qtype.name}, max_#Archi={fullE}) : {t/m}")

if __name__ == "__main__":
    for t in list(TypeQueue):
        foo(t, False)
        foo(t, True)
