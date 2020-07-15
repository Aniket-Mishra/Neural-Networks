# Hebbian Learning
# 1. Initialize Weights
# 2. Netj = xj*wij
# 3. if netj >= 0, y_f = 1
# if netj < 0, y_f = -1

# 4. if h_f = y (target), stop

# else:
# if y_f != ym revise weights
#
# 5. wj_new - wj_old + xjOj
# for bias: b_new = b_old + 1*Oj
# Oj = output


X1 = [0.25, 0.25, 0.5, 0.5, 0.75, 0.75, 1, 1]
X2 = [0.353, 0.471, 0.353, 0.647, 0.705, 0.882, 0.705, 1]
Y = [0, 1, 0, 1, 0, 1, 0, 1]

#perceptron => net >= 0 => y' = 1 else y' = 0
# alpha 0 <= @ >= 1
# y' > y => sub @x else add @x

weight_1, weight_2, bias, learning_rate = 0, 0, 0, 0.5

for i in range(0, len(X1)):
    element_x1 = int(X1[i])
    element_x2 = int(X2[i])

    #print("e1 = {} e2 = {}".format(element_x1, element_x2))

    net = element_x1*weight_1 + element_x2*weight_2 + Y*bias
    if net >= 0:
        Yop = 1
    else:
        Yop = 0

    if Yop == Y:
        continue
    else:
        if Yop > Y:
            weight_1 = weight_1 - learning_rate*X1[i]
            weight_2 = weight_2 - learning_rate*X2[i]
            i=0
        else:
            weight_1 = weight_1 + learning_rate*X1[i]
            weight_2 = weight_2 + learning_rate*X2[i]
            i=0

print("Weight 1 - {} and weight 2 - {} and bias is {}".format(weight_1, weight_2, bias))
