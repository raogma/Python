from django.urls import path

from petstagram3.accountsApp.views import CreateProfileView, UserLogin, ProfileDetailsView, EditProfileView, \
    DeleteProfileView

urlpatterns = [
    path('create-profile/', CreateProfileView.as_view(), name='register'),
    path('login/', UserLogin.as_view(), name='login'),
    path('profile/<int:pk>/', ProfileDetailsView.as_view(), name='profileDetails'),
    path('edit-profile/<int:pk>/', EditProfileView.as_view(), name='profileEdit'),
    path('delete-profile/<int:pk>/', DeleteProfileView.as_view(), name='profileDelete'),
    # path('edit-password/<int:pk>/', LoginView.as_view(), name='passwordEdit'),
]
