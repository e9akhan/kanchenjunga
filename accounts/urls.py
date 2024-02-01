"""
    Module name :- urls
"""

from django.urls import path, reverse_lazy
from django.contrib.auth.views import LogoutView
from accounts.views import CreateUser, UserLoginView, UpdateUser


app_name = 'accounts'

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page = reverse_lazy('accounts:login')), name='logout'),

    path('add-user/', CreateUser.as_view(), name='sign-up'),
    path('update-user/<int:pk>/', UpdateUser.as_view(), name='update-user')
]