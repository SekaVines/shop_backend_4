from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ProductSerializer, ProductDetailSerializer, ProductReviewSerializer, ReviewSerializer, TagSerializer
from .models import Product, Review, Tag

@api_view(['GET'])
def product_list_view(request):
    products = Product.objects.all()
    data = ProductSerializer(products, many=True).data
    return Response(data=data)


# @api_view(['GET'])
# def product_detail_view(request, id):
#     try:
#         product = Product.objects.get(id=id)
#     except Product.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND,
#                         data={'error': 'Product not found!'})
#     data = ProductDetailSerializer(product, many=False).data
#     return Response(data=data)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_view(request, id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND,
                        data={'error': 'Product not found!'})
    if request.method == 'GET':
        data = ProductDetailSerializer(product, many=False).data
        return Response(data=data)
    elif request.method == 'PUT':
        serializer = ProductUpdateValidateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE,
            data={'message': 'error',
            'errors': serializer.errors})
        product.title = request.data['title']
        product.description = request.data.get('description', '')
        product.price = request.data['price']
        product.category_id = request.data['category']
        product.tags.set(request.data['tags'])
        product.save()
        return Response(data={'massage': 'Product updated!'})
    elif request.method == 'DELETE':
        product.delete()
        return Response(data={'message': 'Product successfully removed!'})



@api_view(['GET'])
def product_with_review_list_view(request):
    products = Product.objects.all()
    data = ProductReviewSerializer(products, many=True).data
    return Response(data=data)

@api_view(['GET'])
def product_with_tag_list_view(request):
    tags = Tag.objects.all()
    data = TagSerializer(tags.filter(is_active=True), many=True).data
    return Response(data=data)









