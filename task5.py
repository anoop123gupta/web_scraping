import pprint
import json
import os
from task4 import scrape_movie_details
from task1 import top_scrape_list

# def get_movie_list_details():
# 	var_2=top_scrape_list()
# 	list_for_task5=[]
# 	for i in range(len(var_2)):
# 		link=(var_2[i]['url'])
# 		if i==10:
# 			break
# 		else:
# 			var_3=(scrape_movie_details(link))
# 			list_for_task5.append(var_3)
# 	pprint.pprint(list_for_task5)
# get_movie_list_details(top_scrape_list)

def get_movie_list_details():
	if os.path.isfile('cache_for_task5.json'):
		with open('cache_for_task5.json','r')as f:
			var=json.load(f)
			return(var)
	else:
		li=[]
		movie_list=top_scrape_list()
		for i in range(len(movie_list)):
			link=movie_list[i]['url']
			if i==10:
				break
			else:
				var2=scrape_movie_details(link)
				li.append(var2)
		# pprint.pprint(li)
		# return(li)
		with open('cache_for_task5.json','w')as f:
			json.dump(li,f)

# print(get_movie_list_details())