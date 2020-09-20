#Q1:使用 while 迴圈顯示 100 個你好，並在顯示第 100 個後，使用 print 顯示「我說完了啦」並停止 
i = 1
i = input('請輸入100:')
i = int(i)

while i <= 100:
    i = i + 1
    print('你好')
print('我說完了啦')