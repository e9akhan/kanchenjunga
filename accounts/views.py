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
from django.db.models import Q
from accounts.forms import SignUpForm, LoginForm, UpdateUserForm

# Create your views here.


@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class CreateUser(PermissionRequiredMixin, CreateView):
    """
    Create user.
    """

    template_name = "accounts/user.html"
    form_class = SignUpForm
    success_url = reverse_lazy("accounts:users")
    permission_required = ["is_superuser"]

    def form_invalid(self, form):
        """
        Invalid form.
        """
        messages.info(self.request, form.errors)
        return super().form_invalid(form)


@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class UpdateUser(PermissionRequiredMixin, UpdateView):
    """
    Update user.
    """

    model = User
    form_class = UpdateUserForm
    template_name = "accounts/user.html"
    context_object_name = "user"
    success_url = reverse_lazy("accounts:users")

    def get(self, request, *args, **kwargs):
        """
        Get method.
        """
        try:
            self.get_object()
        except:
            messages.info(request, "User doest not exists.")
            return redirect("accounts:login")

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
        return self.request.user.is_superuser or (
            self.get_object() == self.request.user
        )


@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class DeleteUser(PermissionRequiredMixin, DeleteView):
    """
    Delete user.
    """

    model = User
    template_name = "accounts/delete.html"
    success_url = reverse_lazy("accounts:users")
    context_object_name = "user"

    def get(self, request, *args, **kwargs):
        """
        Get method.
        """
        try:
            self.get_object()
        except:
            messages.info(request, "User doest not exists.")
            return redirect("accounts:users")

        return super().get(request, *args, **kwargs)

    def has_permission(self) -> bool:
        """
        Method to check permissions.
        """
        return self.request.user.is_superuser or (
            self.get_object() == self.request.user
        )

    def get_context_data(self, **kwargs):
        """
        Overriding get context data method.
        """
        context = super().get_context_data(**kwargs)
        context["title"] = "Delete User"
        return context


@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class ListUser(ListView):
    """
    List all users.
    """

    model = User
    template_name = "accounts/list_user.html"
    context_object_name = "users"
    paginate_by = 10


class UserLoginView(LoginView):
    """
    Login View.
    """

    template_name = "accounts/login.html"
    form_class = LoginForm
    next_page = reverse_lazy("store:equipment-types")


@method_decorator(login_required(login_url="accounts:login"), name="dispatch")
class SearchUser(ListView):
    """
    Search User.
    """

    model = User
    template_name = "accounts/list_user.html"
    paginate_by = 8
    context_object_name = "users"

    def get_queryset(self):
        """
        Overriding get queryset.
        """
        search = self.request.GET["search"]
        return self.model.filter(
            Q(username__icontains=search)
            | Q(first_name__icontains=search)
            | Q(last_name__icontains=search)
        )
