
from django.conf.urls import url

from products.views import (
	ProductListView, 
	product_list_view, 
	ProductDetailView, 
	ProductDetailSlugView, 
	product_detail_view,
	ProductFeaturedDetailView, 
	ProductFeaturedListView
	)

urlpatterns = [
    
    #url('^featured/$',ProductFeaturedListView.as_view()),
    #url('^featured/(?P<pk>\d+)/$',ProductFeaturedDetailView.as_view()),
    url('^$',ProductListView.as_view()),
    #url('^products-fbv/$',product_list_view),
    url('^(?P<pk>\d+)/$',ProductDetailView.as_view()),
    url('^(?P<slug>[\w-]+)/$',ProductDetailSlugView.as_view()),
    #url('^products-fbv/(?P<pk>\d+)/$',product_detail_view),
    #url('^contact/$',contactpage),
]
