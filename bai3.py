# for x in range(1,10):
# 	print(x)

#đọc file test.txt
file=open('data/test.txt','r').read()
#chia thành dòng
mang = file.split('\n')
#mở tạo file file_cookie
file_cookie = open('data/file_cookie.txt','w')
#vòng lập biến mảng
for x in mang:
	#print(x.split(',')[2])
	file_cookie.write(x.split(',')[2]+"\n")