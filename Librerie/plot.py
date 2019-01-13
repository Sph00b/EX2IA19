import matplotlib.pyplot as plt
from pandas import read_csv

def plot(s):
    names = ["PyDictionary","CustomDictionary_Parametri_Buoni","CustomDictionary_Parametri_Cattivi"] #filenames
    c = 0       #color
    for f in names:
        d = read_csv("../Data/" + s + f + ".csv", sep = ',', header = None)  # read file
        x = d[0].values
        y = d[1].values
        plt.plot(x, y, color = "C" + str(c), label = f)
        plt.legend(loc = "best")
        c += 1
    plt.savefig("../Graph/"+s+".png")
    plt.show()

if __name__ == "__main__":
    plot("Utilizzo")
    plot("Insert")
    plot("Search")
    plot("Deleate")
