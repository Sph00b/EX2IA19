
import random
from grafoConPriorita import GrafoConVisitaPriorita


def randomLetter():
     return random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')

def randomWeight():
    # range: [1, int + 1]
    int = 1000
    return 1 + random.random() * int

def graphGenerator(dimensione):
    """
    Il generatore crea un albero di un singolo nodo e, ogni volta
    che crea un nuovo vertice, lo connette all'albero mediante un
    arco. Il risultato finale è un grafo non orientato, connesso e
    pesato sui vertici.

    Gli elementi conterranno lettere casuali dell'alfabeto

    :param dimensione: la dimensione del grafo, strettamente positiva
    :return:
    """
    assert dimensione > 0, "la dimensione del grafo deve essere strettamente maggiore di zero"
    G = GrafoConVisitaPriorita()    # inizializzo un grafo vuoto

    # inserisco il primo nodo
    G.addWeightedNode(randomLetter(), randomWeight())

    for i in range(1, dimensione):
        G.addWeightedNode(randomLetter(), randomWeight())
        newNode = G.getLastInserted()
        heads = G.getNodes()
        heads.remove(newNode)
        G.insertEdge(newNode, random.choice(heads))

    return G

if __name__ == "__main__":

    G = graphGenerator(10)
    G.visitaInPriorita()
