from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # The health check path for Render
    # Make sure your views.py file has a 'health_check' function!
    path('status/', views.health_check, name='health_check'),

    path('', views.index, name='index'),
    path('robots.txt', views.robots, name='robots'),
    path('sitemap.xml', views.sitemap, name='sitemap'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
