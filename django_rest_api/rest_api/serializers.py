from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','email','password','address','phone','create_at']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title','storeId','category','price','stock','condition','create_at']

class ProductImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title','productId','url']


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','userId','name','create_at']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id','userId','quatity']


class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = ['cartId','productId','quatity','create_at']

class FileUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileUpload
        fields = ['imgFile']

class JoinSerializer(serializers.ModelSerializer):
    product_details = ProductSerializer(source='productId')
    class Meta:
        model = CartItem
        fields = ['cartId','productId','quatity','product_details','create_at']