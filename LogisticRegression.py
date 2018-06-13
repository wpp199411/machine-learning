# -*- coding: UTF-8 -*-
import numpy as np
#输入：X：样本数据
#      Y：期望输出
#     NewInput：待分类数据
#      alpha：学习率，默认0.01
#      times：最大迭代步数，默认1000
#      errors：误差阈值
#输出：w：权值
#      Label：分类结果
def LogisticRegression(X,Y,NewInput,alpha=0.01,times=1000,error=0.01):
    X=np.mat(X)
    Y=np.mat(Y)
    a,b=np.shape(X)
    w=np.random.random((b,1))
    for i in range(times):
        OUT=1.0/(1+np.exp(-X*w))
        Error=Y.T-OUT
        if sum(abs(Error))>error:
            w=w+alpha*X.T*Error
    print('训练误差为\ned',sum(abs(Error)))
    Label = np.sign(1.0 / (1 + np.exp(-np.dot(NewInput , w)))-0.5)
    return w,Label

#使用Perceptron.py的实验数据
if __name__ == '__main__':
    X=[[1,3],[1,4],[1,1]]
    Y=[1,1,-1]
    NewInput=[1,2]
    a,b=LogisticRegression(X,Y,NewInput)
    print('权值为\n',a,'\n分类结果为\n',b)