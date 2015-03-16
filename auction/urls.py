from django.conf.urls import patterns, include, url
from django.contrib import admin
from weBay import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'auction.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.see_all, name='home'),
    url(r'^new/auction$', views.create_auction, name='create_auction'),
    url(r'^item/(?P<id>\d+)$', views.get_details, name='item_detail'),
    url(r'^item/(?P<id>\d+)/begin$', views.begin_auction, name='begin'),
    url(r'^item/(?P<id>\d+)/update$', views.update_auction, name='update'),
    url(r'^item/(?P<id>\d+)/end$', views.end_auction, name='end'),
    url(r'^admin/', include(admin.site.urls)),
)
