"""paper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from basic_app import views
from django.contrib.auth import views as lview
from django.urls import reverse_lazy
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include('basic_app.urls')),


    url(r'^accounts/login/$', lview.LoginView.as_view(), name='login'),    #directly let u go to login.html file
    url(r'^accounts/logout/$', lview.LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),
    url(r'^password-reset/$',lview.PasswordResetView.as_view(template_name='registration/password_reset.html',success_url=reverse_lazy('password_reset_done')),name='password_reset'),

    url(r'^password-reset/done/$',lview.PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'),
    url(r'^password-reset-confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',lview.PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),name='password_reset_confirm'),
    url(r'^password-reset-complete/$',lview.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name='password_reset_complete'),


]
