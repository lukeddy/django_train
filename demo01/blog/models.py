# -*- coding: utf-8 -*-
from django.db import models


class Employee(models.Model):
    #进入demo01的根目录执行：python manage.py syncdb
    name = models.CharField(max_length= 20)