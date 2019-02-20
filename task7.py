import pprint
from task5 import get_movie_list_details
list_1=get_movie_list_details()
def analyse_movies_directors():
    list_2=[]
    uni=[]
    Dict={}
    for i in list_1:
        a=i['director']
        # print(a)
        for j in a:
            list_2.append(j)
            if j not in uni:
                uni.append(j)
    # print(list_2)
    # print(uni)
    for m in uni:
        count=0
        for n in list_2:
            if m==n:
                count+=1
        retunr(m,count)
analyse_movies_directors()
