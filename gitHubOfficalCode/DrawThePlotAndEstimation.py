import math
import pickle
import numpy as np
from matplotlib import pyplot as plt

class pubMed:
    def __init__(self):
        self.data = {}

    def loadDocument(self, filename, label):
        with open(filename, 'rb') as f:
            xy = pickle.load(f)
            x, y = [], []
            for xAndy in xy:
                x.append(xAndy[0])
                y.append(xAndy[1])
                # x.append(math.log10(xAndy[0]))
                # y.append(math.log10(xAndy[1]))
            self.data[label] = (x, y)

    def DrawHeapLaw(self, step):
        colors = ['r', 'g', 'b']
        plt.ylabel('Vocabulary Size')
        plt.xlabel('Collection Size')
        plt.title("Heaps' law")

        for idx, (label, (x, y)) in enumerate(self.data.items()):
            step -= 1
            i = 0
            print(x)
            filtered_x, filtered_y = [], []
            while i < len(x):

                filtered_x.append(x[i])
                filtered_y.append(y[i])
                i += step
            plt.plot(filtered_x, filtered_y, color=colors[idx], label=label)
            beta  ,  logk = np.polyfit(filtered_x, filtered_y, 1)
            print(f"Slope for {label}: {beta}")
            print(f"Slope for {label}: {10**logk}")




        plt.legend()
        plt.grid(True)
        plt.savefig('-loglog.pdf', transparent=True)
        plt.show()


onehu = pubMed()
files = [ 'heapLawData-selectedPromt.pkl' , "heaplaw125m.pkl","heaplaw1.3b.pkl"]
labels = ["PubMed","125m","1.3b" ]
for file, label in zip(files, labels):
    onehu.loadDocument(file, label)

onehu.DrawHeapLaw(10)
