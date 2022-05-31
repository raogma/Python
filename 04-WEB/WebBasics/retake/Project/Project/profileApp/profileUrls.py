from django.urls import path

from Project.profileApp.views import ProfileDetailsPage, ProfileCreatePage, ProfileEditPage, ProfileDeletePage

urlpatterns = [
    path('details/<int:pk>', ProfileDetailsPage.as_view(), name='profile-details'),
    path('create', ProfileCreatePage.as_view(), name='profile-create'),
    path('edit/<int:pk>', ProfileEditPage.as_view(), name='profile-edit'),
    path('delete/<int:pk>', ProfileDeletePage.as_view(), name='profile-delete'),
]
