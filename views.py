from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.views.generic import TemplateView, DetailView
from.models import Player
from.models import Team
from.models import Match
from.models import Try
from .filters import TryFilter
from .forms import SubmitUrlForm


def search(request):
    try_list = Try.objects.all()
    try_filter = TryFilter(request.GET, queryset=try_list)

    return render(request, 'rugby/test.html', {'filter':try_filter})

class TryFormView(generic.ListView):
    template_name = "rugby/try_form.html"

    def get_queryset(self):
        single_match = Match.objects.filter(tries_created=0).order_by("-date").first()
        match_players = []
        match_players.append(single_match)
        home_players = Player.objects.all().filter(team=single_match.home_team)

        for home_player in home_players:
            match_players.append(home_player)

        away_players = Player.objects.all().filter(team=single_match.away_team)

        for away_player in away_players:
            match_players.append(away_player)

        return match_players

    def post(self, request, *args, **kwargs):
        names = request.POST.getlist('player_name')
        starts = request.POST.getlist('start_time')
        ends = request.POST.getlist('end_time')

        print(names)
        game = Match.objects.filter(tries_created=0).order_by("-date")[0]



        for n,s,e in zip(names,starts,ends):

            if n == 'Select Player':
                continue

            fixed_video_link = game.video_link + "?start=" + str(s) + "&end=" + str(e)

            p = Try(match=game,player=Player.objects.filter(name=n).first(),video_link=fixed_video_link,viewcount=0,ratings_average=0,start_time=s,end_time=e)
            p.save()
        
        
        game.tries_created = 1
        game.save()
        

        return render(request, "rugby/thankyou.html", {})


class AllPlayersView(generic.ListView):
    template_name = "rugby/allplayers.html"

    def get_queryset(self):
        return Player.objects.all()

class DetailPlayerView(generic.DetailView):

    model = Player
    template_name = "rugby/playerdetails.html"

class TeamView(DetailView):
    model = Team

    def get_context_data(self, **kwargs):
        context = super(TeamView, self).get_context_data(**kwargs)

        combined_query = []
        match_query = Match.objects.all().order_by("-date")[:32]
        try_query = Try.objects.all()

        for i in match_query:
            combined_query.append(i)

        for j in try_query:
            combined_query.append(j)
        
        context['object_list'] = combined_query
        
        return context

class PlayerView(DetailView):
    model = Player

    def get_context_data(self, **kwargs):
        context = super(PlayerView, self).get_context_data(**kwargs)

        combined_query = []
        match_query = Match.objects.all()
        try_query = Try.objects.all()

        for i in match_query:
            combined_query.append(i)

        for j in try_query:
            combined_query.append(j)
        
        context['object_list'] = combined_query
        
        return context




def index(request):
    return render(request, 'rugby/home.html')

def thankyou(request):
    return render(request, 'rugby/thankyou.html')

def contact(request):
    return render(request, 'rugby/basic.html', {'content':['Please email maidenrhys@gmail.com']})




# Create your views here.
