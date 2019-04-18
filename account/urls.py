from django.conf.urls import url
from . import views as account_views

urlpatterns=[
    url(r'^signup/',account_views.account_signup,name='signup'),
    url(r'^$',account_views.account_login,name='login'),
    url(r'^logout/',account_views.account_logout,name='logout'),
]