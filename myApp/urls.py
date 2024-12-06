from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings
from myApp.views import login
from django.urls import path

urlpatterns = [
    # HOME PAGE URL
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),

    path('dashboard/', views.dashboard, name='admin_dashboard'),

    path('userdashboard/', views.user_dashboard, name='user_dashboard'),

    path('sellerdashboard/', views.seller_dashboard, name='seller_dashboard'),
    path('seller/uploadproducts/', views.upload_product, name='seller.uploadproducts'),


    path('logout/', views.logout, name='logout'),

    # USERS URLS
    path('users/', views.users, name='users'),
    path('adduser/', views.add_user, name='add_user'),
    path('updateuser/', views.update_user, name='update_user'),
    path('deletuser/', views.delete_user, name='delete_user'),

    # PRODUCTS URLS
    path('products/', views.products, name='products'),
    path('addproduct/', views.add_product, name='add_product'),
    path('updateproduct/', views.update_product, name='update_product'),
    path('deleteproduct/', views.delete_product, name='delete_product'),

    # SERVICES URLS
    path('services/', views.services, name='services'),
    path('addservice/', views.add_service, name='add_service'),
    path('updateservice/', views.update_service, name='update_service'),
    path('deleteservice/', views.delete_service, name='delete_service'),

    # CATEGORIES URLS
    path('categories/', views.categories, name='categories'),
    path('addcategory/', views.add_category, name='add_category'),
    path('updatecategory/', views.update_category, name='update_category'),
    path('deletecategory/', views.delete_category, name='delete_category'),

    # CART SERVICES
    path('addtocart/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_items, name='cart'),
    path('deletefromcart/', views.delete_from_cart, name='delete_from_cart'),

    # path(r'^static/(?P<path>.*)$', server, {'document_root': settings.STATIC_ROOT})

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  #for image upload purposes