
# No other modules apart from 'bs4' and 'requests' need to be imported
# as they aren't required to solve the assignment

# Import required module/s
from bs4 import BeautifulSoup
import requests

def getUserName(url_website, full_name):
	username = ""
	##############	ADD YOUR CODE HERE	##############
	soup=BeautifulSoup(requests.get(url_website).content, 'html.parser')
	soup=soup.prettify()
	soup1=BeautifulSoup(soup,'html5lib')
	#print(type(soup1))
	'''
	with open('output.txt','w') as file:
		file.write(str(soup.prettify()))
	with open('output.txt','r') as html:
		contents=html.read()
		soup=BeautifulSoup(contents,'html5lib')
	'''
	
	with open('names.txt','w') as text:
		for i in soup1.find_all('tr'):
			text.write(i.text)
	with open('names.txt','r') as text, open('noemptylines.txt','w') as result:
		for line in text:
			if line.strip():
				result.write(line)
	with open('noreplines.txt','w') as output, open('noemptylines.txt','r') as input:
		lines_seen_so_far=set()
		for line in input:
			if line not in lines_seen_so_far:
				output.write(line)
				lines_seen_so_far.add(line)
	output.close()
	input.close()
	final=full_name.replace(".","")
	final=final.replace(" ","")
	final=final.lower()
	with open('noreplines.txt','r') as input:
		for line in input:
			if final in line:
				username=line
	username=username.replace(' ','')
	username=username.replace('\n','')
	#print(username)
	##################################################
	return username

if __name__ == "__main__":
	url_website = "https://www.cse.iitb.ac.in/archive/page222?batch=MTech1"
	full_name = "A.V.S BHARADWAJ"
	username = getUserName(url_website, full_name)
	print("The username of " + full_name + " is: " + username)
