"""animals URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as django_views
from django.urls import path, include
from info import views


from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('family/<int:X>', views.family, name='family'),
    path('animal/<int:id>', views.animal, name='animal_d'),
    # path('add_animal/', views.add_animal, name='add'),
    path('add_animal/', views.AddAnimals.as_view(), name='add'),
    path('show_animals/', views.AnimalIndex.as_view()),
    path('', views.home, name='home'),
    path('buy_animal/<int:id>', views.buy, name='buy'),
    path('panier', views.show_panier, name='panier'),
    path('forum/', include('forum.urls')),
    path('', include('accounts.urls')),
    path('login/', django_views.LoginView.as_view(), name='login'),
    path('logout/', django_views.LogoutView.as_view(), name='logout'),

]
# path('accounts/', include('django.contrib.auth.urls')),
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                            document_root=settings.MEDIA_ROOT)
