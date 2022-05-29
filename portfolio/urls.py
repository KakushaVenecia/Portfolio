from django.urls import include,re_path as url
from . import views

urlpatterns=[
    url('^$',views.index, name = 'index'),
    url('^project/$', views.myportfolio, name='myportfolio'),
    url('^project/(\d+)/', views.myportfolio_details, name='myportfolio_details'),
    url('^contact/$', views.display_contact, name ='display')
]