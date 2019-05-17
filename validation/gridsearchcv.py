# -*- coding: utf-8 -*-
from sklearn import svm
from sklearn import model_selection as ms
import pickle
from sklearn import datasets


authors_file = '../tools/email_authors.pkl'
authors_file_handler = open(authors_file, "rb")
authors = pickle.load(authors_file_handler)
authors_file_handler.close()

iris = datasets.load_breast_cancer()

svr = svm.SVC()

parameters = {'kernel': ('linear','rbf'), 'C':[1,10]}
clf = ms.GridSearchCV(svr, parameters)
clf.fit(iris.data, iris.target)

print(clf.best_params_)
