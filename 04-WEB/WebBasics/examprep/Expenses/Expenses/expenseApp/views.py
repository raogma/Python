from django.shortcuts import render

from Expenses.expenseApp.forms import ExpenseForm, ExpenseFormDelete
from Expenses.mainApp.models import Expense
from Expenses.utils import crud


def create_exp(req):
    return crud(req, ExpenseForm, None, 'homePath', 'expense-create.html')


def edit_exp(req, pk):
    return crud(req, ExpenseForm, Expense.objects.get(pk=pk), 'homePath', 'expense-edit.html')


def delete_exp(req, pk):
    return crud(req, ExpenseFormDelete, Expense.objects.get(pk=pk), 'homePath', 'expense-delete.html')

