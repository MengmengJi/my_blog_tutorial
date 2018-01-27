from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
from django.http import Http404

# Create your views here.
def home(request):
    post_list = Article.objects.all()    #获取全部的Article对象
    return render(request, 'home.html', {'post_list':post_list})

def detail(request, id):
    try:
        post = Article.objects.get(id = str(id))
        #因为id是每个博文的唯一标识，所以这里使用id对数据库中的博文进行查找
    except Article.DoesNotExist:
        raise Http404 
    return render(request, 'post.html', {'post': post})
    #return HttpResponse("You're looking at my_args %s." % my_args)

    #render函数中第一个参数是request对象， 第二个参数是一个模版名称， 第三个参数是一个字典类型的可选参数
    #它将返回一个包含有给定模版，根据给定的上下文渲染结果的 HttpResponse 对象
