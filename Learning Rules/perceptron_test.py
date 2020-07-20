import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets
import matplotlib.pyplot as plt

from Perceptron_Rule import Perceptron


def accuracy(y_true, y_pred):
    accuracy = np.sum(y_true == y_pred) / len(y_true)
    return accuracy


X, y = datasets.make_blobs(n_samples=150, n_features=2,
                           centers=2, cluster_std=1.05, random_state=2)
x_train, x_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=123)


p = Perceptron()
p.fit(x_train, y_train)
predictions = p.predict(x_test)

print('preceptron classification accuracy: ', accuracy(y_test, predictions))

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
plt.scatter(x_train[:, 0], x_train[:, 1], marker='o', c=y_train)

x0_1 = np.amin(x_train[:, 0])
x0_2 = np.amax(x_train[:, 0])

x1_1 = (-p.weights[0] * x0_1 - p.bias) / p.weights[1]
x1_2 = (-p.weights[0] * x0_2 - p.bias) / p.weights[1]


ax.plot([x0_1, x0_2], [x1_1, x1_2], 'k')

ymin = np.amin(x_train[:, 1])
ymax = np.amax(x_train[:, 1])
ax.set_ylim([ymin-3, ymax+3])

plt.show()
