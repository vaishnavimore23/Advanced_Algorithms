#Vallari Rajurkar
#Vaishnavi More


from sklearn import svm
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier

data=pd.read_csv("banknotes.csv")
#print(data.head())
X_train,X_test,y_train,y_test= train_test_split(data.iloc[:,:-1],data.iloc[:,-1],test_size=0.3,random_state=100)

svmmodel=svm.SVC()
svmmodel.fit(X_train,y_train)
y_pred_svm= svmmodel.predict(X_test)
print("Accuracy of SVM classifier = ",metrics.accuracy_score(y_test,y_pred_svm)*100)


knnmodel=KNeighborsClassifier(n_neighbors=5)
knnmodel.fit(X_train,y_train)
y_pred_knn=knnmodel.predict(X_test)
print("Accuracy of KNN classifier = ",metrics.accuracy_score(y_test,y_pred_knn)*100)
