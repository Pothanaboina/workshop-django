"""ExampleProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from VVITApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('g/',views.demo),
    path('k/<str:n>/',views.greet),
    path('gh/<str:n>/<int:b>',views.stdnt),
    path('l/',views.ky),
    path('n/',views.my),
    path('p/<str:en>/<int:es>/',views.emp),
    path('y/<str:self>/',views.ry),
    path('h/<str:m>/',views.hello),
    path('t/<str:sname>/<str:srollno>/<str:sage>/<str:sbranch>/', views.student),
    path('d/',views.my_fun),
    path('f/<str:a>/',views.ml),
    path('j/<str:ename>/<str:esal>/',views.fun),
    path('r/<str:e>/',views.good),
    path('m/',views.stdform),
    path('',include('BSApp.urls')),
]
