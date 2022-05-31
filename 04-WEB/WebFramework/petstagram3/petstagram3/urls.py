from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('petstagram3.mainApp.urlsMain')),
    path('pet/', include('petstagram3.petApp.urlsPet')),
    path('photo/', include('petstagram3.photoApp.urlsPhoto')),
    path('accounts/', include('petstagram3.accountsApp.urlsAccounts')),
    path('profile/', include('petstagram3.profileApp.urlsProfile')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
