import socket
from bs4 import BeautifulSoup
import requests
import datetime

HOST = '127.0.0.1'
PORT = 24680

def fetchWebsiteData(url_website):
	web_page_data = ''
	##############	ADD YOUR CODE HERE	##############
	soup=BeautifulSoup(requests.get(url_website).content,'html.parser')
	web_page_data=soup.find_all('tbody')
	for i in web_page_data:
		a=i.find_all("tr")
	web_page_data=a
	#print(web_page_data)
	##################################################
	return web_page_data

def fetchVaccineDoses(web_page_data):
	vaccine_doses_dict = {}
	##############	ADD YOUR CODE HERE	##############
	doses=[]
	for i in web_page_data:
		for item in (i.find_all('td',class_='dose_num')):
			if item.text not in doses:
				doses.append(item.text)
	for i in range(len(doses)):
		vaccine_doses_dict[doses[i]]="Dose "+str(i+1)
	##################################################
	return vaccine_doses_dict

def fetchAgeGroup(web_page_data, dose):
	age_group_dict = {}
	##############	ADD YOUR CODE HERE	##############
	age=[]
	for i in web_page_data:
		a=(i.find_all('td',class_='age'))
		b=(i.find_all('td', class_='dose_num'))
		for j in range(len(b)):
			if (b[j].text)==dose:
				if a[j].text not in age:
					age.append(a[j].text)
	for i in range(len(age)):
		age[i]=age[i].replace('+','')
		age[i]=int(age[i])
	age.sort()
	for i in range(len(age)):
		age[i]
	for i in range(len(age)):
		age_group_dict[str(i+1)]=str(age[i])+"+"
	##################################################
	return age_group_dict

def fetchStates(web_page_data, age_group, dose):
	states_dict = {}
	##############	ADD YOUR CODE HERE	##############
	states=[]
	for i in web_page_data:
		state=(i.find_all('td',class_='state_name'))
		dosenum=(i.find_all('td',class_='dose_num'))
		age=(i.find_all('td',class_='age'))
		for j in range(len(age)):
			if((dosenum[j].text)==dose and (age[j].text)==age_group):
				if state[j].text not in states:
					states.append(state[j].text)
	states.sort()
	for i in range(len(states)):
		states_dict[str(i+1)]=states[i]
	##################################################
	return states_dict

def fetchDistricts(web_page_data, state, age_group, dose):
	districts_dict = {}
	##############	ADD YOUR CODE HERE	##############
	districts=[]
	for i in web_page_data:
		staterange=(i.find_all('td', class_='state_name'))
		dosenum=(i.find_all('td', class_='dose_num'))
		age=(i.find_all('td',class_='age'))
		district=(i.find_all('td',class_='district_name'))
		for j in range(len(age)):
			if((dosenum[j].text)==dose and (age[j].text)==age_group and (staterange[j].text)==state):
				districts.append(district[j].text)
	districts.sort()
	for i in range(len(districts)):
		districts_dict[str(i+1)]=districts[i]
	##################################################
	return districts_dict

def fetchHospitalVaccineNames(web_page_data, district, state, age_group, dose):
	hospital_vaccine_names_dict = {}
	##############	ADD YOUR CODE HERE	##############
	hnames=[]
	vaccine=[]
	for i in web_page_data:
		districts=(i.find_all('td',class_='district_name'))
		dosenum=(i.find_all('td',class_='dose_num'))
		age=(i.find_all('td',class_='age'))
		staterange=(i.find_all('td',class_='state_name'))
		hnamerange=(i.find_all('td',class_='hospital_name'))
		vaccinename=(i.find_all('td',class_='vaccine_name'))
		for j in range(len(age)):
			if((districts[j].text)==district and (dosenum[j].text)==dose and (staterange[j].text)==state and (age[j].text)==age_group):
				hnames.append(hnamerange[j].text)
				vaccine.append(vaccinename[j].text)
	hnames.sort()
	vaccine.sort()
	vaccinenamedict={}
	for i in range(len(hnames)):
		for j in range(len(vaccine)):
			vaccinenamedict[hnames[i]]=vaccine[j]
		hospital_vaccine_names_dict[str(i+1)]=vaccinenamedict
	##################################################
	return hospital_vaccine_names_dict

def fetchVaccineSlots(web_page_data, hospital_name, district, state, age_group, dose):
	vaccine_slots = {}
	##############	ADD YOUR CODE HERE	##############
	for i in web_page_data:
		dosenum=(i.find_all('td',class_='dose_num'))
		age=(i.find_all('td',class_='age'))
		statesrange=(i.find_all('td',class_='state_name'))
		hname=(i.find_all('td',class_='hospital_name'))
		districts=(i.find_all('td',class_='district_name'))
		may15=(i.find_all('td',class_='may_15'))
		may16=(i.find_all('td',class_='may_16'))
		may17=(i.find_all('td',class_='may_17'))
		may18=(i.find_all('td',class_='may_18'))
		may19=(i.find_all('td',class_='may_19'))
		may20=(i.find_all('td',class_='may_20'))
		may21=(i.find_all('td',class_='may_21'))
		for j in range(len(dosenum)):
			if((dosenum[j].text)==dose and (age[j].text)==age_group and (statesrange[j].text)==state and (hname[j].text)==hospital_name and (districts[j]).text==district):
				vaccine_slots["1"]={'May 15':may15[j].text}
				vaccine_slots["2"]={'May 16':may16[j].text}
				vaccine_slots["3"]={'May 17':may17[j].text}
				vaccine_slots["4"]={'May 18':may18[j].text}
				vaccine_slots["5"]={'May 19':may19[j].text}
				vaccine_slots["6"]={'May 20':may20[j].text}
				vaccine_slots["7"]={'May 21':may21[j].text}
	##################################################
	return vaccine_slots

def openConnection():
	client_socket = None
	client_addr = None
	############## ADD YOUR CODE HERE ##############
	server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server.bind((HOST,PORT))
	server.listen(1)
	while True:
		client_socket, client_addr=server.accept()
		break
	######################################################
	return client_socket, client_addr

def startCommunication(client_conn, client_addr, web_page_data):
	##############	ADD YOUR CODE HERE ##############
	def welcome():
		print("Client is connected at: ",client_addr)
		client_conn.sendall(bytes("============================\n"+'#'+" Welcome to CoWIN ChatBot "+'#'+"\n============================\n",'utf-8'))
		client_conn.sendall(bytes('\nSchedule an Appointment for Vaccination:','utf-8'))
		choosedose(3)
	def choosedose(remtries):
		x=0
		vaccinedoses=fetchVaccineDoses(web_page_data)
		client_conn.sendall(bytes("\n>>> Select the Dose of Vaccination:\n"+str(vaccinedoses)+"\n",'utf-8'))
		dosenum=client_conn.recv(1024).decode()
		if dosenum =="q" or dosenum =="Q":
			stopCommunication(client_conn,1)
		elif dosenum=='b' or dosenum=='B':
			choosedose(remtries)
		elif dosenum=="1":
			x=1
			client_conn.sendall(bytes("\n<<< Dose selected: "+str(dosenum)+"\n",'utf-8'))
			print("Dose selected: ",dosenum)
			chooseage(remtries,dosenum)
		elif dosenum=="2":
			x=1
			client_conn.sendall(bytes("\n<<< Dose selected: "+str(dosenum)+"\n",'utf-8'))
			print("Dose selected: ",dosenum)
			seconddose(dosenum,remtries)
		if(x==0):
			if remtries!=0:
				invalidinput(remtries)
				remtries=remtries-1
				if remtries!=0:
					choosedose(remtries)
				else:
					stopCommunication(client_conn,0)
	def seconddose(dosenum,remtries):
		client_conn.sendall(bytes("\n>>> Provide the date of First Vaccination Dose (DD/MM/YYYY), for e.g. 12/5/2021",'utf-8'))	
		date=client_conn.recv(1024).decode()
		if date=='q' or date=='Q':
			stopCommunication(client_conn,1)
		elif date=='b' or date=='B':
			choosedose(remtries)
		isValidDate=True
		dateinstring=date
		refdate=datetime.datetime.strptime("14/08/2000","%d/%m/%Y")
		today=datetime.datetime.today().strftime("%d/%m/%Y")
		today=datetime.datetime.strptime(today,"%d/%m/%Y")
		try:
			date=datetime.datetime.strptime(date,"%d/%m/%Y")
		except ValueError:
			isValidDate=False
		if(isValidDate):
			diff1=date-refdate
			diff2=today-refdate
			diff3=today-date
			diff3=str(int((diff3.days)/7))
			if diff1>diff2:
				client_conn.sendall(bytes("\n<<< Invalid Date provided of First Vaccination Dose: "+dateinstring,'utf-8'))
				seconddose(dosenum,remtries)
			else:
				client_conn.sendall(bytes("\n<<< Date of First Vaccination Dose provided: "+dateinstring,"utf-8"))
				client_conn.sendall(bytes("\n<<< Number of weeks from today: "+diff3,"utf-8"))
				if int(diff3)<4:
					client_conn.sendall(bytes("\n<<< You are not eligible right now for 2nd Vaccination Dose! Try after "+str(4-int(diff3))+" weeks",'utf-8'))
					stopCommunication(client_conn,0)
				elif int(diff3)>8:
					client_conn.sendall(bytes("\n<<< You have been late in scheduling your 2nd Vaccination Dose by "+str(int(diff3)-8)+" weeks",'utf-8'))
					chooseage(remtries,dosenum)
				else:
					client_conn.sendall(bytes("\n<<< You are eligible for 2nd Vaccination Dose and are in the right time-frame to take it.",'utf-8'))
					chooseage(remtries,dosenum)
		else:
			client_conn.sendall(bytes("\n<<< Invalid Date provided of First Vaccination Dose: "+dateinstring,'utf-8'))
			seconddose(dosenum,remtries)
	def chooseage(remtries,dosenum):
		x=0
		agedict=fetchAgeGroup(web_page_data,dosenum)
		client_conn.sendall(bytes("\n>>> Select the Age Group: \n"+(str(agedict))+"\n",'utf-8'))
		agekeys=[]
		for i in agedict.keys():
			agekeys.append(str(i))
		age=client_conn.recv(1024).decode()
		if age=='b' or age=='B':
			choosedose(remtries)
		elif age=='q' or age=='Q':
			stopCommunication(client_conn,1)
		for i in range(len(agekeys)):
			if age==str(i+1):
				x=1
				client_conn.sendall(bytes("\n<<< Selected Age Group: "+str(agedict[age])+"\n",'utf-8'))
				print("Age Group selected: ",agedict[age])
				choosestate(remtries,agedict[age],dosenum)
		if(x==0):
			if remtries!=0:
				invalidinput(remtries)
				remtries=remtries-1
				if remtries!=0:
					agedict.clear()
					chooseage(remtries,dosenum)
				else:
					stopCommunication(client_conn,0)
	def choosestate(remtries,age,dosenum):
		x=0
		client_conn.sendall(bytes(">>> Select the State: \n"+str(fetchStates(web_page_data,age,dosenum))+"\n",'utf-8'))
		statedict=fetchStates(web_page_data,age,dosenum)
		state=client_conn.recv(1024).decode()
		if state=='b' or state=='B':
			chooseage(remtries,dosenum)
		elif state=='q' or state=='Q':
			stopCommunication(client_conn,1)
		statekeys=[]
		for i in statedict.keys():
			statekeys.append(i)
		for i in range(len(statekeys)):
			if state in statekeys:
				x=1
				client_conn.sendall(bytes("\n<<< Selected State: "+str(statedict[state])+"\n",'utf-8'))
				print("State selected: ",statedict[state])
				choosedistrict(remtries,statedict[state],age,dosenum)
		if(x==0):
			if remtries!=0:
				invalidinput(remtries)
				remtries=remtries-1
				if remtries!=0:
					statedict.clear()
					choosestate(remtries,age,dosenum)
			else:
				stopCommunication(client_conn,0)
	def choosedistrict(remtries,state,age,dosenum):
		x=0
		client_conn.sendall(bytes(">>> Select the District: \n"+str(fetchDistricts(web_page_data,state,age,dosenum))+"\n",'utf-8'))
		districtdict=fetchDistricts(web_page_data,state,age,dosenum)
		district=client_conn.recv(1024).decode()
		if district=='b' or district=='B':
			choosestate(remtries,age,dosenum)
		elif district=='q' or district=='Q':
			stopCommunication(client_conn,1)
		districtkeys=[]
		for i in districtdict.keys():
			districtkeys.append(i)
		for i in range(len(districtkeys)):
			if district in districtkeys:
				x=1
				client_conn.sendall(bytes("\n<<< Selected District: "+str(districtdict[district])+"\n",'utf-8'))
				print("District selected: ",districtdict[district])
				choosecenter(remtries,districtdict[district],state,age,dosenum)
		if(x==0):
			if remtries!=0:
				invalidinput(remtries)
				remtreis=remtries-1
				if remtries!=0:
					districtdict.clear()
					choosedistrict(remtries,state,age,dosenum)
			else:
				stopCommunication(client_conn,0)
	def choosecenter(remtries,district,state,age,dosenum):
		x=0
		client_conn.sendall(bytes(">>> Select the Vaccination Center Name: \n"+str(fetchHospitalVaccineNames(web_page_data, district, state,age,dosenum))+"\n",'utf-8'))
		hnamedict=fetchHospitalVaccineNames(web_page_data, district, state, age, dosenum)
		hname=client_conn.recv(1024).decode()
		if hname=='b' or hname=='B':
			choosedistrict(remtries,state,age,dosenum)
		elif hname=='q' or hname=='Q':
			stopCommunication(client_conn,1)
		hnamekeys=[]
		for i in hnamedict.keys():
			hnamekeys.append(i)
		for i in range(len(hnamekeys)):
			if hname in hnamekeys:
				x=1
				hnameandvaccine=hnamedict[hname]
				for i in hnameandvaccine.keys():
					hospital=i
				client_conn.sendall(bytes("\n<<< Selected Vaccination Center: "+hospital+"\n",'utf-8'))
				print("Hospital selected: ",hospital)
				chooseslot(remtries,hospital,district,state,age,dosenum)
		if(x==0):
			if remtries!=0:
				invalidinput(remtries)
				remtries=remtries-1
				if remtries!=0:
					choosecenter(remtries,district,state,age,dosenum)
				else:
					stopCommunication(client_conn,0)
	def chooseslot(remtries,hospital,district,state,age,dosenum):
		x=0
		slotsdict=fetchVaccineSlots(web_page_data,hospital,district,state,age,dosenum)
		client_conn.sendall(bytes(">>> Select one of the available slots to schedule the Appointment: \n"+str(slotsdict)+"\n",'utf-8'))
		slot=client_conn.recv(1024).decode()
		if slot=='b' or slot=='B':
			choosecenter(remtries,district,state,age,dosenum)
		if slot=='q' or slot=='Q':
			stopCommunication(client_conn,1)
		slotkeys=[]
		flag=0
		for i in slotsdict.keys():
			slotkeys.append(str(i))
		for i in range(len(slotkeys)):
			if slot in slotkeys:
				x=1
				for i in slotsdict[(slot)]:
					if slotsdict[(slot)][i]=="0":
						client_conn.sendall(bytes("\n<<< Selected Vaccination Appointment Date: "+i,'utf-8'))
						client_conn.sendall(bytes("\n"+"<<< Available Slots on the selected Date: "+slotsdict[(slot)][i],'utf-8'))
						client_conn.sendall(bytes("\n<<< Selected Appointment Date has no available slots, select another date!\n",'utf-8'))
						print("Vaccination Date selected: ",i)
						print("Available Slots on that date: ",slotsdict[slot][i])
						chooseslot(remtries,hospital,district,state,age,dosenum)
				dateandslot=slotsdict[(slot)]
				for i in dateandslot.keys():
					date=i
				for i in dateandslot.values():	
					slotavailable=i
				client_conn.sendall(bytes("\n<<< Selected Vaccination Appointment Date: "+date,'utf-8'))
				client_conn.sendall(bytes("\n"+"<<< Available Slots on the selected Date: "+slotavailable,'utf-8'))
				client_conn.sendall(bytes("\n<<< Your appointment is scheduled. Make sure to carry ID Proof while you visit Vaccination Center!\n",'utf-8'))
				print("Vaccination Date selected: ",date)
				print("Available Slots on that date: ",slotavailable)
				stopCommunication(client_conn,0)
		if (x==0):
			if remtries!=0:
				invalidinput(remtries)
				remtries=remtries-1
				if remtries!=0:
					chooseslot(remtries,hospital,district,state,age,dosenum)
				else:
					stopCommunication(client_conn,0)
	def invalidinput(remtries):
		if remtries==3:
			a=1
		elif remtries==2:
			a=2
		else:
			a=3
		print("Invalid input detected %s time(s)!" %(a))
		client_conn.sendall(bytes(("\n<<< Invalid input provided %s time(s)! Try again\n" %(a)),'utf-8'))
		if a==3:
			print("Notifying the client and closing the connection!")
			stopCommunication(client_conn,0)
	welcome()
	##################################################

def stopCommunication(client_conn,flag):
	############## ADD YOUR CODE HERE ##############
	if flag==1:
		print("Client wants to quit!")
		print("Saying bye to the client and closing the connenction!")
	client_conn.sendall(bytes("<<< See ya! Visit again :)",'utf-8'))
	exit()
	##################################################

################# ADD UTILITY FUNCTIONS HERE #################
## You can define any utility functions for your code.      ##
## Please add proper comments to ensure that your code is   ##
## readable and easy to understand.                         ##
##############################################################

##############################################################

if __name__ == '__main__':
	"""Main function, code begins here
	"""
	url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	web_page_data = fetchWebsiteData(url_website)
	client_conn, client_addr = openConnection()
	startCommunication(client_conn, client_addr, web_page_data)
