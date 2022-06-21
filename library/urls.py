from .authorization import *
from .views import *
from django.urls import path

urlpatterns = [
    #authentication
    path('signup/', signUp.as_view(), name="signup"),
    path('signin/', signIn.as_view(), name="signin"),
    path('signout/', signOut.as_view(), name="signout"),
    path('pwdch/', changePassword.as_view(), name="changePassword"),

    #views
    path('' , homepage.as_view(), name="homepage"),
    path('add/', addBook, name="add")
]