import numpy as np
import matplotlib.pyplot as plt


class Perceptron(object):

    '''
        Trying to follow industry standards, here's my first code with description :')

        How a perceptron works:
        1. take input nodes and one bias node.
        2. take weights = 0 for each input node and the bias, therefore, len(input_nodes+1) = len(weights)
        3. summation, i.e. dot product for the weights and the nodes including the bias.
        4. activation function to declare the value of the perceptron, y' or y_out as 0 or 1.
        So, perceptron is a binary classifier. If you are using a single layer perceptron, chances are, any other classification model
        like logistic regression/svm and so on would work just as well.
    '''

    def __init__(self, number_of_inputs=0, epochs=1000, learning_rate=0.01):
        '''
            parameterized constructer to give the object the number of input nodes, +1 would be bias
            the epoches is how many times we run the loop to train our perceptron
            the learning rate that should be really low. 0.05 is a good number
        '''
        self.epochs = epochs
        self.learning_rate = learning_rate
        # Weights + bias node
        self.weights = np.zeros(number_of_inputs)
        self.bias = 0

    def activation_function(self, y_out):
        return np.where(y_out >= 0, 1, 0)

    def fit(self, inputs, output):

        n_samples, n_features = inputs.shape
        self.weights = np.zeros(n_features)

        output_array = np.array([1 if i > 0 else 0 for i in output])

        for _ in range(self.epochs):

            for i, input_i in enumerate(inputs):

                y_net = np.dot(input_i, self.weights) + self.bias
                y_out = self.activation_function(y_net)

                update = self.learning_rate * (output_array[i] - y_out)
                self.weights += update * input_i
                self.bias += update

    def predict(self, inputs):
        '''
            We are summing up the (inputs+bias * weights)  for each input and then returning a y_out value
            y_out is our y' i.e. output of the perceptron
        '''
        y_net = np.dot(inputs, self.weights) + self.bias

        y_out = self.activation_function(y_net)

        return y_out
