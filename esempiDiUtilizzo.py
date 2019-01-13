from customGraph import CustomGraph
from graphGenerator import graphGenerator
from priorityQueue import TypeQueue
import random

def printNodeList(l):
    s = "["
    for node in l:
        s += "("+str(node.weight)+")"
    print(f"{s}]")

G = CustomGraph(TypeQueue(1))

gen = graphGenerator(G)
for _ in range(10):
    next(gen)

lista = G.getNodes()
a = G.addWeightedNode("a", 33)
G.insertEdge(a.id, random.choice(lista).id)

b = G.addWeightedNode("b", 45)
c = G.addWeightedNode("c", 54)
d = G.addWeightedNode("d", 69)
e = G.addWeightedNode("e", 72)

G.insertEdge(a.id,b.id)
G.insertEdge(b.id,c.id)
G.insertEdge(c.id, d.id)
G.insertEdge(e.id,d.id)
G.insertEdge(b.id,e.id)
# il grafo G è ancora connesso
G.print()

h = random.choice(G.getNodes())
print(h.value)

# cancelliamo tutti i nodi con id dispari
for node in G.getNodes():
    if node.id%2 is not 0:
        G.deleteNode(node.id)

# crea un arco tra due nodi casuali se non sono adiacenti
f = random.choice(G.getNodes())
g = random.choice(G.getNodes())
if not G.isAdj(f.id,g.id) and f is not g:
    G.insertEdge(f.id,g.id)
G.print()

print(G.deg(a.id))

if G.numEdges() < G.numNodes() -1:
    print("Sicuramente il grafo non è connesso")

printNodeList(G.visitaInPriorita())

nodeList = G.getNodes()
for n in range(0, len(nodeList)):
    for m in range(n+1, len(nodeList)):
        G.insertEdge(nodeList[n].id, nodeList[m].id)

printNodeList(G.visitaInPriorita())










