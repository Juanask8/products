# 讀取檔案
products = []
with open('products.csv', 'r', encoding='utf-8') as f:
	for line in f:
		if '商品,價格' in line:
			continue  # 跳到下一回繼續
		name, price = line.strip().split(',')   # strip: 去掉換行符號 split: 切割
		products.append([name, price])
print(products)

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


