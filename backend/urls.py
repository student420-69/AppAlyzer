from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from appalyzerUSERS import views as user_views
from appalyzer import views as app_views

# Configuración de urls y sus funciones
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('login/', auth_views.LoginView.as_view(template_name='appalyzerUSERS/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='appalyzerUSERS/logout.html'), name='logout'),
    path('password-reset/', auth_views.PasswordResetView.as_view(template_name='appalyzerUSERS/password_reset.html'), name='password_reset'),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(template_name='appalyzerUSERS/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='appalyzerUSERS/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name='appalyzerUSERS/password_reset_complete.html'), name='password_reset_complete'),
    path('', include('appalyzer.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

