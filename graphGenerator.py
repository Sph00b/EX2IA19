import random
from customGraph import CustomGraph


def randomLetter():
     return random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

def randomWeight():
    return 1 + random.random() * 1000

def graphGenerator(dimensione):
    """
    Il generatore crea un albero di un singolo nodo e, ogni volta
    che crea un nuovo vertice, lo connette all'albero mediante un
    arco. Il risultato finale è un grafo non orientato, connesso e
    pesato sui vertici.

    :param dimensione: la dimensione del grafo, strettamente positiva
    :return:
    """
    assert dimensione >= 0, "la dimensione del grafo deve essere positiva"

    G = CustomGraph()    # inizializzo un grafo vuoto

    if dimensione > 0:
        # inserisco il primo nodo
        G.addWeightedNode(randomLetter(), randomWeight())

        for i in range(1, dimensione):
            newNode = G.addWeightedNode(randomLetter(), randomWeight())
            listNode = G.getNodes()
            listNode.remove(newNode)
            G.insertEdge(newNode, random.choice(listNode))

    return G

if __name__ == "__main__":

    G = graphGenerator(10)
    G.visitaInPriorita()
