"""Myblog URL Configuration

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
from django.conf.urls import include, url
from django.contrib import admin
from blog import views
from blog.views import index, view_category, view_post
from blog import views as blog_view

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index, name='index'),
    url(r'^blog/view/(?P<slug>[^\.]+).html', views.view_post, name='view_blog_post'),
    url(r'^blog/category/(?P<slug>[^\.]+).html', views.view_category, name='view_blog_category'),
   # url(r'^blog/view/(?P<slug>[^\.]+).html','Myblog.blog.views.view_post', name='view_blog_post',),
   # url(r'^blog/category/(?P<slug>[^\.]+).html','Myblog.blog.views.view_category',name='view_blog_category'),
]
