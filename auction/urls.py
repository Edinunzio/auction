from django.conf.urls import patterns, include, url
from django.contrib import admin
from weBay import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'auction.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='home'),
    url(r'^item/(?P<item_id>\d+)$', views.item_detail, name='item_detail'),
    url(r'^admin/', include(admin.site.urls)),
)
