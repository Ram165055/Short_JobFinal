from django.urls import path

from . import views
from pagelink.views import frontpage,post_detail

urlpatterns=[
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('register', views.register,name='register'),
    path('dash',views.dash,name='dash'),
    path('post',views.post,name='post'),
    path('about',views.about,name='about'),
    # path('blog',views.blog,name='blog'),
    path('searchresult',views.searchresult,name='searchresult'),
    path('search',views.search,name='search'),
    path('joblist',views.joblist,name='joblist'),
    path('profile',views.profile,name='profile'),
    path('my_func',views.my_func,name='my_func'),

    path('export/csv-database-write/', views.csv_database_write, name='csv_database_write'),
    path('predict',views.predict,name='predict'),
    path('predict_result',views.predict_result,name='predict_result'),
    path('show',views.show,name='show'),
    path('frontpage', frontpage, name='frontpage'),
    path('<slug:slug>/', post_detail, name='post_detail')
    

]
