from django.urls import path
from . import views
from user.models import Seller
urlpatterns = [
    path("", views.index, name="seller_index"), 
    path("register", views.register_seller, name="register_seller"),
    path("login", views.login_seller, name="login_seller"),
    path("logout", views.logout_seller, name = "logout_seller"),
    path("<str:seller_name>", views.seller, name="seller"),
    path("<str:seller_name>/getlist", views.getlist, name="getlist"),
    path("<str:seller_name>/get<str:dish_name>", views.getitem, name="getitem"),
    #path("<str:seller_name>/<str:item>", views.item, name="item" ),
    path("<str:seller_name>/additem", views.additem, name="additem"),
]