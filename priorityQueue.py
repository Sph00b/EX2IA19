from Librerie.priorityQueues.PQbinomialHeap import PQbinomialHeap
from Librerie.priorityQueues.PQ_Dheap import PQ_DHeap
from Librerie.priorityQueues.PQbinaryHeap import PQbinaryHeap
from enum import Enum

class TypeQueue(Enum):
    BINARH = 1  #Binary Heap
    BINOMH = 2  #Binomial Heap
    DHEAP3 = 3   #D-Heap, d=10
    DHEAP10 = 4   #D-Heap, d=10
    DHEAP100 = 5   #D-Heap, d=10

class PriorityQueue:
    def __init__(self, type):
        self.queue = None
        if type == TypeQueue.BINARH:
            self.queue = PQbinaryHeap()
        elif type == TypeQueue.BINOMH:
            self.queue = PQbinomialHeap()
        elif type == TypeQueue.DHEAP3:
            self.queue = PQ_DHeap(3)
        elif type == TypeQueue.DHEAP10:
            self.queue = PQ_DHeap(10)
        elif type == TypeQueue.DHEAP100:
            self.queue = PQ_DHeap(100)
