from .models import studentclass
from rest_framework import serializers
class stuSerializers(serializers.ModelSerializer):
     class Meta:
         model=studentclass
         fields=['name','age','id']
         