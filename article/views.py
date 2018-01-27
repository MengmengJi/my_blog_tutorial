from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime
from django.http import Http404
from django.contrib.syndication.views import Feed
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def home(request):
    posts = Article.objects.all()    #获取全部的Article对象
    paginator = Paginator(posts, 2)  #每页显示两个
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.paginator(paginator.num_pages)
    return render(request, 'home.html', {'post_list':post_list})

def detail(request, id):
    try:
        post = Article.objects.get(id = str(id))
        #因为id是每个博文的唯一标识，所以这里使用id对数据库中的博文进行查找
    except Article.DoesNotExist:
        raise Http404 
    return render(request, 'post.html', {'post': post})
    #return HttpResponse("You're looking at my_args %s." % my_args)

#归档，列出博客中所有的文章，可显示时间
def archives(request):
    try:
        post_list = Article.objects.all()
    except Article.DoesNotExist:
        raise HttpResponse
    return render(request, 'archives.html', {'post_list': post_list, 'error': False})

#定义自己喜欢的简介
def about_me(request):
    return render(request, 'aboutme.html')

#标签分类，点击对应的标签按钮，会跳转到一个新的页面，这个页面是所有相关的标签的文章的罗列
#看成是对tag的查询操作，通过传入对应的tag，然后对tag进行查询
def search_tag(request, tag):
    try:
        post_list = Article.objects.filter(category = tag)  #contains
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'tag.html', {'post_list':post_list})

#搜索功能，添加查询逻辑，前端界面输入搜索关键字，传送到对应view中，在对应view中进行关键字搜索
#可以只对文章名搜索或者全文搜索
def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request, 'home.html')
        else:
            post_list = Article.objects.filter(title = s)
            if len(post_list) == 0:
                return render(request, 'archives.html', {'post_list': post_list, 'error': True})
            else:
                return render(request, 'archives.html', {'post_list': post_list, 'error': False})
    return redirect('/')

    #render函数中第一个参数是request对象， 第二个参数是一个模版名称， 第三个参数是一个字典类型的可选参数
    #它将返回一个包含有给定模版，根据给定的上下文渲染结果的 HttpResponse 对象


class RSSFeed(Feed):
    title = "RSS feed - article"
    link = "feeds/posts/"
    description = "RSS feed - blog posts"

    def items(self):
        return Article.objects.order_by('-date_time')

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.date_time

    def item_description(self, item):
        return item.content

