from django.urls import path

from Project.gameApp.views import GameDetailsPage, GameCreatePage, GameEditPage, GameDeletePage

urlpatterns = [
    path('details/<int:pk>', GameDetailsPage.as_view(), name='game-details'),
    path('create/', GameCreatePage.as_view(), name='game-create'),
    path('edit/<int:pk>', GameEditPage.as_view(), name='game-edit'),
    path('delete/<int:pk>', GameDeletePage.as_view(), name='game-delete'),
]
