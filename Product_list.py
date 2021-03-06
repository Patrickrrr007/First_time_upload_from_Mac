import os #operating system

	#記帳程式清單

def read_file(filename):
	products = []	
		#讀取檔案 r
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue 
				#如果有商品價格的話 直接進入到下一格
			name, price = line.strip().split(',')
			products.append([name, price])
			#記得要空格
		print(products)
	return products

	

	#輸入商品名稱

def user_input(products):
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
		price = int(price)
		products.append(p)
		#又可以直接簡潔成
		#products.append([name, price])
	print('總共有', len(products), '項')
	print(products)
	#print(products[0][1])
	#這樣寫不好 依序把所有產品都列出來可這樣寫

	return products

def print_products(products):
	for p in products:
	#記得要寫對框框！！ p[]!!	
		print(p[0], '的價格是:',p[1] )
	#輸出檔案 w

def write_file(filename, products):
	with open(filename, 'w', encoding = 'utf-8') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')
	#每次寫是會更新的喔！！


def main():
	filename = 'products_list.csv'
	if os.path.isfile(filename): #檢察檔案在不在
			print('YES!!!!我的檔案找到啦')
			products = read_file(filename)
	else:	
			print('找不到檔案啦...')

	products = user_input(products)
	print_products(products)
	write_file('products_list.csv', products)


main()

