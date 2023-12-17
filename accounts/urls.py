from rest_framework.authtoken import views
from django.urls import path
from .views import CreateAccountView, ManageAccountView

urlpatterns = [
    path('token/', views.obtain_auth_token),
    path('create/', CreateAccountView.as_view()),
    path('manage/', ManageAccountView.as_view()),
]
