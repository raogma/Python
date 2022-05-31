from django.urls import path

from Expenses.mainApp.views import home

urlpatterns = [
    path('', home, name='homePath'),

]
