#規定玩家只能輸入指定的內容

while True:
	mode = input('請輸入遊戲模式:')
	if mode =='q': #quit
		break
	elif mode =='1':
		print('啟動遊戲模式1:')
	elif mode =='2':
		print('啟動遊戲模式2:')
	else:
		print('只能輸入1/2/q:')
