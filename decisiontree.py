import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from matplotlib.colors import ListedColormap

dataset=pd.read_csv(r"C:\Users\student\Desktop\PumpingData.csv")

X=dataset.iloc[:,[3,4]].values
y=dataset.iloc[:,5].values

from sklearn.model_selection import train_test_split

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=0)

from sklearn.tree import DecisionTreeClassifier
classi=DecisionTreeClassifier(criterion='entropy',random_state=0)
classi.fit(X_train,y_train)

y_pred=classi.predict(X_test)
print(y_pred)

from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)
print(cm)

arr=np.array(cm)
TP=int(arr[0, 0])
TN=int(arr[1, 1])
FP=int(arr[1, 0])
FN=int(arr[0, 1])
total=TP+TN+FP+FN
accuracy=(TP+TN)/total
Misclassificationrate=(FP+FN)/total

print(accuracy)
print(Misclassificationrate)


