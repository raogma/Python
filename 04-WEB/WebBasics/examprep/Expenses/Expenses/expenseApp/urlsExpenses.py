from django.urls import path

from Expenses.expenseApp.views import create_exp, edit_exp, delete_exp

urlpatterns = [
    path('create/', create_exp, name='createExp'),
    path('edit/<int:pk>', edit_exp, name='editExp'),
    path('delete/<int:pk>', delete_exp, name='deleteExp'),
]
