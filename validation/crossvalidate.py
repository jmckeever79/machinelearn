from sklearn import model_selection as ms
from sklearn import datasets as ds
from sklearn import svm

iris = ds.load_iris()

print(iris.data.shape, iris.target.shape)

x_train, x_test, y_train, y_test = ms.train_test_split(iris.data,
                                                       iris.target,
                                                       test_size = 0.4,
                                                       random_state = 0)

print(x_train.shape, x_test.shape)
print(y_train.shape, y_test.shape)

clf = svm.SVC(kernel = 'linear', C = 1).fit(x_train, y_train)

s = clf.score(x_test, y_test)

print(s)