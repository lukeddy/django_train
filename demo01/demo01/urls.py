from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demo01.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/index/$', 'blog.views.index'),
    url(r'^blog/category/$', 'blog.views.category'),
    url(r'^blog/detail/$', 'blog.views.detail'),
    url(r'^blog/detail3/$', 'blog.views.detail3'),
    #CRUD
    url(r'^blog/insert/$', 'blog.views.insert'),
    url(r'^blog/list/$', 'blog.views.list_emps'),

    #many2one
    url(r'^blog/many2one_add/$', 'blog.views.test_add'),
    url(r'^blog/many2one_add2/$', 'blog.views.test_add2'),
    url(r'^blog/many2one_add3/$', 'blog.views.test_add3'),
    url(r'^blog/many2one_find/$', 'blog.views.test_find'),

    #many2many
    url(r'^blog/many2many_test/$', 'blog.views2.test'),
    url(r'^blog/many2many_add/$', 'blog.views2.add'),
    url(r'^blog/many2many_find/$', 'blog.views2.find'),
    url(r'^blog/many2many_update/$', 'blog.views2.update'),
    url(r'^blog/many2many_del/$', 'blog.views2.delete'),
)
