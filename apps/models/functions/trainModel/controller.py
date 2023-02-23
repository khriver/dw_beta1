from apps.models.functions.trainModel.modeling import *
from django.core.cache import cache
class trainModel:
    def __init__(self,filename,data,modelname,hyperparams):
        self.filename = filename
        self.name = modelname
        self.params = hyperparams
        self.x_train = data['x_train']
        self.y_train = data['y_train']
        self.x_test = data['x_test']
        self.y_test = data['y_test']

    def train(self):
        if self.name == 'svm':
            clf = support_vector_machine(self)
        if self.name == 'catboost':
            clf = catboost(self)

        cache.set(f'{self.filename}_clf',clf)



