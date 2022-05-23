from rest_framework import serizlizers
from .models import Car

class Carserializer(serizlizers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id','make','model','year','price']