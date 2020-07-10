# from django.contrib.gis.geos import Point
# from django.contrib.gis.db import models

from django.db import models

from members.models import User


class Box(models.Model):
    id = models.IntegerField(unique=True, primary_key=True, help_text='크로스핏 박스 번호')
    boxname = models.CharField(max_length=150, help_text='크로스핏 박스 이름')
    boxwebsite = models.URLField(max_length=255, help_text='크로스핏 박스 URL')
    boxaddress = models.CharField(max_length=255, help_text='크로스핏 박스 주소')
    boxcity = models.CharField(max_length=100, help_text='크로스핏 박스 도시')
    boxstate = models.CharField(max_length=100)
    boxcountry = models.CharField(max_length=100, help_text='크로스핏 박스 나라')
    boxcfkids = models.BooleanField()
    boxzipcode = models.CharField(max_length=100, help_text='zip_code')
    boxphone = models.CharField(max_length=100, help_text='전화번호')
    boxlat = models.FloatField(help_text='위도')
    boxlng = models.FloatField(help_text='경도')
    comment = models.ManyToManyField('BoxComment')
    def __str__(self):
        return self.boxname


class BoxComment(models.Model):
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.box