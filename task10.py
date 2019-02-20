import pprint 
import random
import time
import json
import os
from task1 import top_scrape_list
from task4 import scrape_movie_details


def analyse_language_and_directors():
	if os.path.isfile("all_movies_data.json"):
		with open("all_movies_data.json","r+")as file_data:
			var=json.load(file_data)
		
			list_for_all_directors=[]
			list_for_all_language=[]
			list_for_uni_director=[]
			list_for_uni_language=[]
			for j in var:	
				a=j['director']
				b=j['language']
				for k in a:
					if k not in list_for_uni_director:
						list_for_uni_director.append(k)
				for l in b:
					if l not in list_for_uni_language:
						list_for_uni_language.append(l)
			# print((list_for_all_directors))
			# print((list_for_uni_director))
			# print (list_for_uni_language)
			main_dic={}
			for j in list_for_uni_director:
				mini_dic={}
				for i in list_for_uni_language:
					count=0
					for k in var:
						lang=k["language"]
						direc=k["director"]
					# print (lang,direc)
						if i in lang and j in direc:
							count+=1
					if count>0:
						# print (j,i,count)
						mini_dic[i]=count
				main_dic[j]=mini_dic
			pprint.pprint(main_dic)
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


analyse_language_and_directors()