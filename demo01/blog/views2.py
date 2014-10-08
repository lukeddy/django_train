# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.template import loader, Context, Template
from django.shortcuts import render_to_response
from blog.models import Author, Book
# Create your views here.


def test(req):
    t = Template('<h2>Hello template {{user}}</h2>')
    user = {"name": "wangwu", "age": 18}
    c = Context({'user': user})
    return HttpResponse(t.render(c))


def add(req):
    author1 = Author.objects.create(name="作者3")
    author2 = Author.objects.create(name="作者4")

    book = Book()
    book.name = "Thinging In Java"
    book.save()
    book.authors.add(author1)
    book.authors.add(author2)

    # book1 = Book.objects.create(name="Thinging In Java", author=author1)
   # book2 = Book.objects.create(name="30精通Python", authors=[author1, author2])
    # book3 = Book.objects.create(name="精通HTML", author=author2)
    # book4 = Book.objects.create(name="精通Nodejs", author=author2)

    return HttpResponse("<h3>添加成功</h3>")


def find(req):
    book = Book.objects.get(id=2)
    print book
    authors = book.authors.all()
    t = Template('<h2>book:{{book}}, authors: {{authors}}</h2>')
    c = Context({'book': book, 'authors': authors})
    return HttpResponse(t.render(c))


def update(req):
    book = Book.objects.get(id=1)
    book.name = "30精通Python"
    book.save()

    return HttpResponse("更新成功")


def delete(req):
    Book.objects.get(id=2).delete()
    return HttpResponse("删除成功")