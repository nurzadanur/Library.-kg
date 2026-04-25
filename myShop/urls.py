from django.urls import path
from .views import (
    ShopHomeView,
    CategoriesView,
    ProductsView,
    CategoryProductsView,
    RegisterView,
    LoginView
)

urlpatterns = [
    path('', ShopHomeView.as_view(), name='shop_home'),  # /shop/
    path('categories/', CategoriesView.as_view(), name='categories'),
    path('products/', ProductsView.as_view(), name='products'),
    path('categories/<int:id>/', CategoryProductsView.as_view(), name='category_products'),

    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]