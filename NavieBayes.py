# -*- coding: UTF-8 -*-
import pandas as pd
def NavieBayes(X,Y,NewInput):
#输入：X:样本数据
#      Y:期望输出
#      NewInput:待分类样本
#输出：Probility:所有输出种类的概率（字典形式储存）
#      maxLable:分类结果
    X=pd.DataFrame(X)
    Y=pd.Series(Y)
    Feature=X.columns
    Ylable=Y.unique()
    column = X.columns
    YP={}
    Probility={}
    for i in Ylable:
        number=Y[Y.isin([i])]
        P=len(number)/len(Y)
        YP[str(i)]=P
        XSample=X[Y.isin([i])]
        x=0
        PP=1
        for j in column:
            Feature=NewInput[x]
            x+=1
            XY=XSample[XSample[j].isin([Feature])]
            PP=PP*len(XY)/len(XSample)
        Probility[str(i)]=P*PP
    maxPro=0
    for lable,Pro in Probility.items():
        if maxPro<Pro:
            maxPro=Pro
            maxLable=lable
    return maxLable,Probility




New=[2,'S']
X={'x1':[1,1,1,1,1,2,2,2,2,2,3,3,3,3,3],
   'x2':['S','M','M','S','S','S','M','M','L','L','L','M','M','L','L']}
Y=[-1,-1,1,1,-1,-1,-1,1,1,1,1,1,1,1,-1]
print(NavieBayes(X,Y,New))