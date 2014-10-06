from django.http import HttpResponse
from django.template import loader, Context
from django.shortcuts import render_to_response
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