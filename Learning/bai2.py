#đọc
file=open('data/test.txt','r').read()
print(file.split('\n')[2].split(',')[1])