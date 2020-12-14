# Python
# Django
from django.urls import path, include
from django.contrib.auth import views as auth_views
# Project
from .pedidos.views import PedidosHome
from .clientes import urls

urlpatterns = [
    path('home/', PedidosHome.as_view(), name='pedidos__home'),
    path('clientes/', include('apps.clientes.urls')),
    # Auth
    path('login/', auth_views.LoginView.as_view(), {
        'template_name': 'registration/login.html',
        'redirect_authenticated_user': True,
    }, name='login'),
    path('logout/', auth_views.logout_then_login, name='logout'),

    # Troca Senha
    path('trocarsenha/', auth_views.PasswordChangeView.as_view(
        template_name='auth/password_change.html',
    ), name='password_change'),
    path('trocarsenha/sucesso', auth_views.PasswordChangeDoneView.as_view(
        template_name='auth/password_change_done.html'
    ), name='password_change_done'),

    # Reset Senha
    path('esqueciminhasenha/', auth_views.PasswordResetView.as_view(
        template_name='auth/password_reset_form.html',
    ), name='password_reset'),

    path('esqueciminhasenha/emailenviado/', auth_views.PasswordChangeDoneView.as_view(
        template_name='auth/password_reset_done.html'
    ), name='password_reset_done'),   
 
    path('esqueciminhasenha/novasenha/(<uidb64>[0-9A-Za-z_\-]+)/(<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', auth_views.PasswordResetConfirmView.as_view(
        template_name='auth/password_reset_confirm.html',
    ), name='password_reset_confirm'),

    path('esqueciminhasenha/feito/', auth_views.PasswordResetCompleteView.as_view(
        template_name='auth/password_reset_complete.html'
    ), name='password_reset_complete'), 
]

