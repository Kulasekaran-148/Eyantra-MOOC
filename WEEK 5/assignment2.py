
# No other modules apart from 'bs4' and 'requests' need to be imported
# as they aren't required to solve the assignment
# Import required module/s
from bs4 import BeautifulSoup
import requests


def getUserName(url_website, full_name):
	username = "Full Name does not exist on website"
	##############	ADD YOUR CODE HERE	#############
	soup=BeautifulSoup(requests.get(url_website).content,'html5lib')
	for i in soup.find_all('tr', class_=['row1','row2']): 
		data=str(i.td.table.tbody.tr.td.a.b.text)
		if full_name==data:
			username=(i.td.table.tbody.tr.select("td")[1].b.text)
			username=username.replace("cseiitbacin","")
			break
	##################################################
	return username


if __name__ == "__main__":
	url_website = "https://www.cse.iitb.ac.in/archive/page222?batch=MTech1"
	full_name = "A.V.S BHARADWAJ"
	username = getUserName(url_website, full_name)
	print("The username of " + full_name + " is: " + username)
