from .views import ListUserView, CreateUserView, UpdateUserView, DeleteUserView, \
    ListCompanyView, CreateCompanyView, UpdateCompanyView, DeleteCompanyView

from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', login_required(ListUserView.as_view()), name='users-list',),
    url(r'^new$', login_required(CreateUserView.as_view()), name='users-new', ),
    url(r'^edit/(?P<pk>\d+)/$', login_required(UpdateUserView.as_view()), name='users-edit', ),
    url(r'^delete/(?P<pk>\d+)/$', login_required(DeleteUserView.as_view()), name='users-delete', ),

    url(r'^company/$', login_required(ListCompanyView.as_view()), name='company-list', ),
    url(r'^company/new$', login_required(CreateCompanyView.as_view()), name='company-new', ),
    url(r'^company/edit/(?P<pk>\d+)/$', login_required(UpdateCompanyView.as_view()), name='company-edit', ),
    url(r'^company/delete/(?P<pk>\d+)/$', login_required(DeleteCompanyView.as_view()), name='company-delete', ),

]

urlpatterns += staticfiles_urlpatterns()