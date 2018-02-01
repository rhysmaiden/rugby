from django.contrib import admin
from rugby.models import Match
from rugby.models import Player
from rugby.models import Try
from rugby.models import Team

admin.site.register(Match)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Try)