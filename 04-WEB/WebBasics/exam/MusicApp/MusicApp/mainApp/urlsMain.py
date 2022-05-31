from django.urls import path

from MusicApp.mainApp.views import home_view

urlpatterns = [
    path('', home_view, name='show home'),
]
