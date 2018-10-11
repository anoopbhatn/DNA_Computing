import numpy as np
import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D

# Plotting accuracies of different classifiers for whole training data

x=[0,2,5,8,11]
classifiers=['','Decision Tree','Logistic Regression','KNN','SVM']
accuracies=[0,81.73,73.98,72.18,97.62]

plt.axis((0,12,60,120))
plt.xticks(x,classifiers)
plt.plot(x,accuracies,'bo')
plt.show()