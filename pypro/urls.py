"""pypro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('contas/login/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='login'),
    path('contas/logout/', auth_views.LoginView.as_view(redirect_authenticated_user=True), name='logout'),
    path('contas/password_reset/', auth_views.LoginView.as_view(redirect_authenticated_user=True),
         name='password_reset'),
    path('', include('social_django.urls', namespace='social')),
    path('', include('pypro.base.urls')),
    path('aperitivos/', include('pypro.aperitivos.urls')),
    path('modulos/', include('pypro.modulos.urls')),
    path('turmas/', include('pypro.turmas.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns.append(
        path('__debug__/', include(debug_toolbar.urls))
    )
