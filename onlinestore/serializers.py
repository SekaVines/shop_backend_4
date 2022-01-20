from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import *


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductReviewSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True)

    class Meta:
        model = Product
        fields = ['reviews', 'title']


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductUpdateValidateSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=22)
    descriptions = serializers.CharField(required=False)
    price = serializers.FloatField()
    category = serializers.IntegerField()
    tags = serializers.ListField()

    def validate(self, attrs):
        title = attrs['title']
        products = Product.objects.filter(title=title)
        if products:
            raise ValidationError('Title already exists!')
        return title
