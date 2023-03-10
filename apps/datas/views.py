from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from .models import Api_test1, Api_test2
from .serializers import Api_test1_Serializer, Api_test2_Serializer
from django.core.cache import cache
import pandas as pd
from sklearn.model_selection import train_test_split

@method_decorator(csrf_exempt, name = 'dispatch') #CSRF 우회하기 위한 방법 공부 추가 필요
class loadDataView(View): # 클래스형 뷰 작성
    def get(self, request):
        filename = request.GET.get('filename')
        type = request.GET.get('type')
        if type == 'database':
            query_set = Api_test1.objects.all()
            serializer = Api_test1_Serializer(query_set, many=True)
            return JsonResponse({ 'Success' : 'True','filename' : f'{filename}','file' : f'{serializer.data}'}, safe=False)

        return HttpResponse("get success!")
    

@method_decorator(csrf_exempt, name = 'dispatch') #CSRF 우회하기 위한 방법 공부 추가 필요
class uploadDataView(View): # 클래스형 뷰 작성
    def post(self,request):
        try:
            extension = request.POST.__getitem__('extension')
            file = request.FILES.__getitem__('file')
            filename = request.POST.__getitem__('filename')

            cachedata = {
                'extension' : extension,
                'file' : file,
                'filename' : filename
            }
            cache.set(f'{filename}',cachedata)

            return JsonResponse({"success" : 'True'})
        except Exception as e:
            print(e)
            return JsonResponse({'success' : 'False'})

@method_decorator(csrf_exempt, name = 'dispatch')
class handleDataView(View):
    def get(self,request):
        filename = request.GET.get('filename')
        trainratio = float(request.GET.get('trainratio'))
        file = cache.get(f'{filename}')['file']
        df = pd.read_csv(file)
        x_data = df.drop(columns='cancer')
        y_data = df['cancer'] #임시로 y값 설정
        x_train, x_test, y_train, y_test = train_test_split(x_data, y_data, train_size = trainratio)
        cache.set(f'{filename}_data', {'x_train': x_train, 'x_test': x_test, 'y_train': y_train, 'y_test': y_test})
        return JsonResponse({'train': len(x_train), 'test': len(x_test), 'success': 'True'})

