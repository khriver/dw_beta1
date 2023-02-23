from sklearn import svm
from sklearn.metrics import confusion_matrix
from catboost import CatBoostClassifier

def support_vector_machine(self):  # params  = { 'C' : 100~1000 , 'kernel' : 'linear','rbf',
    clf = svm.SVC(kernel=self.params['kernel'], C=self.params['Const'])
    clf.fit(self.x_train, self.y_train)
    return clf
def catboost(self):
    clf = CatBoostClassifier(iteration = 2, depth = 2, learning_rate= 1, verbose = False)
    clf.fit(self.x_train, self.y_train)
    return clf
