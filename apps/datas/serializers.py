from rest_framework import serializers
from .models import Api_test1
from .models import Api_test2

class Api_test1_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Api_test1
        fields = ['mean_radius','mean_texture','cancer']

class Api_test2_Serializer(serializers.ModelSerializer):

    class Meta:
        model = Api_test2
        fields = ['sepal_length','sepal_width','petal_length','petal_width','target']