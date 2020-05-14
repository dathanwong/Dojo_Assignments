from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker

def index(request):
	baseball = League.objects.filter(sport="Baseball")
	women = League.objects.filter(name__icontains="womens")
	hockey = League.objects.filter(sport__icontains="hockey")
	notFootball = League.objects.exclude(sport__icontains="football")
	conferences = League.objects.filter(name__icontains="conference")
	atlanticRegion = League.objects.filter(name__icontains="atlantic")
	dallas = Team.objects.filter(location="Dallas")
	raptors = Team.objects.filter(team_name__icontains="raptors")
	city = Team.objects.filter(location__icontains="city")
	t = Team.objects.filter(team_name__istartswith="T")
	alpha = Team.objects.all().order_by("location")
	reverse = Team.objects.all().order_by("-team_name")
	coopers = Player.objects.filter(last_name="Cooper")
	joshuas = Player.objects.filter(first_name="Joshua")
	jocoop = coopers.exclude(first_name="Joshua")
	alexWyatt = Player.objects.filter(first_name="Alexander") | Player.objects.filter(first_name="Wyatt")
	context = {
		"leagues": League.objects.all(),
		"teams": Team.objects.all(),
		"players": Player.objects.all(),
		"baseballLeagues": baseball,
		"womenLeagues": women,
		"hockeyLeagues": hockey,
		"notFootballLeagues": notFootball,
		"conferences": conferences,
		"atlantic": atlanticRegion,
		"dallas": dallas,
		"raptors": raptors,
		"city": city,
		"t": t,
		"alpha": alpha,
		"reverse": reverse,
		"coopers": coopers,
		"joshuas": joshuas,
		"jocoop": jocoop,
		"alexWyatt": alexWyatt,
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")