# -*- coding: utf-8 -*-
from django.db import models


class Employee(models.Model):
    #进入demo01的根目录执行：python manage.py syncdb
    name = models.CharField(max_length=20)


#多对一关系
class Entry(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


class Blog(models.Model):
    name = models.CharField(max_length=30)
    entry = models.ForeignKey(Entry)

    def __unicode__(self):
        return self.name


#多对多
class Author(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=30)
    authors = models.ManyToManyField(Author)

    def __unicode__(self):
        return self.name