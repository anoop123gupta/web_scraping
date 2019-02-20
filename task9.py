import random
import time
import json
import os
from task1 import top_scrape_list
from task4 import scrape_movie_details

def kya_naam_du():
	if os.path.isfile("all_movies_data.json"):
		with open('all_movies_data.json','r')as file_data:
			file=json.load(file_data)
			print(file)
		
	else:
		task_1=top_scrape_list()
		list_big=[]
		for i in task_1:
			link=(i['url'])
			time_1=random.randint(1,3)
			time.sleep(time_1)	
			task_2=scrape_movie_details(link)	
			list_big.append(task_2)
			with open("all_movies_data.json","w+")as file_data:
				json.dump(list_big,file_data)


kya_naam_du()




