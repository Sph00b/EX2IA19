from Librerie.Graph import GraphBase
from Librerie.Graph import Node

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
        self.edges = {}


    def addWeightedNode(self, elem, weight):
        """
        Add a new node with the specified value.
        :param elem: the node value.
        :return: the create node.
        """

        newNode = NodoPesato(self.nextId, elem, weight)
        self.nodes.update({self.nextId:newNode})
        self.nextId += 1
        return newNode


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

        F = codaPriorita()  # la definirò in seguito, deve essere intercambiabile, è la Frangia
        F.insert(nodeIdWithMaxPriority, self.nodes.get[nodeIdWithMaxPriority].weight)   # insert(elemento, chiave)

        # visited nodes initialization
        visited_nodes = []

        while not F.isEmpty():  # while there are nodes to explore ...
            node = F.deleteMin()
            visited_nodes.append(node)
            # add all adjacent unexplored nodes to the stack
            for adj_nodeId in self.getAdj(node):
                if adj_nodeId not in visited_nodes:
                    F.insert(adj_nodeId, self.nodes.get[nodeIdWithMaxPriority].weight)

        return visited_nodes