import pprint
from task1 import top_scrape_list

movies=top_scrape_list()
# print(movies)
def group_by_decade(movies):
	list_for_year=[]
	Dicta={}
	for i in movies:
		l=i['year']
		if l not in list_for_year:
			list_for_year.append(l)
	min_year=(min(list_for_year))
	max_year=(max(list_for_year))
	for i in range(1950,2000,10):
		list1=[]
		for j in range(10):
			var=i+j
			for k in movies:
				year=k['year']
				if var==year:
					list1.append(k)
		Dicta[i]=list1
	return(Dicta)
	# pprint.pprint(Dicta)

	# print(list1)

group_by_decade(movies)
