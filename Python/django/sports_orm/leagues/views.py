from django.shortcuts import render, redirect
from .models import League, Team, Player
from django.db.models import Count
from . import team_maker

def index(request):
	#For Part I
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
	
	#For Part II
	atlanticSoccer = Team.objects.filter(league_id = League.objects.filter(name="Atlantic Soccer Conference").first().id)
	penguins = Player.objects.filter(curr_team_id = Team.objects.filter(team_name="Penguins", location="Boston").first().id)
	icbcTeams = Team.objects.filter(league_id = League.objects.filter(name="International Collegiate Baseball Conference").first().id)
	icbcPlayers = []
	for team in icbcTeams.all():
		icbcPlayers += Player.objects.filter(curr_team__id=team.id)
	lopez = []
	acafTeams = Team.objects.filter(league_id = League.objects.filter(name="American Conference of Amateur Football").first().id)
	for team in acafTeams.all():
		lopez += Player.objects.filter(curr_team__id=team.id, last_name="Lopez")
	footballTeams = Team.objects.filter(league__name__icontains= "football")
	footballPlayers = []
	for team in footballTeams:
		footballPlayers += Player.objects.filter(curr_team__id=team.id)
	sophiaTeams = Team.objects.filter(curr_players__first_name="Sophia")
	sophiaLeagues = League.objects.filter(teams__curr_players__first_name="Sophia")
	flores = Player.objects.filter(last_name="Flores").exclude(curr_team=Team.objects.filter(team_name="Roughriders", location="Washington").first())
	samEvans = Team.objects.filter(all_players__first_name="Samuel", all_players__last_name="Evans")
	manitobaPlayers = Player.objects.filter(all_teams__location = "Manitoba", all_teams__team_name="Tiger-Cats")
	formerVikings = Player.objects.filter(all_teams__location = "Wichita", all_teams__team_name="Vikings").exclude(curr_team__location="Wichita", curr_team__team_name="Vikings")
	jacob = Team.objects.filter(all_players__first_name = "Jacob", all_players__last_name="Gray").exclude(team_name="Colts")
	joshua = Player.objects.filter(first_name="Joshua", all_teams__league__name="Atlantic Federation of Amateur Baseball Players")
	twelve = Team.objects.annotate(Count('all_players'))
	twelve = twelve.filter(all_players__count__gt=11)
	allPlayers = Player.objects.annotate(Count('all_teams'))
	allPlayers = allPlayers.order_by('all_teams__count')

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
		"atlanticSoccer": atlanticSoccer,
		"penguins": penguins,
		"icbcPlayers": icbcPlayers,
		"lopez": lopez,
		"footballPlayers": footballPlayers,
		"sophiaTeams": sophiaTeams,
		"sophiaLeagues": sophiaLeagues,
		"flores": flores,
		"samEvans": samEvans,
		"manitobaPlayers": manitobaPlayers,
		"formerVikings": formerVikings,
		"jacob": jacob,
		"joshua": joshua,
		"twelve": twelve,
		"allPlayers": allPlayers
	}
	return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")