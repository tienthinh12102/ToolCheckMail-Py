from requests import session
import re #thư viện tìm kiếm
s= session()
email='thinh1202'

def checkmail(s,email):
	DL= s.get('https://signup.live.com/signup?username='+email+'@hotmail.com&lic=1')
	kq=re.search("isAvailable",DL.text)
	if kq==None:
		print('email live')
	else:
		open('data/mailDie.txt','a').write(email+'@hotmail.com'+'\n')
		print('email die: '+ email)

# checkmail(s,email)
for x in range(1,10):
	newEmail = email+str(x)
	checkmail(s,newEmail)