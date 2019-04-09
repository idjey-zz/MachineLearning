#Library Import
from sklearn import tree


#Lables and Features input
features = [[2,2],[2,2],[3,4],[2,2],[4,4],[4,4],[3,2],[2,2]]
labels = [0,0,1,0,1,1,0,0]



#Initialize Classification Algorithm DecisionTree
algorithm = tree.DecisionTreeClassifier()



#Training with data (Model Fitting)
algorithm = algorithm.fit(features, labels)


#TestData (Checking model with test data)
newData = [[3,4]]


#Displaying Output
print(algorithm.predict(newData))





