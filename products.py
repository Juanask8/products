import os  # operating system(作業系統)

# 讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if '商品,價格' in line:
				continue  # 跳到下一回繼續
			name, price = line.strip().split(',')   # strip: 去掉換行符號 split: 切割
			products.append([name, price])
		print(products)
	return products

# 讓使用者輸入
def user_input(products):
	while True:
		name = input('請輸入商品名稱:')
		if name == 'q':
			break
		price = input('請輸入商品價格:')
		p = [name, price]
		products.append(p)
	print(products)
	return(products)  # append更新過

# 印出所有購買紀錄
def print_products(products):
	for p in products:
		print(p[0], '的價格是', p[1])

#寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:  # with 檔案讀取
			f.write('商品,價格\n')
			for p in products:
				f.write(p[0] + ',' + p[1] + '\n') # ,做分隔 \n換行

def main():
	filename = 'products.csv'
	if os.path.isfile(filename):   # 檢查檔案在不在
		print('yeah! 找到檔案了')
		products = read_file(filename)
	else:
		print('找不到檔案....')

	products = user_input(products)
	print_products(products)
	write_file('products.csv', products)

main()