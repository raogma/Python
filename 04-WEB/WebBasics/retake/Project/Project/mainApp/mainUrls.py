from django.urls import path

from Project.mainApp.views import HomePage, DashPage

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('dashboard/', DashPage.as_view(), name='dashboard')
]
