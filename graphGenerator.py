import random

def randomLetter():
     return random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

def randomWeight():
    return 1 + random.random() * 1000

def graphGenerator(G):  # genera un grafo connesso con n-1 archi
    """
    Il generatore crea un albero di un singolo nodo e, ogni volta
    che crea un nuovo vertice, lo connette all'albero mediante un
    arco. Il risultato finale è un grafo non orientato, connesso e
    pesato sui vertici.

    :param G: un grafo vuoto
    """

    firstNode = G.addWeightedNode(randomLetter(), randomWeight())   # inserisco il primo nodo
    listNode = [firstNode]
    while True:
        yield
        newNode = G.addWeightedNode(randomLetter(), randomWeight())
        G.insertEdge(newNode.id, random.choice(listNode).id)
        listNode.append(newNode)
