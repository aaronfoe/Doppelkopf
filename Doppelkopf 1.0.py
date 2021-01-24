#Checks sign, returns "Pos", "Neg", "Null"
def sign(x):
	if abs(int(x)) == x:
		sgn = "Pos"
	elif abs(int(x)) != x:
		sgn = "Neg"
	else:
		sgn = "Null"
	return sgn

#Returns: Gametype + normal or solo. Error = "KP"
def typ(a,b,c,d):
	if sign(a) == "Pos" and sign(b) == "Pos" and sign(c) == "Neg" and sign(d) == "Neg":
		k = Pa + " + "+ Pb + "s Sieg"
		l = "normal"
		return [k,l]
	elif sign(a) == "Pos" and sign(b) == "Neg" and sign(c) == "Pos" and sign(d) == "Neg":
		k = Pa + " + " + Pc + "s Sieg"
		l = "normal"
		return [k,l]
	elif sign(a) == "Pos" and sign(b) == "Neg" and sign(c) == "Neg" and sign(d) == "Pos":
		k = Pa + " + " + Pd  + "s Sieg"
		l = "normal"
		return [k,l]
	elif sign(a) == "Neg" and sign(b) == "Pos" and sign(c) == "Pos" and sign(d) == "Neg":
		k = Pb + " + " + Pc + "s Sieg"
		l = "normal"
		return [k,l]
	elif sign(a) == "Neg" and sign(b) == "Pos" and sign(c) == "Neg" and sign(d) == "Pos":
		k = Pb + " + " + Pd + "s Sieg"
		l = "normal"
		return [k,l]
	elif sign(a) == "Neg" and sign(b) == "Neg" and sign(c) == "Pos" and sign(d) == "Pos":
		k = Pd + " + " + Pc + "s Sieg"
		l = "normal"
		return [k,l]
	elif sign(a) == "Pos" and sign(b) == "Neg" and sign(c) == "Neg" and sign(d) == "Neg":
		k = "Solo " + Pa + ", gewonnen."
		l = "solo"
		return [k,l]
	elif sign(a) == "Neg" and sign(b) == "Pos" and sign(c) == "Neg" and sign(d) == "Neg":
		k = "Solo " + Pb + ", gewonnen."
		l = "solo"
		return [k,l]
	elif sign(a) == "Neg" and sign(b) == "Neg" and sign(c) == "Pos" and sign(d) == "Neg":
		k = "Solo " + Pc + ", gewonnen."
		l = "solo"
		return [k,l]
	elif sign(a) == "Neg" and sign(b) == "Neg" and sign(c) == "Neg" and sign(d) == "Pos":
		k = "Solo " + Pd + ", gewonnen."
		l = "solo"
		return [k,l]
	elif sign(a) == "Neg" and sign(b) == "Pos" and sign(c) == "Pos" and sign(d) == "Pos":
		k = "Solo " + Pa + ", verloren."
		l = "solo"
		return [k,l]
	elif sign(a) == "Pos" and sign(b) == "Neg" and sign(c) == "Pos" and sign(d) == "Pos":
		k = "Solo " + Pb + ", verloren."
		l = "solo"
		return [k,l]
	elif sign(a) == "Pos" and sign(b) == "Pos" and sign(c) == "Neg" and sign(d) == "Pos":
		k = "Solo " + Pc + ", verloren."
		l = "solo"
		return [k,l]
	elif sign(a) == "Pos" and sign(b) == "Pos" and sign(c) == "Pos" and sign(d) == "Neg":
		k = "Solo " + Pd + ", verloren."
		l = "solo"
		return [k,l]
	else:
		k = "KP"
		l = "low"
		return [k,l]
	#return k

#Checks entered values, returns solo, normal or falsch
def value_check(a,b,c,d):
	#Normales Spiel
	if abs(a) == abs(b) == abs(c) == abs(d):
		points = "normal"
	#Solo a
	elif abs(a) == 3*abs(b) == 3*abs(c) == 3*abs(d):
		points = "solo"
	#Solo b
	elif abs(b) == 3*abs(a) == 3*abs(c) == 3*abs(d):
		points = "solo"
	#Solo c
	elif abs(c) == 3*abs(a) == 3*abs(b) == 3*abs(d):
		points = "solo"
	#Solo d
	elif abs(d) == 3*abs(a) == 3*abs(b) == 3*abs(c):
		points = "solo"
	else:
		points = "falsch"
	return points

#Integerckeck 
def int_check_one(P):
	k = False
	while k == False:
		print "Punkte", P
		x = raw_input("")
		try:
			int(x)
			k = True
		except ValueError:
			print "Geben sie eine ganze Zahl ein"
	return int(x)
def int_check_two():
	k = False
	while k == False:
		print "Welches Spiel moechten sie verbessern?"
		x = raw_input("")
		try:
			int(x)
			k = True
		except ValueError:
			print "Geben sie eine ganze Zahl ein"
	return int(x)
#Spielernamen
def names(Pa,Pb,Pc,Pd):
	print
	print "Die Spieler heissen:"
	print
	print Pa + ", " + Pb + ", " + Pc + ", " + Pd 
	Pa = raw_input("Neuer Name Spieler 1:	")
	Pb = raw_input("Neuer Name Spieler 2:	")
	Pc = raw_input("Neuer Name Spieler 3:	")
	Pd = raw_input("Neuer Name Spieler 4:	")
	players = {"Pa":Pa,"Pb":Pb,"Pc":Pc,"Pd":Pd}
	return players
def no_names():
	print
	print "Bitte benennen sie die Spieler!"
	print
	Pa = raw_input("Name Spieler 1:	")
	Pb = raw_input("Name Spieler 2:	")
	Pc = raw_input("Name Spieler 3:	")
	Pd = raw_input("Name Spieler 4:	")
	players = {"Pa":Pa,"Pb":Pb,"Pc":Pc,"Pd":Pd}
	return players

#Spieladdition: Addiert Spiele eines Tags; returns sums for each player
def player_sum_day(x,day):
	sum = 0
	for i in day:
		sum += i[x]
	return sum

def player_league_points(x):
	print

#Programm; initial statements
import cPickle
running = True

while running == True:
	
	try:
		with open("./DKData/players.txt","rb") as players:
			spieler = cPickle.load(players)
			
	except IOError:	
		spieler = no_names()
		with open("./DKData/players.txt","wb") as players:
			cPickle.dump(spieler, players)
	
	Pa = spieler["Pa"]
	Pb = spieler["Pb"]
	Pc = spieler["Pc"]
	Pd = spieler["Pd"]

	print
	print "DOPPELKOPF V1.0"
	print "Hauptmenue"
	print
	print "Was moechten sie tun? (Entsprechende Zahl + Enter)"
	print "1: Neues Spiel eingeben"
	print "2: Statistiken einsehen"
	print "3: Alte Spiele einsehen"
	print "4: Spielernamen aendern"
	print "5: Programm beenden"  
	print "6: Alle Daten loeschen"
	men = raw_input("")
#Menu
	if men == "1":
		day = []
		eingabe = True
		while eingabe == True:	
			row = 1
			spiel = True		
			while spiel == True:			
				print
				print "Werte eingeben"
				print
				a = int_check_one(Pa)
				b = int_check_one(Pb)
				c = int_check_one(Pc)
				d = int_check_one(Pd)

				y = value_check(a,b,c,d)
				z = typ(a,b,c,d)

#checks input for validity
				if y == "normal" and z[1] == "normal":
					print
					print z[0]
					print
					spiel = False
					savegame = True
				elif y == "solo" and z[1] == "solo":
					print
					print z[0]
					print
					spiel = False
					savegame = True
				else:
					print
					print "Falsche Eingabe."
					print "Enter um erneut einzugeben. S und Enter um das letzte Spiel zu verwerfen"
					savegame = False
					if raw_input("").lower() == "s":
						spiel = False
				
#Saves Game in new Matrix row as a dictionary with Name:Point pairs as a new round
				if savegame == True:
					day.append({Pa:a,Pb:b,Pc:c,Pd:d})
					row += 1
#Ask for input: Continue or stop?
			abb = raw_input("Um ein weiteres Spiel einzugeben Enter druecken. Um die Eingabe abzuschliessen, druecken sie S und dann Enter.")
			if abb.lower() != "s":
				print abb
				eingabe = True
			else:
				eingabe = False
################################		
#prints game
		correct = False
		while correct == False:
			print Pa, " "*(11-len(Pa)), Pb, " "*(11-len(Pb)), Pc, " "*(11-len(Pc)), Pd, " "*(11-len(Pd)), 
			for i in day:
				print
				for j in [Pa,Pb,Pc,Pd]:
					if len(str(i[j])) == 1:
						print i[j], " "*10,
					elif len(str(i[j])) == 2:
						print i[j], " "*9,
					elif len(str(i[j])) == 3:
						print i[j], " "*8,
					elif len(str(i[j])) == 4:
						print i[j], " "*7,
					elif len(str(i[j])) == 5:
						print i[j], " "*6,
					elif len(str(i[j])) == 6:
						print i[j], " "*5,
#correct game?		
			print
			print
			if raw_input("Sind alle Werte korrekt? Enter fuer Ja, S und Enter fuer Nein").lower() == "s":
				row = int_check_two() - 1
				spiel = True
				while spiel == True:
					print
					print "Werte eingeben"
					print
					a = int_check_one(Pa)
					b = int_check_one(Pb)
					c = int_check_one(Pc)
					d = int_check_one(Pd)

					y = value_check(a,b,c,d)
					z = typ(a,b,c,d)

#checks values for validity
					if y == "normal" and z[1] == "normal":
						print
						print z[0]
						print
						spiel = False
						savegame = True
					elif y == "solo" and z[1] == "solo":
						print
						print z[0]
						print
						spiel = False
						savegame = True
					else:
						print
						print "Falsche Eingabe."
						print "Enter um erneut einzugeben. S und Enter um das letzte Spiel zu verwerfen"
						savegame = False
						if raw_input("").lower() == "s":
							spiel = False
				if savegame == True:
					day[row] = {Pa:a,Pb:b,Pc:c,Pd:d}

			else:
				correct = True
######### ALL VALUES ARE CORRECT NOW. Saves day ################
		games = {}
		safegames = {}
		try:
			with open("./DKData/allgames.txt","rb") as allgames:
				games = cPickle.load(allgames)
				newkey = len(games) + 1
				games[newkey] = day

			with open("./DKData/allgames.txt","wb") as allgames:
				cPickle.dump(games, allgames)
		except IOError:
			with open("./DKData/allgames.txt","wb") as allgames:
				games[1] = day
				cPickle.dump(games, allgames)
				print "except"
		
#######Emergency save
		try:
			with open("./DKData/safety.txt","rb") as safety:
				safegames = cPickle.load(safety)
				safekey = len(safegames) + 1
				safegames[safekey] = day

			with open("./DKData/safety.txt","wb") as safety:
				cPickle.dump(safegames, safety)
		except IOError:
			with open("./DKData/safety.txt","wb") as safety:
				safegames[1] = day
				cPickle.dump(safegames, safety)
				print "except"
		except EOFError:
			with open("./DKData/safety.txt","wb") as safety:
				safegames[1] = day
				cPickle.dump(safegames, safety)
				print "except"
		#print games
########## New Day is now saved
########## Calculations for new day		
		print
		print "Ergebnisse des Spieltages:"
		
		Paday = player_sum_day(Pa,day)
		Pbday = player_sum_day(Pb,day)
		Pcday = player_sum_day(Pc,day)
		Pdday = player_sum_day(Pd,day)


		ranking = {Pa:Paday, Pb:Pbday, Pc:Pcday, Pd:Pdday}
		rev_ranking = {Paday:Pa, Pbday:Pb, Pcday:Pc, Pdday:Pd}
		for key, value in ranking.iteritems():
			print key + ":", value

		league_points_day = {}

		points = [x for x in ranking.values()]
		first = max(points)
		points.remove(max(points))
		second = max(points)
		points.remove(max(points))
		third = max(points)
		points.remove(max(points))
		fourth = max(points)

		for player in ranking.keys():
			if ranking[player] == fourth:
				league_points_day[player] = 0
			elif ranking[player] == third:
				league_points_day[player] = 1
			elif ranking[player] == second:
				league_points_day[player] = 2
			elif ranking[player] == first:
				league_points_day[player] = 3
		
		print
		print "Erspielte Ligapunkte:"	
		for player in league_points_day:
			print player + ":", league_points_day[player]
		print
		raw_input("Enter zum fortfahren")

######Saving leaguepoints
		standings = {}		
		try:
			with open("./DKData/leaguepoints.txt","rb") as leaguepoints:
				standings = cPickle.load(leaguepoints)
				newkey = len(standings) + 1
				standings[newkey] = league_points_day

			with open("./DKData/leaguepoints.txt","wb") as leaguepoints:
				cPickle.dump(standings, leaguepoints)
		except IOError:
			with open("./DKData/leaguepoints.txt","wb") as leaguepoints:
				standings[1] = league_points_day
				cPickle.dump(standings, leaguepoints)
				print "except IO"
		except EOFError:
			with open("./DKData/leaguepoints.txt","wb") as leaguepoints:
				standings[1] = league_points_day
				cPickle.dump(standings, leaguepoints)
				print "except"

		#print standings
###### Standings are now saved in single-game-standings dictionary
	
	elif men == "2":
		print
		#Getting list of league points
		try:
			with open("./DKData/leaguepoints.txt","rb") as leaguepoints:
				standings = cPickle.load(leaguepoints)
				games_available = True
		except IOError:
			games_available = False
			print "Noch keine Daten vorhanden. Im Hauptmenue koennen Spiele eingetragen werden."
		except EOFError:
			games_available = False
			print "Noch keine Daten vorhanden. Im Hauptmenue koennen Spiele eingetragen werden."
		#Calculating current leaguepoints total
		lepoints_a = 0
		lepoints_b = 0
		lepoints_c = 0
		lepoints_d = 0

		for day in standings.values():
			lepoints_a += day[Pa]
			lepoints_b += day[Pb]
			lepoints_c += day[Pc]
			lepoints_d += day[Pd]
		
		print "Ligapunkte gesamt:"
		#print
		print Pa + ":",lepoints_a
		print Pb + ":",lepoints_b
		print Pc + ":",lepoints_c
		print Pd + ":",lepoints_d
		
		#Calculating current gamepoints total
		if games_available == True:
			try:
				with open("./DKData/allgames.txt","rb") as allgames:
					games = cPickle.load(allgames)
			except IOError:
				print "nogames"
			except EOFError:
				print "nogamesEOF"

			gapoints_a = 0
			gapoints_b = 0
			gapoints_c = 0
			gapoints_d = 0
			day_count = 0.0
			game_count = 0.0
			#Gets game_count
			for day in games.values():
				day_count += 1
				for game in day:
					gapoints_a += game[Pa]
					gapoints_b += game[Pb]
					gapoints_c += game[Pc]
					gapoints_d += game[Pd]
					game_count += 1
			print
			print "Spielpunkte gesamt:"
			print Pa + ":",gapoints_a
			print Pb + ":",gapoints_b
			print Pc + ":",gapoints_c
			print Pd + ":",gapoints_d
			print
			print "Anzahl der Spiele:", int(game_count)
			print
			print "Anzahl der Spieltage:", int(day_count)
			print
			print "Durchschnittliche Spiele pro Spieltag:", game_count/day_count
			print 
			print "Durchschnittliche Ligapunkte pro Spieltag:"
			print Pa + ":", lepoints_a/day_count 
			print Pb + ":", lepoints_b/day_count 
			print Pc + ":", lepoints_c/day_count 
			print Pd + ":", lepoints_d/day_count
			print
			print "Durchschnittliche Spielpunkte pro Spiel:"
			print Pa + ":", gapoints_a/game_count
			print Pb + ":", gapoints_b/game_count
			print Pc + ":", gapoints_c/game_count
			print Pd + ":", gapoints_d/game_count
######Gets combination stats
			ab_win = 0
			ac_win = 0
			ad_win = 0
			bc_win = 0
			bd_win = 0
			cd_win = 0
			so_a_win = 0
			so_b_win = 0
			so_c_win = 0
			so_d_win = 0
			so_a_los = 0
			so_b_los = 0
			so_c_los = 0
			so_d_los = 0

			for day in games.values():
				for match in day:
					points_a = match[Pa]
					points_b = match[Pb]
					points_c = match[Pc]
					points_d = match[Pd]

					game_type = typ(points_a,points_b,points_c,points_d)
					#print game_type[0]
					if game_type[0] == Pa + " + "+ Pb + "s Sieg":
						ab_win += 1
						#print "abSieg"
					elif game_type[0] == Pa + " + " + Pc + "s Sieg":
						ac_win += 1
						#print "acS"
					elif game_type[0] == Pa + " + " + Pd + "s Sieg":
						ad_win += 1
						#print "ads"
					elif game_type[0] == Pb + " + " + Pc + "s Sieg":
						bc_win += 1
						#print "bcs"
					elif game_type[0] == Pb + " + " + Pd + "s Sieg":
						bd_win += 1
						#print "bds"
					elif game_type[0] == Pd + " + " + Pc + "s Sieg":
						cd_win += 1
						#print "cdSieg"
					elif game_type[0] == "Solo " + Pa + ", gewonnen.":
						so_a_win += 1
						#print "saw"
					elif game_type[0] == "Solo " + Pb + ", gewonnen.":
						so_b_win += 1
						#print "sbw"
					elif game_type[0] == "Solo " + Pc + ", gewonnen.":
						so_c_win += 1
						#print "scw"
					elif game_type[0] == "Solo " + Pd + ", gewonnen.":
						so_d_win += 1
						#print "sdw"
					elif game_type[0] == "Solo " + Pa + ", verloren.":
						so_a_los += 1
						#print "sal"
					elif game_type[0] == "Solo " + Pb + ", verloren.":
						so_b_los += 1
						#print "sbl"
					elif game_type[0] == "Solo " + Pc + ", verloren.":
						so_c_los += 1
						#print "scl"
					elif game_type[0] == "Solo " + Pd + ", verloren.":
						so_d_los += 1
						#print "sdl"
					else:
						print "else"
						
			print			
			print "Teamstats:"
			print Pa, "+", Pb + ":", ab_win + cd_win, "Spiele gespielt.",ab_win, "Spiele gewonnen,", cd_win, "Spiele verloren"
			try:
				print "	", (ab_win/(ab_win + cd_win))*100,"Prozent der Spiele gewonnen"
				print
			except ZeroDivisionError:
				print
			print Pa, "+", Pc + ":", ac_win + bd_win, "Spiele gespielt.",ac_win, "Spiele gewonnen,", bd_win, "Spiele verloren"
			try:	
				print "	", (ac_win/(ac_win + bd_win))*100,"Prozent der Spiele gewonnen"
				print
			except ZeroDivisionError:
				print
			print Pa, "+", Pd + ":", ad_win + bc_win, "Spiele gespielt.",ad_win, "Spiele gewonnen,", bc_win, "Spiele verloren"
			try:
				print "	", (ac_win/(ad_win + bc_win))*100,"Prozent der Spiele gewonnen"
				print
			except ZeroDivisionError:
				print
			print Pb, "+", Pc + ":", bc_win + ad_win, "Spiele gespielt.",bc_win, "Spiele gewonnen,", ad_win, "Spiele verloren"
			try:	
				print "	", (ac_win/(bc_win + ad_win))*100,"Prozent der Spiele gewonnen"
				print
			except ZeroDivisionError:
				print
			print Pb, "+", Pd + ":", bd_win + ac_win, "Spiele gespielt.",bd_win, "Spiele gewonnen,", ac_win, "Spiele verloren"
			try:
				print "	", (ac_win/(bd_win + ac_win))*100,"Prozent der Spiele gewonnen"
				print
			except ZeroDivisionError:
				print
			print Pc, "+", Pd + ":", cd_win + ab_win, "Spiele gespielt.",cd_win, "Spiele gewonnen,", ab_win, "Spiele verloren"
			try:
				print "	", (ac_win/(cd_win + ab_win))*100,"Prozent der Spiele gewonnen"
				print
			except ZeroDivisionError:
				print
			print
			print "Soli:"
			print Pa,":", so_a_win, "Solos gewonnen", so_a_los, "Solos verloren"
			print Pb,":", so_b_win, "Solos gewonnen", so_b_los, "Solos verloren"
			print Pc,":", so_c_win, "Solos gewonnen", so_c_los, "Solos verloren"
			print Pd,":", so_d_win, "Solos gewonnen", so_d_los, "Solos verloren"
		


		raw_input()




	elif men == "3":
		print
		with open("./DKData/allgames.txt","rb") as allgames:
			games = cPickle.load(allgames)
		
		game_day_count = 1
		for day in games.values():
			print "Spieltag", game_day_count
			for match in day:	
				for player in match.keys():
					print player, match[player],
				print
			print
			game_day_count += 1
		
		raw_input()
	elif men == "4":
		namen = names(Pa,Pb,Pc,Pd)
		print
		with open("./DKData/players.txt", "wb") as players:
			cPickle.dump(namen, players)
		print "Die Spieler heissen jetzt:"
		for i in namen:
			print namen[i] 
	elif men == "5":
		running = False
	elif men == "6":
		loe = raw_input("Moechten sie wirklich alle Daten loeschen? J fuer Ja, beliebige Taste zum abbrechen")
		if loe.lower() == "j":
			games = {}
			with open("./DKData/allgames.txt","wb") as allgames:
				cPickle.dump(games, allgames)
			print "Daten wurden geloescht"
			standings = {}
			with open("./DKData/leaguepoints.txt","wb") as leaguepoints:
				cPickle.dump(standings, leaguepoints)

