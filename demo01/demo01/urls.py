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
)
