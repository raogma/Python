from django.urls import path

from Expenses.profileApp.views import profile_details, edit_profile, delete_profile, create_profile

urlpatterns = [
    path('', profile_details, name='profileDetails'),
    path('create/', create_profile, name='profileCreate'),
    path('edit/', edit_profile, name='profileEdit'),
    path('delete/', delete_profile, name='profileDelete'),
]
