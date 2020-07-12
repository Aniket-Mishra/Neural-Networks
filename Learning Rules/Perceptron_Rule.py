# Perceptron Learning
# 1. Initialize Weights
# 2. Netj = xj*wij
# 3. if netj >= 0, y_f = 1
# if netj < 0, y_f = 0

# 4. if h_f = y (target), stop

# else:
# if y_f != ym revise weights

# 5. wj_new - wj_old +- alpha*xj
#   if y_f < y, subtract
#   if y_f > y, Add
# where 0<= alpha <= 1
# alpha = learning rate
# for bias: b_new = b_old +- alpha*xj
