from django.shortcuts import render
from .models import Rank
from django.http import JsonResponse,HttpResponse
import json
# Create your views here

def get_ranks(request):
    """
    个人设置最多返回10条消息,
    通过post方式提交查询的起始位置和结束位置


    """
    if request.method=='POST':
        start_range = int(request.POST.get('start_range',1))
        end_range = int(request.POST.get('end_range',start_range+10))
        client_number = request.POST.get('client_number')

        try:
            range_queryset = Rank.objects.all().order_by('-score')
        except Exception as e:
            print(e)
            result = {'code':'412','data':'数据库异常'}
            return JsonResponse(result)
        # 对查询对象转json

        client_rank = {}

        list_result=[]
        for i ,data in enumerate(range_queryset):
            obj = {}
            obj['id'] = data.id
            obj['clients'] = data.clients
            obj['score'] = data.score
            obj['rank'] = i+1
            list_result.append(obj)
            if data.clients ==client_number:
                client_rank=obj

        #对前端范围进行切片处理，并在最后添加上访问客户端的信息
        list_result = list_result[start_range - 1:end_range]
        list_result.append(client_rank)



        result = {'list':list_result}
        return JsonResponse(result)
    else:
        return HttpResponse('无效请求')


def commit_score(request):

    if request.method == 'POST':
        client_number = request.POST.get('client_number')
        score = request.POST.get('score')

        try:
            Rank.objects.create(clients=client_number,score=score)
        except Exception as e:
            print(e)
            result = {'code':400,'error':'Bad request'}
            return JsonResponse(result)
        result = {'code':201,'data':'数据创建成功'}
        return JsonResponse(result)
    else:
        return HttpResponse('无效请求')