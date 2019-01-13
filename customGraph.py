from Librerie.Graph import Node
from Librerie.Graph import GraphBase
from codaPriorita import CodaPriorita

class WeightedNode(Node):
    """
    a variant of the node which holds weight.
    """

    def __init__(self, id, value, weight):
        """
        Constructor.
        :param id: node ID (integer).
        :param value: node value.
        :param weight: node weight
        """
        assert weight > 0, "i pesi dei vertici devono essere strettamente positivi"
        Node.__init__(self, id, value)
        self.weight = weight

class CustomGraph(GraphBase):
    """
    Implementatio of the GraphBase data struct with weighted nodes and custom visit method.
    """

    def __init__(self):
        """
        Manteniamo l'insieme degli archi come liste di adiacenza
        """
        GraphBase.__init__(self)
        self.edges = {}  # dictionary {nodeId: listaAdiacenti}

    def numEdges(self):
        """
        Return the number of edges.
        :return: the number of edges.
        """
        return len(self.getEdges())

    def addNode(self, elem):
        #per il tipo di struttura non è adatto (ampliare)
        pass

    def addWeightedNode(self, elem, weight):
        """
        Add a new node with the specified value.
        :param elem: the node value.
        :return: the create node.
        """

        newNode = WeightedNode(self.nextId, elem, weight)
        self.nodes.update({self.nextId:newNode})
        self.edges.update({self.nextId:[]})     # aggiungo una lista di adiacenza vuota per il nuovo nodo
        self.nextId += 1
        return newNode

    def deleteNode(self, nodeId):
        self.edges.pop(nodeId)
        for key in self.edges.keys():
            if nodeId in self.edges.get(key):
                self.edges.get(key).remove(nodeId)
        self.nodes.pop(nodeId)
        """
        Remove the specified node.
        :param nodeId: the node ID (integer).
        :return: void.
        """

    def getNode(self, id):
        """
        Return the node, if exists.
        :param id: the node ID (integer).
        :return: the node, if exists; None, otherwise.
        """
        return self.nodes.get(id)

    def getNodes(self):
        """
        Return the list of nodes.
        :return: the list of nodes.
        """
        return list(self.nodes.values())

    def insertEdge(self, tail, head, weight=None):
        self.edges.get(tail.id).append(head.id)   # aggiunge head alla lista di adiacenza di tail
        self.edges.get(head.id).append(tail.id)   # aggiunge tail alla lista di adiacenza di head

    def deleteEdge(self, tail, head):
        self.edges.get(tail.id).remove(head.id)  # rimuove head dalla lista di adiacenza di tail
        self.edges.get(head.id).remove(tail.id)  # rimuove tail dalla lista di adiacenza di head

    def getEdge(self, tail, head):
        '''
        :return: True if the edge exists, False otherwise
        '''
        if head.id in self.edges.get(tail.id):
            return (self.getNode(head.id), self.getNode(tail.id))

    def getEdges(self):
        l = []
        for key in self.edges.keys():
            for element in self.edges.get(key):
                head = self.getNode(key)
                tail = self.getNode(element)
                if not (tail, head) in l:
                    l.append(head, tail)
            return l

    def isAdj(self, tail, head):
        return head in self.edges.get(tail)

    def getAdj(self, nodeId):
        return self.edges.get(nodeId)

    def deg(self, nodeId):
        return len(self.edges.get(nodeId))

    def visitaInPriorita(self):
        """
        Visita che parte da dal vertice di costo massimo ed usa
        una coda con priorità come frangia F
        :return: lista con ordine della visita.
        """
        assert not self.isEmpty(), "Il grafo è vuoto"

        nodeMaxPriority = self.getNodes()[0]

        for node in self.getNodes():                #troviamo il nodo di costo maggiore
            if node.weight > nodeMaxPriority.weight:
                nodeMaxPriority = node

        F = CodaPriorita()  # Frangia

        """
        Tweak per l'inserimento del peso in una Coda con Priorità:
        l'implementazione delle code presente nelle Librerie mantiene in alto il minimo valore
        disponibile, mentre il testo del progetto rchiede che la nostra coda mantenga in alto
        la massima priorità. Per ovviare al problema si inseriscono come chiavi dei nodeId i
        pesi con segno negativo.
        """

        F.insert(nodeMaxPriority, -nodeMaxPriority.weight)      #inizializziamo F con il nodo di costo maggiore (nodo, peso)
        visited_nodes = []

        while not F.isEmpty():  # while there are nodes to explore ...
            node = F.findMin()   # findMin() ritorna l'id del nodo con priorità massima
            F.deleteMin()
            visited_nodes.append(node)
            # add all adjacent unexplored nodes to the stack
            for adj_nodeId in self.getAdj(node.id):
                if self.getNode(adj_nodeId) not in visited_nodes:
                    F.insert(self.getNode(adj_nodeId), -self.getNode(adj_nodeId).weight)
        return visited_nodes

    def print(self):
        None
        #farlo bellino che serve

if __name__ == "__main__":
    G = CustomGraph()
    G.getNode(1)
    G.getNodes()
    G.getEdges()
    G.visitaInPriorita()
