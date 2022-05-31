from django.contrib import admin

from Project.gameApp.models import Game


@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    pass
