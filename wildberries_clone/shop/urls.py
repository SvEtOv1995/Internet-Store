# shop/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Главная страница с товарами и категориями
    path('', views.product_list, name='product_list'),

    # Страница категории с товарами
    path('category/<slug:slug>/', views.category_products, name='category_products'),

    # Страница подробного описания товара
    path('product/<slug:slug>/', views.product_detail, name='product_detail'),

    # Страница корзины
    path('cart/', views.cart, name='cart'),

    # Страница избранного
    path('favorites/', views.favorites, name='favorites'),

    # Страница профиля пользователя
    path('profile/', views.profile, name='profile'),
]
