from rest_framework.authtoken import views
from django.urls import path
from .views import CreateAccountView, ManageAccountView, LogInView, LogOutView

urlpatterns = [
    path('create/', CreateAccountView.as_view()),
    path('manage/', ManageAccountView.as_view()),
    path('login/', LogInView.as_view()),
    path('logout/', LogOutView.as_view()),
]
