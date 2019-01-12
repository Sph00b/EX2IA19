from Librerie.Graph import GraphBase
from Librerie.Graph import Node
from codaPriorita import CodaPriorita

class NodoPesato (Node):

    def __init__(self, id, value, weight):
        Node.__init__(self, id, value)
        """
        Constructor.
        :param id: node ID (integer).
        :param value: node value.
        :param weight: node weight
        """
        assert weight > 0, "i pesi dei vertici devono essere strettamente positivi"
        self.weight = weight


class GrafoConVisitaPriorita(GraphBase):

    def __init__(self):
        GraphBase.__init__(self)
        """
        manteniamo l'insieme degli archi come liste di adiacenza
        """
        self.edges = {}     # dictionary {nodeId: listaAdiacenti}


    def addWeightedNode(self, elem, weight):    # verrà usato nel generatore di G
        """
        Add a new node with the specified value.
        :param elem: the node value.
        :return: the create node.
        """

        newNode = NodoPesato(self.nextId, elem, weight)
        self.nodes.update({self.nextId:newNode})
        self.edges.update({self.nextId:[]})     # aggiungo una lista di adiacenza vuota per il nuovo nodo
        self.nextId += 1
        return newNode

    def getNode(self, id):  # non lo uso da nessuna parte
        """
        Return the node, if exists.
        :param id: the node ID (integer).
        :return: the node, if exists; None, otherwise.
        """
        return self.nodes.get(id)

    def insertEdge(self, tail, head, weight=None):  # verrà usato nel generatore di G
        """
        Add a new edge.
        :param tail: the tail node ID (integer).
        :param head: the head node ID (integer).
        :param weight: It will be ignored in this particular implementation.
        """
        self.edges.get(tail).append(head)   # aggiunge head alla lista di adiacenza di tail
        self.edges.get(head).append(tail)   # aggiunge tail alla lista di adiacenza di head

    def deleteEdge(self, tail, head):   # non lo uso da nessuna parte
        """
        Remove the specified edge.
        :param tail: the tail node ID (integer).
        :param head: the head node ID (integer).
        """
        self.edges.get(tail).pop(head)  # rimuove head dalla lista di adiacenza di tail
        self.edges.get(head).pop(tail)  # rimuove tail dalla lista di adiacenza di head

    def isAdj(self, tail, head):    # non lo uso da nessuna parte
        """
        Checks if two nodes ar adjacent.
        :param tail: the tail node ID (integer).
        :param head: the head node ID (integer).
        :return: True, if the two nodes are adjacent; False, otherwise.
        """
        # Note: this method only checks if tail and head exist

        if head in self.edges.get(tail):
            return True
        else:
            return False

    def getAdj(self, nodeId):
        """
        Return all nodes adjacent to the one specified.
        :param nodeId: the node id.
        :return: the list of nodes adjacent to the one specified.
        :rtype: list
        """

        return self.nodes.get(nodeId)


    def visitaInPriorita(self):
        """
        visita che parte da dal vertice di costo massimo ed usa
        una coda con priorità come frangia F
        :return: lista con ordine della visita.
        """

        if self.isEmpty():
            print("il grafo è vuoto")
            return
        else:
            """
            troviamo il vertice con peso maggiore con cui inizializzare la coda F
            """
            nodeIdWithMaxPriority = 0
            for nodeId in range(0, self.nextId):
                if self.nodes.get(nodeId).weight > self.nodes.get(nodeIdWithMaxPriority).weight:
                    nodeIdWithMaxPriority = nodeId

        F = CodaPriorita()  # Frangia
        """
        Tweak per l'inserimento del peso in una Coda con Priorità:
        l'implementazione delle code presente nelle Librerie mantiene in alto il minimo valore
        disponibile, mentre il testo del progetto rchiede che la nostra coda mantenga in alto
        la massima priorità. Per ovviare al problema si inseriscono come chiavi dei nodeId i
        pesi con segno negativo.
        """
        F.insert(nodeIdWithMaxPriority, -self.nodes.get[nodeIdWithMaxPriority].weight)   # insert(elemento, chiave)

        # visited nodes initialization
        visited_nodes = []

        while not F.isEmpty():  # while there are nodes to explore ...
            node = F.findMin()   # findMin() ritorna l'id del nodo con priorità massima
            F.deleteMin()
            visited_nodes.append(node)
            # add all adjacent unexplored nodes to the stack
            for adj_nodeId in self.getAdj(node):
                if adj_nodeId not in visited_nodes:
                    F.insert(adj_nodeId, -self.nodes.get[nodeIdWithMaxPriority].weight)

        return visited_nodes