import requests
import pprint
import json
import os
from bs4 import BeautifulSoup
if os.path.isfile('flipkart.json'):
	with open('flipkart.json','r')as file:
		file_data=json.load(file)
		print(file_data)
else:

	link="https://www.flipkart.com/search?q=mi+all+mobile&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_0_6&otracker1=AS_QueryStore_OrganicAutoSuggest_0_6&as-pos=0&as-type=RECENT&as-searchtext=mi%20all%20"
	req=requests.get(link)
	# print(req)
	page=req.text
	# print(page)
	soup=BeautifulSoup(page,'html.parser')
	# print(soup)
	main_div=soup.find_all('div',class_="_1UoZlX")
	# print(main_div)
	list_for_all_phones=[]
	list_for_rupess=[]
	list_for_rating=[]
	list_for_all_detail=[]
	dictionary={}
	dic_list=[]
	for i in main_div:
		# print(i)
		col=(i.find('div',class_='_1-2Iqu row'))
		# print(col)
		n=col.find('div',class_='_3wU53n')
		text=(n.text)
		list_for_all_phones.append(text)
		for k in list_for_all_phones:
			dictionary['mobile_name']=k

		price=col.find('div',class_='_1vC4OE _2rQ-NK')
		price_text=(price.text)
		list_for_rupess.append(price_text)
		for l in list_for_rupess:
			dictionary['price']=l

		rating=col.find('div',class_='hGSR34')
		rt=(rating.text)
		list_for_rating.append(rt)
		for m in list_for_rating:
			dictionary['rating']=m

		b=col.find('div',class_='_3ULzGw')
		c=b.find('ul')
		for j in c:
			sp=(j.text).split('\n')
			list_for_all_detail.append(sp)
		dictionary['ram']=list_for_all_detail[0]
		dictionary['Display']=list_for_all_detail[1]
		dictionary['camera']=list_for_all_detail[2]
		dictionary['battery']=list_for_all_detail[3]
		dictionary['processor']=list_for_all_detail[4]
		dictionary['warranty']=list_for_all_detail[5]

		# pprint.pprint(dictionary)
		dic_list.append(dictionary)
	# pprint.pprint(dic_list)
	with open('flipkart.json','w')as file:
		json.dump(dic_list,file)

	# print(list_for_all_phones)
	# print(list_for_rupess)
	# print(list_for_rating)
	# print(list_for_all_detail)


	