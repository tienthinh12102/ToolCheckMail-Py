# r: chỉ đọc
# a: chỉ ghi.ko xóa file cũ
# w: chỉ ghi.xóa hết ghi lại
# r+ đọc và ghi

#mở file
file=open('data/test.txt','w', encoding='utf-8')
file.write('thinh-samaá')
file.write('\n thinh-samaá')
