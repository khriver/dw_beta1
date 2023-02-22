#from apps.models.functions.evalModel.evaluate import *
import pandas as pd
from sklearn.metrics import accuracy_score, confusion_matrix,f1_score, roc_curve, auc, roc_auc_score
from django.core.cache import cache
class evalModel:
    def __init__(self,filename,data,modelname):
        self.filename = filename
        self.name = modelname
        self.x_train = data['x_train']
        self.y_train = data['y_train']
        self.x_test = data['x_test']
        self.y_test = data['y_test']

    def eval(self):
        clf = cache.get(f'{self.filename}_clf')
        y_prob = clf.predict_proba(self.x_test)[:,1]
        y_pred = clf.predict(self.x_test)
        print("f1:",f1_score(self.y_test,y_pred))
        print("Accuracy:",accuracy_score(self.y_test, y_pred))
        print("AUC:",roc_auc_score(self.y_test, y_prob))




