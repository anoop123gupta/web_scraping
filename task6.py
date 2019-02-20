import pprint
from task5 import get_movie_list_details
from task4 import scrape_movie_details
lista=get_movie_list_details()

def analyse_movies_language(list_1):
    list_2=[]
    uni=[]
    Dict={}
    for i in list_1:
        a=(i['language'])
        # print(a)
        for j in a:
            # print(j)
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
    # print(m,count)
        Dict[m]=count
    return(Dict)
analyse_movies_language(lista)


