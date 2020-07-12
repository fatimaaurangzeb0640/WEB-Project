from django.urls import path
from . import views
from user.models import Seller
urlpatterns = [
    path("", views.index, name="seller_index"), 
    path("register", views.register_seller, name="register_seller"),
    path("login", views.login_seller, name="login_seller"),
    path("logout", views.logout_seller, name = "logout_seller"),
    path("<str:seller_name>", views.seller, name="seller"),
    path("<str:seller_name>/getitems", views.getitems, name="getitems"),
    path("<str:seller_name>/getlist", views.getlist, name="getlist")
]