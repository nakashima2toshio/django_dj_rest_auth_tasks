# django_dj_rest_auth_tasks/settings.py
# from allauth.account.views import ConfirmEmailView
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

# from accounts.views import CustomConfirmEmailView  # カスタムビューをインポート

urlpatterns = [
    path('admin/', admin.site.urls),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
    path('/dj-rest-auth/registration/account-confirm-email/', include('allauth.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    # path('dj-rest-auth/registration/account-confirm-email/<str:key>/', ConfirmEmailView.as_view(), name='account_confirm_email'),  # カスタムビューを使用
]
