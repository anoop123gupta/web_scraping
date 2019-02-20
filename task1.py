import requests
import pprint
import json
import os
from bs4 import BeautifulSoup

def top_scrape_list():
	if os.path.isfile("cache_file_for_task_1.json"):
		with open("cache_file_for_task_1.json","r+")as data:
			file=json.load(data)
			return(file)

	else:
		endpoint='https://www.imdb.com/india/top-rated-indian-movies/'
		req=requests.get(endpoint)
		# print(req)
		result=req.text
		# print(result)
		soup=BeautifulSoup(result,'html.parser')
		# print(soup)
		main=soup.find('div',class_='article')
		# print(main)
		sub_main=main.find('div',class_='lister')
		# print(sub_main)
		tbody=sub_main.find('tbody',class_='lister-list')
		# print(tbody)
		trs=tbody.find_all('tr')
		# print(trs)
		dic={}
		lit=[]
		rank=0
		list_year=[]
		for tr in trs:
			rank+=1
			td=tr.find('td',class_='titleColumn')
			a=td.find('a').text
			# print(rank,a)

			year=td.find('span').text
			year=int(year[1:5])
			if year not in list_year:
				list_year.append(year)
			# print(year[1:5])

			link=td.find('a')
			link=("https://www.imdb.com"+link.get('href'))
			link=link
			# link=link[0:37]
			# print(link)

			rating=tr.find('td',class_='ratingColumn imdbRating')
			rate=(rating.text).strip()
			# print(rate)

			dic={'Title':a,'rank':rank,'year':year,'url':link,'rating':rate}
			# print(dic)
			lit.append(dic)
			# print(lit)
		# return(list_year)
		# return(lit)
		with open("cache_file_for_task_1.json","w")as data:
			json.dump(lit,data)

movies=(top_scrape_list())
# pprint.pprint(movies)
