from django.shortcuts import render
from .models import Publisher
from django.http import HttpResponse, JsonResponse
from django.forms.models import model_to_dict
from django.core import serializers
import json
from . import serializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication


# Create your views here.


# def publishers(request):
# pub_list = Publisher.objects.all()
# pub_list = Publisher.objects.all().values()
# print(pub_list)
# 第一种办法 序列化json数据
# l = []
# for pub in pub_list:
#     d = {}
#     d['name'] = pub.name
#     d['address'] = pub.address
#     l.append(d)

# 这是第二种方案
# for pub in pub_list:
#     l.append(model_to_dict(pub))
# 第三种方案
# data = serializers.serialize('json', pub_list)

# 这是DRF提供的序列化
# p = Publisher.objects.all()
# d = serializer.PublisherSerializers(p, many=True)
# return HttpResponse(json.dumps(d.data), content_type='application/json')
# return JsonResponse(list(pub_list), safe=False
@api_view(['GET', 'POST'])
def publisher_list(request):
    if request.method == 'GET':
        queryset = Publisher.objects.all()
        s = serializer.PublisherSerializers(queryset, many=True)
        return Response(s.data)
    elif request.method == 'POST':
        s = serializer.PublisherSerializers(data=request.data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        else:
            return Response(s.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def publisher_detail(request, pk):
    try:
        p = Publisher.objects.get(pk=pk)
    except p.DoesNotExist:
        return Response(status.HTTP_204_NO_CONTENT)

    if request.method == 'GET':  # 获取单条数据
        p = serializer.PublisherSerializers(p)
        return Response(p.data)

    elif request.method == 'PUT':  # 更新
        p = serializer.PublisherSerializers(p, data=request.data)
        if p.is_valid():
            p.save()
            return Response(p.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':#删除
        p.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#
#
# {
#     'code':1,
#     'error':'das',
#     'data':[]
# }

