from django.urls import path
from .views import *

urlpatterns = [
    path('load/',loadDataView.as_view()),
    path('upload/',uploadDataView.as_view()),
    path('split/',handleDataView.as_view())
]