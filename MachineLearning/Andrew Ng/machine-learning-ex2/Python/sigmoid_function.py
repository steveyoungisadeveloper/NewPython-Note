from numpy import *
import numpy as np



#load data
def file2matrix(filename):
    fr = open(filename)
    numberOfLine = len(fr.readlines())
    X = zeros((numberOfLine,3))#双括号 外围是zeros() 内维是（1，3）
    Y = zeros((numberOfLine,1))
    i = 0
    fr = open(filename)
    for line in fr.readlines():
        line = line.strip()
        listFromLine = line.split(',')
        X[i,:] = [1, listFromLine[0], listFromLine[1]]
        Y[i,:] = [listFromLine[2]]
        i += 1
    return X, Y


#----------------------------------------------------------------------------------


def sigmoid(g):
    h = 1/(1+exp(-g))
    return h

def costFun(x, theta, y, iterate, alpha):
    m = len(y)
    J_history = []
    for i in range(iterate):
        g = dot(x , theta)
        h = sigmoid(g)
        loss = h - y
        gradient = dot(x.T, loss) / m
        J = (-dot(np.transpose(y),np.log(h))-np.dot(np.transpose(1-y),np.log(1-h)))/m
    return gradient, J


fr = "ex2data1.txt"
x,y = file2matrix(fr)
theta = zeros((3,1))
iterate = 1
alpha = 1


# z = dot(x , theta)
# h = sigmoid(z)
# m = len(y)
# temp0 = theta[0] - alpha / m * (sum((h - y) * x[:,0]))
# temp1 = theta[1] - alpha / m * (sum((h - y) * x[:,1]))
# theta[2] = theta[2] - alpha / m * (sum((h - y) * x[:,2]))
# theta[0] = temp0
# theta[1] = temp1
# z = dot(x , theta)
# h = sigmoid(z)
# J = (1 / m) * (sum(-y * log10(h) - (1-y) * log10(1-h)))
# print(z,J)


gradient, J = costFun(x,theta,y,iterate,alpha)



print("theta is", gradient)
print("Cost is", J) # 不知道为什么J 大了1000倍
