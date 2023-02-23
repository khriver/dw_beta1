from django.urls import path
from . import views

urlpatterns = [
    path('train/', views.trainModelView.as_view()) # 최종 url은 /앱이름/기능이름
]