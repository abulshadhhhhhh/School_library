"""
URL configuration for school_library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from app1 import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('register', views.register),
    path('login', views.login),
    path('logout', views.logout,name='logout'),
    path('bookstore', views.bookstore),
    path('changepassword', views.changepassword),
    path('changepasswordsuccess', views.changepasswordsuccess),
    path('passview', views.passview),
    path('affairview/<int:id>', views.affairview,name='affairview'),
    path('addbook', views.addbook, name='addbook'),
    path('editprofile', views.editprofile),
    path('editprofileview', views.editprofileview),
    path('editprofilesuccess', views.editprofilesuccess),
    path('librarian', views.librarian,name='librarian'),
    path('delete/<int:id>', views.deletebook, name='deletebook'),
    path('editbook/<int:id>', views.editbook, name='editbook'),
    path('history',views.history),
    path('userhistory',views.userhistory),
    path('issuebooksuccess',views.userhistory),
    path('getbook',views.getbook,name="getbook"),
    path('search',views.search,name="search"),
    path('return/<int:id>',views.returnbook,name="return")

    ]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)