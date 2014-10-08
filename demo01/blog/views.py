# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import loader, Context, Template
from django.shortcuts import render_to_response
from blog.models import Employee, Entry, Blog
from django.conf import settings
# Create your views here.


class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age


def index(req):
    t = loader.get_template("index.html")
    c = Context({})
    return HttpResponse(t.render(c))


def detail(req):
    user = {"name": "wangwu", "age": 18}
    return render_to_response("detail.html", {"title": "Detail Page", "user": user})


def category(req):
    user = Person("lisi", 12)
    book_list = ["Pyton", "Java", "Android", "Object-c"]
    # return HttpResponse("<p>Hello,this is paragraph</p>")
    return render_to_response("detail.html", {"title": "Detail Page", "user": user, "book_list":book_list})


def detail3(req):
    t = Template('<h2>Hello template {{user}}</h2>')
    user = {"name": "wangwu", "age": 18}
    c = Context({'user': user})
    return HttpResponse(t.render(c))


def insert(req):
    #1.插入数据
    emp = Employee()
    emp.name = '张三'
    emp.save()
    #2.插入数据
    emp = Employee(name='李四')
    emp.save()
    #3.插入数据
    Employee.objects.create(name='王五')

    return HttpResponse("<h1>添加成功！</h1>")


def list_emps(req):
    print settings.BASE_DIR
    print settings.STATIC_ROOT
    print settings.STATICFILES_DIRS
    emps = Employee.objects.all()
    return render_to_response("list.html",{"emps":emps})


#多对一测试
def test_add(req):
    entry1 = Entry.objects.create(name="实体1")
    blog1 = Blog.objects.create(name="博客1", entry=entry1)
    blog2 = Blog.objects.create(name="博客2", entry=entry1)
    blog3 = Blog.objects.create(name="博客3", entry=entry1)

    print entry1.blog_set.all()
    return HttpResponse("<h1>创建成功！</h1>")


def test_add2(req):
    #查询实体
    entry2 = Entry(id=7)
    blog1 = Blog.objects.create(name="博客aaa", entry=entry2)
    blog2 = Blog.objects.create(name="博客bbb", entry=entry2)

    return HttpResponse("<h2>创建成功 2</h2>")


def test_add3(req):
    #查询实体
    entry1 = Entry.objects.get(name="实体1")
    blog1 = Blog.objects.create(name="博客mmm", entry=entry1)
    blog2 = Blog.objects.create(name="博客ppp", entry=entry1)

    return HttpResponse("<h2>创建成功 3</h2>")


def test_find(req):
     #blogs = Blog.objects.all().filter(entry_id=8)
    blogs = Blog.objects.filter(entry_id=8)
    print blogs
    t = Template('<h2>Hello template {{blogs}}</h2>')
    c = Context({'blogs': blogs})
    return  HttpResponse(t.render(c))