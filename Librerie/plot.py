import matplotlib.pyplot as plt
from pandas import read_csv

def plot():
    names = ["DHEAP3","DHEAP10","DHEAP100"]#,"BINARH","BINOMH"] #filenames
    option = ["_FullEdges=False","_FullEdges=True"]
    c = 0       #color
    for o in option:
        for f in names:
            d = read_csv("../Data/CustomGraph_QueueType=" + f + o + ".csv", sep = ',', header = None)  # read file
            x = d[0].values
            y = d[1].values
            plt.plot(x, y, color = "C" + str(c), label = f)
            plt.legend(loc = "best")
            c += 1
        plt.savefig("../Graph/DHEAP" + o +"+.png")
        plt.show()

if __name__ == "__main__":
    plot()
