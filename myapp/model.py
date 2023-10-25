import numpy as np
import pandas as pd
import sklearn
import pickle   

data = pd.read_csv("Social_Network_Ads.csv")
# print(data.head())
print(data)

x = data.iloc[:, 2:4].values
y = data.iloc[:,-1].values

from sklearn.model_selection import train_test_split
x_train, x_test, y_train,y_test = train_test_split(x,y,test_size = 0.2)


from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)

ans = knn.fit(x_train, y_train)

print(ans)


# pickle.dump(knn, open('model.pkl'), 'wb')







