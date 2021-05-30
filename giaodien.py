# dong goi : pip install pyinstaller
# xuất file exe : pyinstaller --onefile --windowed frontend.py

from tkinter import * #thư viên giao diện
from requests import session
import tkinter.messagebox
import re #thư viện tìm kiếm
s= session()
window = Tk() # tạo đối tượng 

window.wm_title("Check Mail Die 2021")
my_label = Label(window, text = 'Nhập hostmail: ')
my_label.config(font=("Helvetica", 10)) # font và size chữ
my_label.grid(row = 0, column = 0)

hotmail = Entry(window) # tạo textBox
hotmail.grid(row = 0, column = 1)

def checkmail(s,email): #hàm check mail die
	DL= s.get('https://signup.live.com/signup?username='+email+'@hotmail.com&lic=1')
	kq= re.search("isAvailable",DL.text)
	if kq==None:
		print('email live')
	else:
		open('mailDie.txt','a').write(email+'@hotmail.com'+'\n')
		print('email die: '+ email)
	
def Run():
	for x in range(1,101):
		email= hotmail.get() #lấy ra giá trị email
		newEmail = email+str(x)
		checkmail(s,newEmail)
	tkinter.messagebox.showinfo('Window Title','Đã Xong')

btn=Button(window,text="OK", width=10, height=2, command=Run) #Tạo btn
btn.grid(row = 0, column = 2)

window.mainloop() # để phần mềm lun chạy