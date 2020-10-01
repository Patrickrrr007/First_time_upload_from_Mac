#記帳程式清單

products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q': #quit
		break
	price = input('請輸入商品價格:')
	'''p = []
	p.append(name)
	p.append(price)'''
	#前三行可以這樣寫

	p = [name, price]
	products.append(p)
	#又可以直接簡潔成
	#products.append([name, price])
print('總共有', len(products), '項')
print(products)
#print(products[0][1])
#這樣寫不好 依序把所有產品都列出來可這樣寫
for p in products:
#記得要寫對框框！！ p[]!!	
	print(p[0], '的價格是:',p[1] )

with open('Products_list.txt', 'w') as f:
	for p in products:
		f.write(p[0] + ',' + p[1] + '\n')
#每次寫是會更新的喔！！