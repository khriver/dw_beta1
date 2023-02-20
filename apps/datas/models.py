from django.db import models

# Create your models here.
class Api_test1(models.Model):
    mean_radius = models.CharField(max_length=100)
    mean_texture = models.CharField(max_length=100)
    cancer = models.CharField(max_length=100)

    class Meta:
        managed = False #내 데이터베이스를 수정하지 않겠다!!!!
        db_table = 'api_test1' #내 스키마의 데이터를 가져올 테이블 이름

class Api_test2(models.Model):
    sepal_length = models.BigIntegerField()
    sepal_width = models.BigIntegerField()
    petal_length = models.BigIntegerField()
    petal_width = models.BigIntegerField()
    target = models.BigIntegerField()

    class Meta:
        managed = False #내 데이터베이스를 수정하지 않겠다!!!!
        db_table = 'api_test2' #내 스키마의 데이터를 가져올 테이블 이름




