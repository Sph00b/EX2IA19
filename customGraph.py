from Librerie.Graph import Node
from Librerie.Graph import GraphBase
from priorityQueue import PriorityQueue
from priorityQueue import TypeQueue

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

    def __init__(self, qtype):
        """
        @qtype: tipo di coda
        Manteniamo l'insieme degli archi come liste di adiacenza
        """
        GraphBase.__init__(self)
        self.edges = {}  # dictionary {nodeId: listaAdiacenti}
        self.qtype = qtype

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
        if head not in self.edges.get(tail) and tail is not head:
            self.edges.get(tail).append(head)   # aggiunge head alla lista di adiacenza di tail
            self.edges.get(head).append(tail)   # aggiunge tail alla lista di adiacenza di head

    def deleteEdge(self, tail, head):
        self.edges.get(tail).remove(head)  # rimuove head dalla lista di adiacenza di tail
        self.edges.get(head).remove(tail)  # rimuove tail dalla lista di adiacenza di head

    def getEdge(self, tail, head):
        '''
        :return: (head, tail) if the edge exists, None otherwise
        '''
        if head in self.edges.get(tail):
            return tuple({head, tail})
        return None

    def getEdges(self):
        l = []
        for head in self.edges.keys():
            for tail in self.edges.get(head):
                if not (tail, head) in l:
                    l.append((head, tail))
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

        F = PriorityQueue(self.qtype).queue         #inizializzazione della frangia
        assert F is not None, "Tipo coda non valida"
        """
        Tweak per l'inserimento del peso in una Coda con Priorità:
        l'implementazione delle code presente nelle Librerie mantiene in alto il minimo valore
        disponibile, mentre il testo del progetto rchiede che la nostra coda mantenga in alto
        la massima priorità. Per ovviare al problema si inseriscono come chiavi dei nodeId i
        pesi con segno negativo.
        """

        F.insert(nodeMaxPriority, -nodeMaxPriority.weight)      #inizializziamo F con il nodo di costo maggiore (nodo, peso)
        visited_nodes = []
        explored_nodes = set()

        while not F.isEmpty():  # while there are nodes to explore ...
            node = F.findMin()   # findMin() ritorna l'id del nodo con priorità massima
            F.deleteMin()
            explored_nodes |= {node.id}
            visited_nodes.append(node)
            # add all adjacent unexplored nodes to the stack
            if len(F.heap) + len(visited_nodes) < self.numNodes():
                for adj_nodeId in self.getAdj(node.id):
                    if adj_nodeId not in explored_nodes:
                        F.insert(self.getNode(adj_nodeId), -self.getNode(adj_nodeId).weight)
        return visited_nodes

    def print(self):
        listOfNodes = []
        listOfEdges = []
        for node in self.getNodes():
            listOfNodes.append((node.id, node.value, node.weight))
        for edgeOfNodes in self.getEdges():
            listOfEdges.append((edgeOfNodes[0].id, edgeOfNodes[1].id))
        print(f"Nel grafo sono presenti i seguenti elementi in formato (ID, VALUE, WEIGHT):\n{listOfNodes}\nEd i seguenti archi:\n{listOfEdges}")

if __name__ == "__main__":
    G = CustomGraph(TypeQueue.BINOMH)
    a = G.addWeightedNode('a', 12)
    b = G.addWeightedNode('b', 23)
    c = G.addWeightedNode('c', 45)
    G.insertEdge(a, b)
    G.insertEdge(b, c)
    G.insertEdge(c, a)
    G.getNode(1)
    G.getNodes()
    G.getEdges()
    G.visitaInPriorita()
    G.print()
