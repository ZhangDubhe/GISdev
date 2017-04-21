# written by python 3.6
cities_list = map(lambda a: [a[0], float(a[1]), float(a[2])], [i.split(",") for i in open("F:\data\ArcPy\china_city.txt", 'r')])
print(" 最南面的城市:")
cities_sort_south = sorted(cities_list, key=lambda x: x[2])
for  i in range(0,10,1):
    print (cities_sort_south[i])
    
cities_list = map(lambda a: [a[0], float(a[1]), float(a[2])], [i.split(",") for i in open("F:\data\ArcPy\china_city.txt", 'r')])
print(" \n最东面的城市:")
cities_sort_east = sorted(cities_list, key=lambda x: x[1],reverse=True)
for t in cities_sort_east[:10]:
    print(t)
