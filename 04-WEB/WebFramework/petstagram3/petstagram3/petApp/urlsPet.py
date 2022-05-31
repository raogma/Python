from django.urls import path

from petstagram3.petApp.views import like_fn, CreatePet, EditPet, DeletePet

urlpatterns = [
    path('like/<id>', like_fn, name='likePath'),
    path('create/', CreatePet.as_view(), name='petCreatePath'),
    path('edit/<int:pk>/', EditPet.as_view(), name='petEditPath'),
    path('delete/<int:pk>/', DeletePet.as_view(), name='petDeletePath')
]
