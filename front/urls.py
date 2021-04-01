from django.urls import path, include
from  .import views
from django.conf.urls import url
from django.contrib import admin

urlpatterns=[

    path("",views.index,name="home"),
    path('accounts/',include('accounts.urls')),
    path("profile.html",views.profile,name="profile.html"),
    path("info.html",views.upload_fetch,name="info.html"),
    path("upload.html", views.upload, name="upload"),
    path('redcd/',views.barchart1),
    path('getfile1/', views.getfile1),
    path('redcross/',views.barchart2),
    path('getfile2/', views.getfile2),
    path('hackersclub/',views.barchart3),
    path('getfile3/', views.getfile3),
    path('cust/',views.barchart4),
    path('getfile4/', views.getfile4),
    path('test.html',views.new),


    path('upload/',views.upload),
    
    url(r'^search/$',views.search),
]
