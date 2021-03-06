#!/usr/bin/python


"""
    Starter code for the validation mini-project.
    The first step toward building your POI identifier!

    Start by loading/formatting the data

    After that, it's not our code anymore--it's yours!
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score, train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "rb") )

### first element is our labels, any added elements are predictor
### features. Keep this the same for the mini-project, but you'll
### have a different feature list when you do the final project.
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list, sort_keys = '../tools/python2_lesson13_keys.pkl')
labels, features = targetFeatureSplit(data)

### it's all yours from here forward!  
dtc = DecisionTreeClassifier(random_state=0)

features_train, features_test, labels_train, labels_test = train_test_split(
        features, labels, test_size=0.3, random_state=42)

dtc.fit(features_train, labels_train)

s = dtc.score(features_test, labels_test)

pred = dtc.predict(features_test)

acc = accuracy_score(labels_test, pred)
print(acc)

prec = precision_score(labels_test, pred)
print(prec)

rec = recall_score(labels_test, pred)
print(rec)

