from django.conf.urls import patterns, include, url
from django.contrib import admin
from exampleapp import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'example.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.homepage, name='homepage'),
    url(r'^population/(?P<stateslug>[\w-]+)/$', views.statedetail),
    url(r'^population/(?P<stateslug>[\w-]+)/(?P<countyslug>[\w-]+)/$', views.countydetail),
    url(r'^admin/', include(admin.site.urls)),
)
