import json
import  os
from task1 import top_scrape_list
from task5 import scrape_movie_details
task_1=top_scrape_list()
def function_for_task_8():
	for i in task_1:
		link=(i['url'])
		var=link[27:36]
		# print(var)
		task_2=scrape_movie_details(link)	
		json_file=var+".json"
		if os.path.isfile(json_file):
			print("already exists")
		else:
			with open(json_file,'w')as data:
				json.dump(task_2,data)
		# print(task_2)

function_for_task_8()