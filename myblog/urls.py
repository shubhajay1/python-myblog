"""
URL configuration for myblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home,  )
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myblog import views

urlpatterns = [
    path('admin-panel/', admin.site.urls),
    path('', views.homePage, name="home"),
    path('left-sidebar/', views.leftSidebar, name="leftSidebar"),
    path('right-sidebar.html', views.rightSidebar, name="rightSidebar"),
    path('no-sidebar/', views.noSidebar, name="noSidebar"),
    path('about-us/', views.aboutUs, name="aboutUs"),
    path('contact-us/', views.contactUs, name="contactUs"),
    path('UserForm/', views.UserForm, name="userform"),
    path('userpostform/', views.userpostform, name="userpostform"),
    path('userformmodel/', views.userformmodel, name="userformmodel"),
    path('submitForm/', views.submitForm, name='submitForm'),
    path('calculater/', views.calculater, name='calculater'),
    path('emicalculater/', views.emicalculater, name='emicalculater'),
    path('SubmitEmi/', views.SubmitEmi, name='SubmitEmi'),
    path('course/', views.course),
    path('course/<courseId>', views.courseDetails)
]
