from graphGenerator import graphGenerator
from customGraph import CustomGraph
from priorityQueue import TypeQueue
from time import time

timer = 0

# Decorator per calcolare il tempo di esecuzione di una funzione
def timer(func):
    def wrapping_function(*args, **kwargs):
        global timer
        start = time()
        value = func(*args, **kwargs) # chiamiamo da funzione da analizzare
        timer = time() - start
        return value # dobbiamo ritornare il valore calcolato dalla funzione
    return wrapping_function

def FillCSV(ascissa, ordinata, filename):
    file = open(filename + ".csv", "a")
    file.write(ascissa + ",\t" + ordinata + "\n")
    file.close()

def fillEdges(G):
    nodeList = G.getNodes()
    for n in range(0, len(nodeList)):
        for m in range(n+1, len(nodeList)):
            G.insertEdge(nodeList[n].id, nodeList[m].id)

@timer
def test(G):
    G.visitaInPriorita()

def foo(qtype, fullE):
    for i in [10,100,1000]:
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
        # FillCSV(str(i), str(t / m), f"./Data/CustomGraph_QueueType={qtype.name}_FullEdges={fullE}")
        print(f"Media di {m} tempi su {i} visite (Queue_type={qtype.name}, max_#Archi={fullE}) : {t/m}")

if __name__ == "__main__":
    for t in list(TypeQueue):
        foo(t, False)
        foo(t, True)

'''
casi d'uso
'''
def printNodeList(l):
    s = "["
    for node in l:
        s += "("+str(node.weight)+")"
    print(f"{s}]")
