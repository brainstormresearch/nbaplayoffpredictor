import urllib.request
from bs4 import BeautifulSoup
import csv 



url_regseason = 'https://basketball.realgm.com/nba/teams/test/' 
url_regseason_1 = '/stats/'
url_regseason_2= '/Averages/All/points/All/desc/1/Regular_Season'

url_playoffs = 'https://basketball.realgm.com/nba/teams/test/'

url_playoffs_1 = '/stats/'

url_playoffs_2 = '/Averages/All/points/All/desc/1/Playoffs'

playoffs = 0

for year in range(2000,2010):


	file = open('nbadata' + str(year)+'.csv', 'w+', newline ='')
	write = csv.writer(file)

	for i in range(0,40):

		tds = []
		ths = []
		team_found = 0
		url_reg = url_regseason + str(i+1) + url_regseason_1 + str(year) + url_regseason_2

		nbateam = urllib.request.urlopen(url_reg)

		soup = BeautifulSoup(nbateam,"lxml")

		title = soup.find('title')
		t = title.string

		x = t.split()

		team = x[0]+' '+x[1]
		print(team)
		

		divs = soup.findAll("table")

		for div in divs:
			rows = div.findAll('tr')

			for row in rows:
	   			flag = 0
	   			cells = (row.findAll('td'))


	   			for cell in cells:

					#if len(cells) > 0:


	   				if cell.string == "Team Totals":

	   					flag = 1
	   					team_found = 1
	   					tds.append(team)

	   					headers = div.findAll('th')


	   					for header in headers:

	   						ths.append(header.string)

	   					for h in range(1,len(ths)):
	   						ths.append('o-' + ths[h])

	   					

	   					if i == 0:
	   						write.writerow(ths)
	   					
	   					continue

	   				if flag == 1:
	   					tds.append(float(cell.string))

	   				if cell.string == "Opponent Totals":
	   					flag = 2

	   					continue

	   				if flag == 2:
	   					tds.append(float(cell.string))




		url_play = url_playoffs + str(i+1) + url_playoffs_1 + str(year) + url_playoffs_2
		nba_playoffs = urllib.request.urlopen(url_play)
		soup2 = BeautifulSoup(nba_playoffs,"lxml")

		soupstring = str(soup2)
		p = soupstring.find('currently available')
	
		

		if team_found==1:	
			if p != -1:
				tds.append(0)
			else:
				tds.append(1)

				playoffs += 1


		if tds != []:

			write.writerow(tds)	
			
	file.close()
			




# url = 'https://basketball.realgm.com/nba/teams/Boston-Celtics/2/Stats/2019/Averages/All/points/All/desc/1/Regular_Season'

# nbateam = urllib.request.urlopen(url)

# soup = BeautifulSoup(nbateam,"lxml")
# # tables = soup.findAll("tr", {"data-stat" : "Team Totals"})
# w = []

# url2 = 'https://basketball.realgm.com/nba/teams/Cleveland-Cavaliers/5/stats/2019/Averages/All/points/All/desc/1/Playoffs'
# nbaplayoffs = urllib.request.urlopen(url2)

# soup2 = BeautifulSoup(nbaplayoffs,"lxml")

# div_playoffs = soup2.findAll("table")
# print (div_playoffs)

# tds = []
# divs = soup.findAll("table")

# for div in divs:
# 	rows = div.findAll('tr')

# 	for row in rows:
#    		flag = 0
#    		cells = (row.findAll('td'))

#    		for cell in cells:
#    			if cell.string == "Team Totals":
#    				flag = 1
#    				continue
#    			if flag == 1:
#    				tds.append(float(cell.string))

# print(tds)