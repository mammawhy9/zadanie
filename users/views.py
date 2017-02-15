from django.shortcuts import render
from django.core.urlresolvers import reverse
from .forms import *
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.exceptions import PermissionDenied

from .models import User, Company


class CreateUserView(CreateView):
    from django.contrib.auth.models import User
    model = User
    template_name = 'edit_user.html'
    form_class = UserForm

    def get_success_url(self):
        return reverse('users-list')

    def get_context_data(self, **kwargs):

        context = super(CreateUserView, self).get_context_data(**kwargs)
        context['action'] = reverse('users-new')

        return context


class UpdateUserView(UpdateView):

    model = User
    template_name = 'edit_user.html'
    form_class = UserForm

    def get_success_url(self):
        return reverse('users-list')

    def get_context_data(self, **kwargs):
        context = super(UpdateUserView, self).get_context_data(**kwargs)
        context['action'] = reverse('users-edit',
                                    kwargs={'pk': self.get_object().id})

        return context


class DeleteUserView(DeleteView):
    from django.contrib.auth.models import User
    model = User
    template_name = 'delete_user.html'

    def get_success_url(self):
        return reverse('users-list')


class LoggedInMixin(object):

    def dispatch(self, *args, **kwargs):
        return super(LoggedInMixin, self).dispatch(*args, **kwargs)


class ListUserView(LoggedInMixin, ListView):

    model = User
    template_name = 'user_list.html'

    def get_queryset(self):
        from django.contrib.auth.models import User
        return User.objects.all()


class CreateCompanyView(CreateView):
    model = Company
    template_name = 'edit_company.html'
    form_class = CompanyForm

    def get_success_url(self):
        return reverse('company-list')

    def get_context_data(self, **kwargs):
        context = super(CreateCompanyView, self).get_context_data(**kwargs)
        context['action'] = reverse('company-new')
        return context


class UpdateCompanyView(UpdateView):

    model = User
    template_name = 'edit_company.html'
    form_class = CompanyForm

    def get_success_url(self):
        return reverse('company-list')

    def get_context_data(self, **kwargs):
        context = super(UpdateCompanyView, self).get_context_data(**kwargs)
        context['action'] = reverse('company-edit', kwargs={'pk': self.get_object().id})

        return context


class DeleteCompanyView(DeleteView):

    model = Company
    template_name = 'delete_company.html'

    def get_success_url(self):
        return reverse('company-list')


class ListCompanyView(LoggedInMixin, ListView):

    model = Company
    template_name = 'company_list.html'

    def get_queryset(self):

        return Company.objects.all()

