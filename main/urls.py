"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include


from myShop.views import (
    CategoriesView,
    ProductsView,
    CategoryProductsView,
    ShopHomeView,
    RegisterView,
    LoginView
)

from horse_tour.views import LocationListView
from main.views import home


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', home, name='home'),

    path('blog/', include('blog.urls')),

    path('shop/', include('myShop.urls')), 
    

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),

    path('tour/', LocationListView.as_view()),

    path('questionnaire/', include('questionnaire.urls')),

    path('captcha/', include('captcha.urls')),

    path('movies/', include('CineBoard.urls')),

    path('accounts/', include('django.contrib.auth.urls')),
]