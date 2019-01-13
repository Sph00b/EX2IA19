from graphGenerator import graphGenerator
'''
studiare in modo sperimentale visitaInPriorita
confrontando l’andamento dell’algoritmo utilizzando diverse code con priorita
al variare della grandezza dell’input (numero di vertici e/o archi maggiori)
'''

def printNodeList(l):
    s = "["
    for node in l:
        s += "("+str(node.weight)+")"
    print(f"{s}]")

for i in range(2,5):
    G = graphGenerator(10**i)
    printNodeList(G.visitaInPriorita())
