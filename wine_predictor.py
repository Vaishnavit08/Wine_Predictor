# This is a Wine Predictor Case study Can be Implemented by Using KNN algorithm.

from sklearn import metrics
from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split

def WinePredictor():
    # 1] Load the dataset
    wine=datasets.load_wine()

    # print the names of the Features
    print(wine.feature_names)

    # print the label species(class_0,class_1,class_2)
    print(wine.target_names)

    # print the wine data top 5 records
    print(wine.data[0:5])

    # print the wine labels(0:Class_0, 1:Class_1, 2:Class_2)
    print(wine.target)

    # split dataset into training and set and test set
    X_train, X_test ,Y_train,Y_test=train_test_split(wine.data,wine.target,test_size=0.3) 
    # here we gave the 70% training and 30% test

    # create KNN Classifier
    knn=KNeighborsClassifier(n_neighbors=3)

    # train the model using traing sets
    knn.fit(X_train,Y_train)

    # predict the response for test dataset
    y_pred=knn.predict(X_test)

    # Model Accuracy , how often the classifier correct?
    print("Accuracy : ", metrics.accuracy_score(Y_test,y_pred))


def main():
    print("---Vaishnavi_Pravin_Talekar---\n")
    print("Wine Predictor Application using KNN Algorithm\n")

    WinePredictor()

if __name__=="__main__":
    main()