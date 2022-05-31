from django.urls import path

from MusicApp.albumApp.views import album_details_view, album_add_view, album_edit_view, album_delete_view

urlpatterns = [
    path('details/<int:pk>', album_details_view, name='show details album'),
    path('add/', album_add_view, name='show add album'),
    path('edit/<int:pk>', album_edit_view, name='show edit album'),
    path('delete/<int:pk>', album_delete_view, name='show delete album'),
]
