# -*- coding: UTF-8 -*-
from math import log
import operator
#使用operator模块的原因是其用c实现的，执行速度比python代码快。
#程序逻辑参考《统计学习方法》P63页，算法5.2（ID3算法）
def Entropy(X):
#根据分类的类别计算经验熵
#第一个for循环将不同类存储在字典SortLable中
#第二个for循环计算每个类的经验熵并累加
#返回在X样本下总的经验熵
     SampleLen=len(X)
     SortLable={}
     for Sample in X:
         SortResult=Sample[-1]
         SortLable[SortResult]=SortLable.get(SortResult,0)+1
     EmpiricalEntropy=0
     for key in SortLable:
          value=float(SortLable[key])/SampleLen
          EmpiricalEntropy -= value*log(value,2)
     return EmpiricalEntropy

def SplitData(X,axis,value):
#根据样本X，选择样本集对应维度axis中与value相等的样本，并把维度axis去除，为子树建立提供样本集
#for循环将和value相等的样本储存在列表ReSample中，并将用过的特征值value去除
#返回值是由于特征值value相等的样本组成的list，并去除了value所对应的特征属性
     ReSample=[]
     for Sample in X:
         if Sample[axis]==value:
             ReduceFeature=Sample[:axis]
             ReduceFeature.extend(Sample[axis+1:])
             ReSample.append(ReduceFeature)
     return ReSample

def ChooseBestFeatureToSplit(X):
#根据当前样本集X，选择信息增益最大的特征属性
#第一个for循环遍历所有特征属性，计算每个特征值的信息增益，并选择最大的信息增益
#第二个for循环是计算第i个特征属性中不同类别的经验熵并累加
#返回信息增益最大特征属性所对应的维度
     BaseEntropy=Entropy(X)
     FeatureNumbers=len(X[0])-1
     BestInfoGain=0
     Best=0
     for i in range(FeatureNumbers):
         FeatureList=[Feature[i] for Feature in X]
         UniqueFeature=set(FeatureList)
         NewEntropy=0
         FeatureiEntropy=0
         for SingleFeature in UniqueFeature:
             ReSample=SplitData(X,i,SingleFeature)
             a=float(len(ReSample)) / len(X)
             NewEntropy += a*Entropy(ReSample)
         InfoEntropy=BaseEntropy-NewEntropy
         if InfoEntropy>BestInfoGain:
             BestInfoGain=InfoEntropy
             Best=i
     return Best

def CreatDecisionTree(X,labels):
#循环递归创建决策树，先创建根节点，对应的不同特征值中的一个（看在字典中的存放顺序），创建下一个子节点，对应的子节点
#不同特征值中的一个，创建下一个子节点，知道满足第一个或第二个if条件结束创建子节点，退回当前子节点的父节点，开始下一个
#特征值的创建
#第一个if是所有类别相同，返回当前类
#第二个if是没有特征属性时返回当前类别最多的最为当前类
#for循环创建子树，知道满足第一个或第二个if才停止创建
#最后一个返回是在遍历完所有的不同特征值时才返回
     SortLabel=[Sample[-1] for Sample in X]
     if SortLabel.count(SortLabel[0])==len(SortLabel):
         return SortLabel[0]
     if len(X[0])==1:
         Majority={}
         for i in SortLabel:
             Majority[i]=Majority.get(i,0)+1
         SortLabel=sorted(Majority.iteritems(),key=operator.itemgetter,reverse=True)
         return SortLabel[0][0]
     BestFeature=ChooseBestFeatureToSplit(X)
     BestLabel=labels[BestFeature]
     del(labels[BestFeature])
     DecisionTree = {BestLabel:{}}
     F=[Sample[BestFeature] for Sample in X]
     unique=set(F)
     for value in unique:
         DecisionTree[BestLabel][value]=CreatDecisionTree(SplitData(X,BestFeature,value), labels)
     return DecisionTree

NewInput=[[0,1,0,0],[0,2,1,0]]
Z=[1,2,3,4,5]
X = [[0, 0, 0, 0, 'N'],
     [0, 0, 0, 1, 'N'],
     [1, 0, 0, 0, 'Y'],
     [2, 1, 0, 1, 'Y'],
     [2, 2, 1, 0, 'Y'],
     [2, 2, 1, 1, 'N'],
     [1, 2, 1, 1, 'Y']]
labels=['outlook', 'temperature', 'humidity', 'windy']
def digui(n):
        return n*digui(n-1)
digui(2)