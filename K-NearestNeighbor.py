# -*- coding: UTF-8 -*-
import numpy as np
def KNN(X,Y,NewInput,k=1):
#输入：X：样本数据
#      Y:期望类别
#      NewInput:待分类样本
#      k:最邻近的k个实例
#输出：maxlabel:分类结果
    X=np.array(X)
    Y=np.array([str(i) for i in Y])
    NewInput=np.array(NewInput)
    NewInput = np.tile(NewInput, (X.shape[0], 1))
    distance = sum(((NewInput - X) ** 2).T)
    sort=np.argsort(distance)
    vote={}
    maxtimes=0
    for i in range(k):
        vote[Y[sort[i]]]=vote.get(Y[sort[i]],0)+1
    for label,times in vote.items():
        maxtimes=times
        maxlabel=label
    return maxlabel


X=[[1,3],[2,4],[-2,1],[2.3,0]]
Y=[1,0,1,0]
NewInput=[1.5,2]
print(KNN(X,Y,NewInput))
