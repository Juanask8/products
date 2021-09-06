import os  # operating system(作業系統)

# 讀取檔案
products = []
if os.path.isfile('products.csv'):   # 檢查檔案在不在
	print('yeah! 找到檔案了')
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue  # 跳到下一回繼續
			name, price = line.strip().split(',')   # strip: 去掉換行符號 split: 切割
			products.append([name, price])
	print(products)
else:
	print('找不到檔案....')


# 讓使用者輸入
products = []
while True:
	name = input('請輸入商品名稱:')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	p = [name, price]
	products.append(p)
print(products)
print(products[1][0])

# 印出所有購買紀錄
for product in products:
	print(product[0], '的價格是', product[1])

#寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:  # with 檔案讀取
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n') # ,做分隔 \n換行


