from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):


    class Meta:
        model = Product
        fields = '__all__' # 모든 필드 지정

