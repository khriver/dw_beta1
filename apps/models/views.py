from django.http import HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.cache import cache
from apps.models.functions.trainModel.controller import trainModel
from apps.models.functions.evalModel.controller import evalModel
import json

@method_decorator(csrf_exempt, name='dispatch')  # CSRF 우회하기 위한 방법 공부 추가 필요
class trainModelView(View):  # 클래스형 뷰 작성
    def get(self, request):
        filename = request.GET.get('filename')
        modelname = request.GET.get('modelname')
        hyperparams = json.loads(request.GET.get('hyperparams'))
        df = cache.get(f'{filename}_data')
        model_train = trainModel(filename,df,modelname,hyperparams)
        model_train.train()
        model_eval = evalModel(filename, df, modelname)
        model_eval.eval()



        return HttpResponse("get success!")
