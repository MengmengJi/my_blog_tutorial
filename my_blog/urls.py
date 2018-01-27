"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from article import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name = 'home'),
    url(r'^(?P<id>\d+)/$', views.detail, name = 'detail'),
    # url(r'^(?P<my_args>\d+)/$', views.detail, name='detail'),
    # url(r'^test/$', views.test),
]

#url(regex,view,kwargs,name)
#regex:regular expression的简写，字符串模式匹配的一种语法，Django将请求的URL从上至下依次匹配列表中的正则表达式，直到匹配一个为止
#view:当Django匹配了一个正则表达式就会调用指定的view逻辑，上面代码中会调用article/views.py中的home函数
#kwargs:任意关键字参数可传一个字典至目标view
#name命名你的URL，使url在Django的其他地方使用，特别是在模版中
