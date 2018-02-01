from django.conf.urls import url, include
from . import views
from django.views.generic import ListView, DetailView
from rugby.models import Match
from rugby.models import Try
from rugby.models import Player
from rugby.models import Team

import itertools
from itertools import chain
from django.urls import path
from rugby.views import AllPlayersView
from rugby.views import DetailPlayerView
from rugby.views import TeamView
from rugby.views import PlayerView
from rugby.views import TryFormView
from datetime import date


today = date.today()
print(today.year)

single_match = Match.objects.filter(tries_created=0).order_by("-date").first()
match_players = []
match_players.append(single_match)
home_players = Player.objects.all().filter(team=single_match.home_team)

for home_player in home_players:
    match_players.append(home_player)

away_players = Player.objects.all().filter(team=single_match.away_team)

for away_player in away_players:
    match_players.append(away_player)


print(single_match)


#SUPER RUGBY

'''
super_matches = Match.objects.filter(rd=1).filter(league="super").filter(date__year = today.year - 2).order_by("-date")
super_tries = Try.objects.all().filter(match__rd=1)[:10]
super_players = []

for i in super_matches:
    home_players = Player.objects.all().filter(team=i.home_team)

    for home_player in home_players:
        super_players.append(home_player)

    away_players = Player.objects.all().filter(team=i.away_team)

    for away_player in away_players:
        super_players.append(away_player)



super_set = []




for i in super_matches:
    super_set.append(i)
    print("HI")

for j in super_tries:
	super_set.append(j)

super_set.extend(super_players)

print(len(super_set))


#AVIVA PREMIERSHIP
aviva_matches = Match.objects.filter(rd=13).filter(league="aviva").filter(date__year = today.year).order_by("-date")
aviva_tries = Try.objects.all()[:10]
aviva_set = []

for i in aviva_matches:
	aviva_set.append(i)

for j in aviva_tries:
	aviva_set.append(j)

#INTERNATIONAL
international_matches = Match.objects.filter(rd=1).filter(league="international").order_by("-date")
international_tries = Try.objects.all()[:10]
international_set = []

for i in international_matches:
	international_set.append(i)

for j in international_tries:
	international_set.append(j)

#PRO 14
pro_matches = Match.objects.filter(rd=1).filter(league="pro14").order_by("-date")
pro_tries = Try.objects.all()[:10]
pro_set = []

for i in pro_matches:
	pro_set.append(i)

for j in pro_tries:
	pro_set.append(j)


#TOP 14
top_matches = Match.objects.filter(rd=1).filter(league="top14").order_by("-date")
top_tries = Try.objects.all()[:10]
top_set = []

for i in top_matches:
	top_set.append(i)

for j in top_tries:
	top_set.append(j)


print(include)
'''

print(url)

urlpatterns = [
	url(r'^search/$', views.search, name='search'),
    path('tryform/', TryFormView.as_view()),
    #url(r'^tryform/$', ListView.as_view(queryset=match_players, template_name="rugby/try_form.html")),
    #url(r'^$', views.index, name='index'),
    url(r'^thankyou/$', views.thankyou, name='thankyou'),
    #url(r'^super/$', ListView.as_view(queryset=super_set, template_name="rugby/video_page.html")),
    #url(r'^aviva/$', ListView.as_view(queryset=aviva_set, template_name="rugby/video_page.html")),
    #url(r'^international/$', ListView.as_view(queryset=international_set, template_name="rugby/video_page.html")),
    #url(r'^pro/$', ListView.as_view(queryset=pro_set, template_name="rugby/video_page.html")),
    #url(r'^top/$', ListView.as_view(queryset=top_set, template_name="rugby/video_page.html")),
    #path('allplayers/', AllPlayersView.as_view()),
    #url(r'^team/(?P<pk>[0-9]+)/$', TeamView.as_view(template_name="rugby/team_page.html")),
    #url(r'^player/(?P<pk>[0-9]+)/$', PlayerView.as_view(template_name="rugby/player_page.html")),
    #url(r'^(?P<pk>[0-9]+)/$', DetailView.as_view(model=Team, template_name="rugby/team_page.html")),
    #url(r'^(player?P<pk>\d+)$', DetailView.as_view(model=Player, template_name="rugby/video_page.html")),



    # All Teams #
    #url(r'^teams/crusaders$', ListView.as_view(queryset=super_set, template_name="rugby/video_page.html")),
    
]
