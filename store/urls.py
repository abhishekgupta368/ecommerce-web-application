from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:category_slug>', views.home, name='products_by_category'),
    path('category/<slug:category_slug>/<slug:product_slug>',
         views.productPage, name='product_detail'),
    path('cart/add/<int:product_id>', views.add_cart, name='add_cart'),
    path('cart', views.cart_detail, name='cart_detail'),
    path('cart/remove/<int:product_id>', views.cart_remove, name='cart_remove'),
    path('cart/remove_product/<int:product_id>', views.cart_remove_product, name='cart_remove_product'),
    path('thankyou/<int:order_id>', views.thanks_page, name='thanks_page'),
    path('account/create/', views.signupView, name='signup'),
    path('account/signin/', views.signinView, name='signin'),
    path('account/signout/', views.signoutView, name='signout'),
    path('order_history/', views.orderHistory, name='order_history'),
    path('order/<int:order_id>', views.viewOrder, name='order_detail'),
    path('search/', views.search, name='search'),
    path('contact/', views.contact, name='contact')
]
