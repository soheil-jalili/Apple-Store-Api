from django.urls import path

from account import views

app_name = 'account'
urlpatterns = [
    path('signup', views.SignUpView.as_view(), name='sign_up'),
    path('signin', views.SignInView.as_view(), name='sign_in'),
    path('signout', views.SignOutView.as_view(), name='sign_out'),
]
