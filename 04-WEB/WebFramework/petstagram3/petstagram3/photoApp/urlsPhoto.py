from django.urls import path

from petstagram3.photoApp.views import CreatePhoto, EditPhoto, PhotoDetails

urlpatterns = [
    path('create/', CreatePhoto.as_view(), name='createPhotoPath'),
    path('edit/<int:pk>/',  EditPhoto.as_view(), name='editPhotoPath'),
    path('details/<int:pk>/', PhotoDetails.as_view(), name='detailsPhotoPath'),
]
