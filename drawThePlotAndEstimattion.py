import math
import pickle
import numpy as np
from matplotlib import pyplot as plt

class pubMed:
    def __init__(self):
        self.rawData = []

    def loadDocument(self, filename):
        with open(filename, 'rb') as f:
            self.rawData = pickle.load(f)[0:20000]

    def DrawHeapLaw(self):
        if len(self.rawData) < 2:  # Need at least two points to fit
            return None, None, None, None

        x, y = [], []
        for xAndy in self.rawData:
            x.append(math.log10(xAndy[0]))
            y.append(math.log10(xAndy[1]))

        beta, logk = np.polyfit(x, y, 1)
        return x, y, beta, logk


estimation = pubMed()
file = 'dataGenaration/result/heapLawData-selectedPromt.pkl'
estimation.loadDocument(file)

x, y, beta, logk = estimation.DrawHeapLaw()
print(beta)
print(logk)


# Check if data is sufficient for plotting
if x is not None and y is not None:
    # Plotting the result
    plt.figure(figsize=(10, 5))
    plt.scatter(x, y, label='Data Points')
    plt.plot([min(x), max(x)], [beta * min(x) + logk, beta * max(x) + logk], color='red', label='Fitted Line')
    plt.xlabel('log10(X)')
    plt.ylabel('log10(Y)')
    plt.title('Heap\'s Law')
    plt.legend()
    plt.show()
else:
    print("Insufficient data for plotting.")
