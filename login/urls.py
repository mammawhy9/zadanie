from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^home/$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^$', RedirectView.as_view(url=reverse_lazy('login'), permanent=False)),
    url(r'^accounts/login/$', auth_views.login, {'template_name': 'login.html'}, name='login', ),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    url(r'^list/', include('users.urls')),
    url(r'^admin/', admin.site.urls),
]
