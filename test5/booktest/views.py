from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
from django.core.paginator import Paginator
from .models import *
from django.http import JsonResponse
import json


# Create your views here.


def index(request):
    return render(request, 'booktest/index.html')


def upload(request):
    f1 = request.FILES.get('pic')
    '''
    七牛云
    
    '''

    filename = '%s/booktest/%s' % (settings.MEDIA_ROOT, f1.name)

    with open(filename, 'wb') as pic:
        for c in f1.chunks():  # 分片写入
            pic.write(c)

    return HttpResponse("<img src='http://pcxfnejm2.bkt.clouddn.com/Fg0Fox9NjSZLUxnKyJVp1aQaTVz0'>")  # 把图片返回


def page_text(request, index):
    list = HeroInfo.objects.all()  # 惰性执行
    # print(list)
    paginator = Paginator(list, 3)
    if index == '':
        index = 1
    hero_list = paginator.page(int(index))
    # print(hero_list.object_list)
    ctx = {
        'hero_list': hero_list,

    }
    return render(request, 'booktest/index1.html', ctx)


def index3(request):
    return render(request, 'booktest/index3.html')


def pro(request):
    pros = AreaInfo.objects.filter(parent__isnull=True).values()
    return JsonResponse({'data': list(pros)})
    # return render(request, 'booktest/index3.html')


# JSONView
def city(request, pid):
    citys = AreaInfo.objects.filter(parent_id=pid).values()
    return HttpResponse(json.dumps({"data": list(citys)}), 'application/json')
