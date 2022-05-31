from django.urls import path

from petstagram3.mainApp.views import HomeView, DashView

urlpatterns = [
    path('', HomeView.as_view(), name='homePath'),
    path('dashboard/', DashView.as_view(), name='dashPath'),
]
