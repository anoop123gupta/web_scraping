import pprint
from task1 import top_scrape_list
# movies=top_scrape_list()
# print(movies)
def group_by_year():
	movies=top_scrape_list()

	list_for_year=[]
	for i in movies:
		l=i['year']
		if l not in list_for_year:
			list_for_year.append(l)
	# print(list_for_year)

	Dix={}
	for i in list_for_year:
		list_2=[]
		for j in movies:
			var=(j['year'])
			if i==var:
				list_2.append(j)
		Dix[i]=list_2
	return(Dix)
	# pprint.pprint(Dix)
group_by_year()


'''
import pprint
from task1 import top_scrape_list

movies=top_scrape_list()

list1=[1950,1960,1970,1980,1990,2000]
list2=[1959,1969,1979,1989,1999,2019]
def group_by_decade(movies):
	movies=top_scrape_list()
	DICT={}
	for i in range(len(list1)):
		first=list1[i]
		second=list2[i]
		list_decade=[]
		for j in movies:
			l=j['year']
			if l>=first and l<=second:
				list_decade.append(j)
		DICT[first]=list_decade
	pprint.pprint(DICT)

group_by_decade(movies)
'''