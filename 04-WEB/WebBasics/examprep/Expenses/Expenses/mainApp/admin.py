from django.contrib import admin

from Expenses.mainApp.models import Profile, Expense


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):...


@admin.register(Expense)
class ExpensesAdmin(admin.ModelAdmin):...
