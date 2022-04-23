
# No other modules apart from 'socket', 'BeautifulSoup', 'requests' and 'datetime'
# need to be imported as they aren't required to solve the assignment

# Import required module/s
import socket
from bs4 import BeautifulSoup
import requests
import datetime


# Define constants for IP and Port address of Server
# NOTE: DO NOT modify the values of these two constants
HOST = '127.0.0.1'
PORT = 24680


def fetchWebsiteData(url_website):
	"""Fetches rows of tabular data from given URL of a website with data excluding table headers.

	Parameters
	----------
	url_website : str
		URL of a website

	Returns
	-------
	bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	"""
	
	web_page_data = ''

	##############	ADD YOUR CODE HERE	##############
	
	

	##################################################

	return web_page_data


def fetchVaccineDoses(web_page_data):
	"""Fetch the Vaccine Doses available from the Web-page data and provide Options to select the respective Dose.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers

	Returns
	-------
	dict
		Dictionary with the Doses available and Options to select, with Key as 'Option' and Value as 'Command'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchVaccineDoses(web_page_data))
	{'1': 'Dose 1', '2': 'Dose 2'}
	"""

	vaccine_doses_dict = {}

	##############	ADD YOUR CODE HERE	##############
	
	

	##################################################

	return vaccine_doses_dict


def fetchAgeGroup(web_page_data, dose):
	"""Fetch the Age Groups for whom Vaccination is available from the Web-page data for a given Dose
	and provide Options to select the respective Age Group.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the Age Groups (for whom Vaccination is available for a given Dose) and Options to select,
		with Key as 'Option' and Value as 'Command'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchAgeGroup(web_page_data, '1'))
	{'1': '18+', '2': '45+'}
	>>> print(fetchAgeGroup(web_page_data, '2'))
	{'1': '18+', '2': '45+'}
	"""

	age_group_dict = {}

	##############	ADD YOUR CODE HERE	##############
	
	

	##################################################

	return age_group_dict


def fetchStates(web_page_data, age_group, dose):
	"""Fetch the States where Vaccination is available from the Web-page data for a given Dose and Age Group
	and provide Options to select the respective State.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	age_group : str
		Age Group available for Vaccination and its availability in the States
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the States (where the Vaccination is available for a given Dose, Age Group) and Options to select,
		with Key as 'Option' and Value as 'Command'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchStates(web_page_data, '18+', '1'))
	{
		'1': 'Andhra Pradesh', '2': 'Arunachal Pradesh', '3': 'Bihar', '4': 'Chandigarh', '5': 'Delhi', '6': 'Goa',
		'7': 'Gujarat', '8': 'Harayana', '9': 'Himachal Pradesh', '10': 'Jammu and Kashmir', '11': 'Kerala', '12': 'Telangana'
	}
	"""

	states_dict = {}

	##############	ADD YOUR CODE HERE	##############
	
	

	##################################################

	return states_dict


def fetchDistricts(web_page_data, state, age_group, dose):
	"""Fetch the District where Vaccination is available from the Web-page data for a given State, Dose and Age Group
	and provide Options to select the respective District.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	state : str
		State where Vaccination is available for a given Dose and Age Group
	age_group : str
		Age Group available for Vaccination and its availability in the States
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the Districts (where the Vaccination is available for a given State, Dose, Age Group) and Options to select,
		with Key as 'Option' and Value as 'Command'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchDistricts(web_page_data, 'Ladakh', '18+', '2'))
	{
		'1': 'Kargil', '2': 'Leh'
	}
	"""

	districts_dict = {}

	##############	ADD YOUR CODE HERE	##############
	
	

	##################################################

	return districts_dict


def fetchHospitalVaccineNames(web_page_data, district, state, age_group, dose):
	"""Fetch the Hospital and the Vaccine Names from the Web-page data available for a given District, State, Dose and Age Group
	and provide Options to select the respective Hospital and Vaccine Name.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	district : str
		District where Vaccination is available for a given State, Dose and Age Group
	state : str
		State where Vaccination is available for a given Dose and Age Group
	age_group : str
		Age Group available for Vaccination and its availability in the States
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the Hosptial and Vaccine Names (where the Vaccination is available for a given District, State, Dose, Age Group)
		and Options to select, with Key as 'Option' and Value as another dictionary having Key as 'Hospital Name' and Value as 'Vaccine Name'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchHospitalVaccineNames(web_page_data, 'Kargil', 'Ladakh', '18+', '2'))
	{
		'1': {
				'MedStar Hospital Center': 'Covaxin'
			}
	}
	>>> print(fetchHospitalVaccineNames(web_page_data, 'South Goa', 'Goa', '45+', '2'))
	{
		'1': {
				'Eden Clinic': 'Covishield'
			}
	}
	"""
	
	hospital_vaccine_names_dict = {}

	##############	ADD YOUR CODE HERE	##############
	
	

	##################################################

	return hospital_vaccine_names_dict


def fetchVaccineSlots(web_page_data, hospital_name, district, state, age_group, dose):
	"""Fetch the Dates and Slots available on those dates from the Web-page data available for a given Hospital Name, District, State, Dose and Age Group
	and provide Options to select the respective Date and available Slots.

	Parameters
	----------
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	hospital_name : str
		Name of Hospital where Vaccination is available for given District, State, Dose and Age Group
	district : str
		District where Vaccination is available for a given State, Dose and Age Group
	state : str
		State where Vaccination is available for a given Dose and Age Group
	age_group : str
		Age Group available for Vaccination and its availability in the States
	dose : str
		Dose available for Vaccination and its availability for the Age Groups

	Returns
	-------
	dict
		Dictionary with the Dates and Slots available on those dates (where the Vaccination is available for a given Hospital Name,
		District, State, Dose, Age Group) and Options to select, with Key as 'Option' and Value as another dictionary having
		Key as 'Date' and Value as 'Available Slots'
	
	Example
	-------
	>>> url_website = "https://www.mooc.e-yantra.org/task-spec/fetch-mock-covidpage"
	>>> web_page_data = fetchWebsiteData(url_website)
	>>> print(fetchVaccineSlots(web_page_data, 'MedStar Hospital Center', 'Kargil', 'Ladakh', '18+', '2'))
	{
		'1': {'May 15': '0'}, '2': {'May 16': '81'}, '3': {'May 17': '109'}, '4': {'May 18': '78'},
		'5': {'May 19': '89'}, '6': {'May 20': '57'}, '7': {'May 21': '77'}
	}
	>>> print(fetchVaccineSlots(web_page_data, 'Eden Clinic', 'South Goa', 'Goa', '45+', '2'))
	{
		'1': {'May 15': '0'}, '2': {'May 16': '137'}, '3': {'May 17': '50'}, '4': {'May 18': '78'},
		'5': {'May 19': '145'}, '6': {'May 20': '64'}, '7': {'May 21': '57'}
	}
	"""

	vaccine_slots = {}

	##############	ADD YOUR CODE HERE	##############
	
	

	##################################################

	return vaccine_slots


def openConnection():
	"""Opens a socket connection on the HOST with the PORT address.

	Returns
	-------
	socket
		Object of socket class for the Client connected to Server and communicate further with it
	tuple
		IP and Port address of the Client connected to Server
	"""

	client_socket = None
	client_addr = None

	##############	ADD YOUR CODE HERE	##############
	
	

	##################################################
	
	return client_socket, client_addr


def startCommunication(client_conn, client_addr, web_page_data):
	"""Starts the communication channel with the connected Client for scheduling an Appointment for Vaccination.

	Parameters
	----------
	client_conn : socket
		Object of socket class for the Client connected to Server and communicate further with it
	client_addr : tuple
		IP and Port address of the Client connected to Server
	web_page_data : bs4.element.ResultSet
		All rows of Tabular data fetched from a website excluding the table headers
	"""

	##############	ADD YOUR CODE HERE	##############
	
	

	##################################################


def stopCommunication(client_conn):
	"""Stops or Closes the communication channel of the Client with a message.

	Parameters
	----------
	client_conn : socket
		Object of socket class for the Client connected to Server and communicate further with it
	"""

	##############	ADD YOUR CODE HERE	##############
	
	

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
