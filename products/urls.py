from django.conf.urls import url
from . import views as product_views


urlpatterns=[
    url(r'^$',product_views.create_product,name='create_product'),
    url(r'^show_products/$',product_views.show_products,name='show_products'),
# http://127.0.0.1:8000/products/show_products/2
    url(r'^show_products/(?P<prod_id>\d+)/$',product_views.product_details,name='product_details')
]
#url(r'^(?P<rest_id>\d+)/$'