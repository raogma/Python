from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Project.mainApp.mainUrls')),
    path('profile/', include('Project.profileApp.profileUrls')),
    path('game/', include('Project.gameApp.gameUrls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
