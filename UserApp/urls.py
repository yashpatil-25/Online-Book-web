from django.urls import path
from UserApp import views

urlpatterns = [
    path('',views.homepage),
    path('ViewBooks/<cid>',views.ViewBooks),
    path('ViewDetails/<book_id>',views.ViewDetails),
    path("login",views.login),
    path("signup", views.signup),
    path("logout",views.logout),
    path("cart",views.showcart),
    
]