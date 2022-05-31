from django.urls import path

from MusicApp.profileApp.views import profile_details_view, profile_create_view, profile_delete_view

urlpatterns = [
    path('details/', profile_details_view, name='show profile details'),
    path('create/', profile_create_view, name='show create profile'),
    # path('edit/', profile_edit_view, name='show edit profile'),
    path('delete/', profile_delete_view, name='show delete profile'),
]
