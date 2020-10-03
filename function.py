#function 函式/功能

#function是用來收納程式碼的
#他是個功能
#def 函式名稱():
#	內容


#level1 
def washermashine():
	print('請按開始')
	print('按強度')
	print('洗的種類')

washermashine()
print('\n')

#level2 多參數parameter
def wash(dry):
	print('請按開始')
	print('按強度')
	print('洗的種類')
	if dry:
		print('烘乾')
		print('需要十分鐘喔')

wash(True)
wash(False)
print('\n')

#level3 多個參數parameter
'''def wash(dry, water):
	print('加水', water, '分滿')
	if dry:
		print('烘乾')
wash(True, 10)
wash(False, 15)'''

#level4
def wash(dry=False, water=8):
	print('加水', water, '分滿')
	print('加洗衣精')
	print('旋轉')
	if dry:
		print('烘乾')

wash(water=1)



