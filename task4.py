# import requests
# import pprint
# import os
# import json
# from task1 import top_scrape_list
# from bs4 import BeautifulSoup

# link='https://www.imdb.com/title/tt0066763/'
# def scrape_movie_details(url):
# 	movies=top_scrape_list()
# 	Dictionary={}
# 	movie_list=[]
# 	list_for_directors=[]
# 	list_for_languages=[]
# 	list_for_genre=[]
# 	req=requests.get(url)
# 	# print(req)
# 	result=req.text
# 	# print(result)
# 	page=BeautifulSoup(result,"html.parser")
# 	data=page.find('div',class_='title_wrapper')
# 	var=(data.text).strip()
# 	name=data.find('h1').text
# 	# print(name)
# 	s=''
# 	for i in name:
# 		if i !="(":
# 			s+=i
# 		else:
# 			break
# 	# print(s)
# 	Dictionary["name"]=s.strip('\xa0')

# 	var_1=page.find('div',class_='plot_summary_wrapper')
# 	add=var_1.find('div',class_='plot_summary')
# 	bio_text=var_1.find('div',class_='summary_text').text.strip()
# 	Dictionary["bio"]=bio_text

# 	var_2=add.find('div',class_='credit_summary_item')
# 	director=var_2.find('a').text
# 	list_for_directors.append(director)
# 	# print(list_for_directors)
# 	Dictionary["director"]=list_for_directors

# 	detail=page.find('div', attrs={"class":"article","id":"titleDetails"})
# 	txt_block=detail.find_all('div',class_='txt-block')
# 	for i in txt_block:
# 		if i.find('h4') in i:
# 			h4=i.find('h4').text
# 			if h4=='Country:':
# 				country=i.find_all('a')
# 				for j in country:
# 					country_1=j.text
# 					Dictionary["country"]=country_1

# 			if h4=='Language:':
# 				lang=i.find_all('a')
# 				for j in lang:
# 					language=j.text
# 					list_for_languages.append(language)
# 				Dictionary["language"]=list_for_languages

# 	slate=page.find('div',class_='poster')
# 	poster_url=slate.find('img').get('src')
# 	# print(poster_url)
# 	Dictionary["poster_url"]=poster_url

# 	time=page.find('div',class_='subtext')
# 	time_1=time.find('time').get_text().strip().split()
# 	# print(time_1)
	
# 	if len(time_1)<2:
# 		x=int(time_1[0].strip('h'))
# 		y=0
# 	else:
# 		x=int(time_1[0].strip('h'))
# 		y=int(time_1[1].strip('min'))
# 	runtime=str(x*60+y)+" min"
# 	# print(runtime)
# 	Dictionary["runtime"]=runtime

# 	genre=time.find('a').text
# 	list_for_genre.append(genre)
# 	Dictionary["genre"]=list_for_genre
# 	return(Dictionary)
# 	# movie_list.append(Dictionary)
# 	# pprint.pprint(movie_list)
# 	# return(movie_list)
# # print (scrape_movie_details(link))

# =====================edited code========
import requests
import pprint
import os
import json
from task1 import top_scrape_list
from bs4 import BeautifulSoup

link='https://www.imdb.com/title/tt8108198/'
def scrape_movie_details(url):
	movies=top_scrape_list()
	Dictionary={}
	movie_list=[]
	list_for_directors=[]
	list_for_languages=[]
	list_for_genre=[]
	req=requests.get(url)
	# print(req)
	result=req.text
	# print(result)
	page=BeautifulSoup(result,"html.parser")
	data=page.find('div',class_='title_wrapper')
	var=(data.text).strip()
	name=data.find('h1').text
	# print(name)
	s=''
	for i in name:
		if i !="(":
			s+=i
		else:
			break
	# print(s)
	Dictionary["name"]=s.strip('\xa0')

	var_1=page.find('div',class_='plot_summary_wrapper')
	add=var_1.find('div',class_='plot_summary')
	bio_text=var_1.find('div',class_='summary_text').text.strip()
	Dictionary["bio"]=bio_text

	var_2=add.find('div',class_='credit_summary_item')
	director=var_2.find('a').text
	list_for_directors.append(director)
	# print(list_for_directors)
	Dictionary["director"]=list_for_directors

	detail=page.find('div', attrs={"class":"article","id":"titleDetails"})
	txt_block=detail.find_all('div',class_='txt-block')
	for i in txt_block:
		if i.find('h4') in i:
			h4=i.find('h4').text
			if h4=='Country:':
				country=i.find_all('a')
				for j in country:
					country_1=j.text
					Dictionary["country"]=country_1

			if h4=='Language:':
				lang=i.find_all('a')
				for j in lang:
					language=j.text
					list_for_languages.append(language)
				Dictionary["language"]=list_for_languages

	slate=page.find('div',class_='poster')
	poster_url=slate.find('img').get('src')
	# print(poster_url)
	Dictionary["poster_url"]=poster_url

	time=page.find('div',class_='subtext')
	time_1=time.find('time').get_text().strip().split()
	# print(time_1)
	
	if len(time_1)<2:
		x=int(time_1[0].strip('h'))
		y=0
	else:
		x=int(time_1[0].strip('h'))
		y=int(time_1[1].strip('min'))
	runtime=str(x*60+y)+" min"
	# print(runtime)
	Dictionary["runtime"]=runtime

	genre=page.find('a').text
	list_for_genre.append(genre)
	bar=(time.find_all('a'))
	list1=[]
	for m in bar:
		# print(m.text)
		list1.append(m.text)
	p=(list1.pop())
	# print(p)
	# print(list1)
	Dictionary["genre"]=list1
	return(Dictionary)


# scrape_movie_details(link)


