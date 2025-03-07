# admin.py
from django.contrib import admin
from .models import Game, Player

# Customize Game admin
class GameAdmin(admin.ModelAdmin):
    list_display = ('GameID', 'GameName', 'Status', 'Maxplayers', 'StartCash', 'Smallblind', 'Raiseblind', 'Timeout', 'delay')
    list_filter = ('Status',)
    search_fields = ('GameName',)

# Customize Player admin
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('user','cash')
    search_fields = ('user__username', 'game__GameName')
    list_filter = ('game',)

# Register models with custom admin
admin.site.register(Game, GameAdmin)
admin.site.register(Player, PlayerAdmin)
