import numpy as np
def PerceptronTrain(X,Y,lr=1,times=1000):
    X=np.array(X)
    Y=np.array(Y)
    w=np.random.random(X.shape[1])
    b=np.random.random(1)
    for _ in range(times):
        OUT=np.sign(np.dot(X,w)+b)
        if (OUT==Y).all():
            break
        else:
            n=0
            for i in X:
                while np.sign(np.dot(i,w)+b)!=Y[n]:
                    w=w+lr * np.dot(Y[n], i)
                    b=b+Y[n]
                n+=1
    print(w,b)
X=[[1,3],[1,4],[1,1]]
Y=[1,1,-1]
PerceptronTrain(X,Y)
