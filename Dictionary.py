#Dictionary
#注意事項
# 1.用大括括
# 2.'key':'value'
# 3.最後一項前面都需要用逗點

dic1 = {
	'ramen' : '拉麵',
	'frenchfries' : '薯條'
}

dic2 = {
	'name' : 'hamburger',
	'price' : 80
}

dic3 = {
	'name' : 'frenchfries',
	'price' : 50
}
listofdic = [dic2, dic3]

print(listofdic[0]['name'])
print(dic2['name'])
print(dic3['name'])
