"""
    Module name :- views
"""

from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from accounts.forms import SignUpForm, LoginForm, UpdateUserForm

# Create your views here.

# @method_decorator(login_required(login_url= 'accounts:login'), name='dispatch')
class CreateUser(CreateView):
    """
        Create user.
    """
    template_name = 'accounts/user.html'
    form_class = SignUpForm
    success_url = reverse_lazy('store:index')
    permission_required = ['is_superuser']

    def form_invalid(self, form):
        """
            Invalid form.
        """
        messages.info(self.request, form.errors)
        return super().form_invalid(form)


class UpdateUser(UpdateView):
    """
        Update user.
    """
    model = User
    form_class = UpdateUserForm
    template_name = 'accounts/user.html'
    context_object_name = 'user'
    success_url = reverse_lazy('store:index')

    def get(self, request, *args, **kwargs):
        """
            Get method.
        """
        try:
            self.get_object()
        except:
            messages.info(request, 'User doest not exists.')
            return redirect('accounts:login')

        return super().get(request, *args, **kwargs)

    def form_invalid(self, form):
        """
            Invalid form.
        """
        messages.info(self.request, form.errors)
        return super().form_invalid(form)

    def has_permission(self) -> bool:
        """
            Method to check permissions.
        """
        return self.request.user.is_superuser or (self.get_object() == self.request.user)


class DeleteUser(PermissionRequiredMixin, DeleteView):
    """
        Delete user.
    """
    model = User
    template_name = ''
    success_url = ''
    context_object_name = 'user'

    def get(self, request, *args, **kwargs):
        """
            Get method.
        """
        try:
            self.get_object()
        except:
            messages.info(request, 'User doest not exists.')
            return redirect('accounts:login')

        return super().get(request, *args, **kwargs)

    def has_permission(self) -> bool:
        """
            Method to check permissions.
        """
        return self.request.user.is_superuser or (self.get_object() == self.request.user)
    

class ListUser(ListView):
    """
        List all users.
    """
    model = User
    template_name = ''
    context_object_name = 'users'
    paginate_by = 8


class UserLoginView(LoginView):
    """
        Login View.
    """
    template_name = 'accounts/user.html'
    form_class = LoginForm
    success_url = reverse_lazy('store:index')
