from numpy import *

def loadDataSet(fileName):
    numFeat = len(open(fileName).readline().split('\t')) - 1 # 获取样本特征的总数，不算最后的目标变量
    dataMat = []
    labelMat = []
    fr = open(fileName)
    for line in fr.readlines(): # 读取每一行
        lineArr = []
        curline = line.strip().split('\t') # 删除一行中以tab分隔的数据前后的空白符号
        for i in range(numFeat):
            lineArr.append(float(curline[i])) #不包括最后一列
        dataMat.append(lineArr)
        labelMat.append(float(curline[-1]))
    return dataMat, labelMat


def standRegres(xArr, yArr):
    xMat = mat(xArr)
    yMat = mat(yArr).T
    xTx = xMat.T * xMat
    if linalg.det(xTx) == 0.0:
        print("This matrix is singular, cannot do inverse")
        return
    theta = xTx.I * (xMat.T * yMat)
    return theta


# 测试-----------------------------------------------------------------------------------------------------
xArr, yArr = loadDataSet('data.txt')
print(standRegres(xArr, yArr))
