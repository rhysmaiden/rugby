from django.db import models

def make_soup(url):
    thepage = urllib.request.urlopen(url)
    soupdata = BeautifulSoup(thepage, "html.parser")
    return soupdata

class Team(models.Model) :
    team_name = models.TextField()
    league = models.TextField(default='super')
    logo = models.TextField()
    primary_colour = models.TextField(default='#000000')
    secondary_colour = models.TextField(default='#FFFFFF')


    def __str__(self):
        return self.team_name

    def get_matches_of_team(self):
        matches = Team.objects.filter(team_name=self.team_name)
        #matches = Match.objects.filter(home_team=self.team_name)
        return matches

class Match(models.Model) :
    date = models.DateTimeField()
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_team')
    away_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='away_team')
    home_score = models.IntegerField()
    away_score = models.IntegerField()
    stadium = models.TextField()
    ref = models.TextField()
    attendance = models.IntegerField()
    video_link = models.TextField()
    league = models.TextField(default='super')
    rd = models.IntegerField(default=1)
    viewcount = models.IntegerField(default=1)
    ratings_average = models.IntegerField(default=2)
    tries_created = models.IntegerField(default=0)
    tries_in_match = models.IntegerField(default=3)

    def __str__(self):
        return str(self.date) + " - " + str(self.home_team.team_name) + " vs " + str(self.away_team.team_name)

    def update_rating(self) :

        
        url = self.video_link.replace("/s", "")
        
        soup = make_soup(url)
        print(soup.find("span", {"id": "visits"}))
       # print("##" + element)

      #  with open('updateratingtest.csv', 'a') as file:
       #     file.write(element)
        



class Player(models.Model) :
    name = models.TextField()
    age = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    picture = models.TextField(default='hi')
    coolfact = models.TextField(default='')

    def __str__(self):
        return self.name

class Try(models.Model) :
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    player = models.ForeignKey('Player', on_delete=models.CASCADE)
    video_link = models.TextField()
    viewcount = models.IntegerField(default=1)
    ratings_average = models.IntegerField(default=2)
    start_time = models.IntegerField(default=0)
    end_time = models.IntegerField(default=0)


    def __str__(self):
        return str(self.player) + " in " + str(self.match)

    


