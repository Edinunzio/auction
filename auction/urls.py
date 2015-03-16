from django.conf.urls import patterns, include, url
from django.contrib import admin
from weBay import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'auction.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index, name='home'),
    url(r'^item/create$', views.item_create, name='item_create'),
    url(r'^item/start$', views.begin_auction, name='item_begin'),
    url(r'^item/end$', views.end_auction, name='item_end'),
    url(r'^item/(?P<item_id>\d+)$', views.item_detail, name='item_detail'),
    url(r'^bid/create$', views.bid_create, name='bid_create'),
    url(r'^admin/', include(admin.site.urls)),
)
