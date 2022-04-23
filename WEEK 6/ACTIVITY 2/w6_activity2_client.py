
# Import required module/s
import socket
import re
# NOTE: You are free to use any module(s) required for better representation of the data received from the Server.
# NOTE: DO NOT modify the connectToServer() and the 'if' conditions in main() function.
# Although you can make modifications to main() where you wish to call formatRecvdData() function.

def connectToServer(HOST, PORT):

	server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	server_socket.connect ((HOST, PORT))
	return server_socket

def formatRecvdData(data_recvd):
	##############	ADD YOUR CODE HERE	##############
	i=data_recvd

	# OPTIONS  #
	for k in range(100):
		a=("'{}'".format(k))
		a=str(a)
		i=i.replace(a,'\x1b[1;31;38m'+a+'\x1b[0m')
	
	# WELCOME MESSAGE #
	#i=i.replace("Welcome to CoWIN ChatBot",'\x1b[5;32;38m'+'Welcome to CoWIN ChatBot'+'\x1b[0m')
	i=i.replace("Welcome to CoWIN ChatBot",'\x1b[1;32;38m'+'Welcome to CoWIN ChatBot'+'\x1b[0m')
	#i=i.replace("Welcome to CoWIN ChatBot",'\x1b[3;32;38m'+'Welcome to CoWIN ChatBot'+'\x1b[0m')
	i=i.replace("Schedule an Appointment for Vaccination:",'\x1b[1;34;38m'+'Schedule an Appointment for Vaccination:'+'\x1b[0m')
	i=i.replace("Schedule an Appointment for Vaccination:",'\x1b[4;34;38m'+'Schedule an Appointment for Vaccination:'+'\x1b[0m')
	i=i.replace("=",'\x1b[1;31;38m'+'='+'\x1b[0m')

	# DOSE SELECTION #
	i=i.replace("Select the Dose of Vaccination:",'\x1b[1;33;38m'+'Select the Dose of Vaccination'+'\x1b[0m')
	i=i.replace("Dose selected:",'\x1b[1;36;38m'+'Dose selected:'+'\x1b[0m') 
	i=i.replace("Dose selected:",'\x1b[3;36;38m'+'Dose selected:'+'\x1b[0m')

	# DATE SELECTION #
	i=i.replace("Provide the date of First Vaccination Dose",'\x1b[1;33;38m'+'Provide the date of First Vaccination Dose'+'\x1b[0m')
	
	i=i.replace("(DD/MM/YYYY)",'\x1b[1;36;38m'+'(DD/MM/YYYY)'+'\x1b[0m')
	i=i.replace("Date of First Vaccination Dose provided:",'\x1b[1;36;38m'+'Date of First Vaccination Dose provided:'+'\x1b[0m')
	i=i.replace("Date of First Vaccination Dose provided:",'\x1b[3;36;38m'+'Date of First Vaccination Dose provided:'+'\x1b[0m')
	i=i.replace("Number of weeks from today:",'\x1b[1;36;38m'+'Number of weeks from today:'+'\x1b[0m')
	
	# ELIGIBLE CANDIDATE #
	a="for 2nd Vaccination Dose and are in the right time-frame to take it."
	i=i.replace("You are eligible",'\x1b[1;32;38m'+'You are eligible'+'\x1b[0m')
	i=i.replace(a,'\x1b[1;36;38m'+a+'\x1b[0m')
	
	# LATE CANDITATE #
	#i=i.replace("You have been late in scheduling your 2nd Vaccination Dose by",'\x1b[5;36;40m'+'You have been late in scheduling your 2nd Vaccination Dose by'+'\x1b[0m')
	i=i.replace("You have been late in scheduling your 2nd Vaccination Dose by",'\x1b[1;36;38m'+'You have been late in scheduling your 2nd Vaccination Dose by:'+'\x1b[0m')
	
	# NON-ELIGIBLE CANDITATE #
	i=i.replace("You are not eligible right now for 2nd Vaccination Dose!",'\x1b[6;31;38m'+'You are not eligible right now for 2nd Vaccination Dose!'+'\x1b[0m')
	i=i.replace("You are not eligible right now for 2nd Vaccination Dose!",'\x1b[1;31;38m'+'You are not eligible right now for 2nd Vaccination Dose!'+'\x1b[0m')
	
	# INVALID FIRST VACCINATION DATE #
	#i=i.replace("Invalid Date provided of First Vaccination Dose:",'\x1b[5;31;40m'+'Invalid Date provided of First Vaccination Dose:'+'\x1b[0m')
	i=i.replace("Invalid Date provided of First Vaccination Dose:",'\x1b[1;31;38m'+'Invalid Date provided of First Vaccination Dose:'+'\x1b[0m')
	
	# INVALID INPUTS #
	'''
	if re.search("Invalid input",data_recvd):
		i=i.replace(data_recvd,"\x1b[1;31;38m"+data_recvd+"\x1b[0m")
	'''
	i=i.replace("Invalid input provided",'\x1b[1;31;38m'+'Invalid input provided'+'\x1b[0m')
	i=i.replace("Invalid input provided",'\x1b[3;31;38m'+'Invalid input provided'+'\x1b[0m')
	i=i.replace("Try again",'\x1b[1;31;38m'+'Try again'+'\x1b[0m')
	i=i.replace("Try again",'\x1b[3;31;38m'+'Try again'+'\x1b[0m')
	
	# AGE SELECTION #
	i=i.replace("Select the Age Group:",'\x1b[1;33;38m'+'Select the Age Group:'+'\x1b[0m')
	i=i.replace("Selected Age Group:",'\x1b[1;36;38m'+'Selected Age Group:'+'\x1b[0m')
	i=i.replace("Selected Age Group:",'\x1b[3;36;38m'+'Selected Age Group:'+'\x1b[0m')
	
	# STATE SELECTION #
	i=i.replace("Select the State:",'\x1b[1;33;38m'+'Select the State:'+'\x1b[0m')
	i=i.replace("Selected State:",'\x1b[1;36;38m'+'Selected State:'+'\x1b[0m')
	i=i.replace("Selected State:",'\x1b[3;36;38m'+'Selected State:'+'\x1b[0m')

	# DISTRICT SELECTION #
	i=i.replace("Select the District:",'\x1b[1;33;38m'+'Select the District:'+'\x1b[0m')
	i=i.replace("Selected District:",'\x1b[1;36;38m'+'Selected District:'+'\x1b[0m')
	i=i.replace("Selected District:",'\x1b[3;36;38m'+'Selected District:'+'\x1b[0m')

	# CENTER SELECTION #
	i=i.replace("Select the Vaccination Center Name:",'\x1b[1;33;38m'+'Select the Vaccination Center Name'+'\x1b[0m')
	i=i.replace("Selected Vaccination Center:",'\x1b[1;36;38m'+'Selected Vaccination Center:'+'\x1b[0m')
	i=i.replace("Selected Vaccination Center:",'\x1b[3;36;38m'+'Selected Vaccination Center:'+'\x1b[0m')

	# SLOT SELECTION #
	i=i.replace("Select one of the available slots to schedule the Appointment:",'\x1b[1;33;38m'+'Select one of the available slots to schedule the Appointment:'+'\x1b[0m')
	i=i.replace("Selected Vaccination Appointment Date:",'\x1b[1;36;38m'+'Selected Vaccination Appointment Date:'+'\x1b[0m')
	i=i.replace("Selected Vaccination Appointment Date:",'\x1b[3;36;38m'+'Selected Vaccination Appointment Date:'+'\x1b[0m')
	
	i=i.replace("Available Slots on the selected Date:",'\x1b[1;36;38m'+'Available Slots on the selected Date:'+'\x1b[0m')
	i=i.replace("Available Slots on the selected Date:",'\x1b[3;36;38m'+'Available Slots on the selected Date:'+'\x1b[0m')
	
	i=i.replace("Selected Appointment Date has no available slots, select another date!",'\x1b[1;31;38m'+'Selected Appointment Date has no available slots, select another date!'+'\x1b[0m')

	# BOOKING SUCCESSFUL #
	a="Your appointment is scheduled. Make sure to carry ID Proof while you visit Vaccination Center!"
	i=i.replace(a,'\x1b[3;32;38m'+a+'\x1b[0m')
	i=i.replace(a,'\x1b[1;32;38m'+a+'\x1b[0m')
	i=i.replace(a,'\x1b[5;32;38m'+a+'\x1b[0m')
	a="See ya! Visit again :)"
	i=i.replace(a,'\x1b[3;32;38m'+a+'\x1b[0m')
	i=i.replace(a,'\x1b[1;32;38m'+a+'\x1b[0m')
	i=i.replace(a,'\x1b[5;32;38m'+a+'\x1b[0m')

	print(i)
	if "<<< See" in data_recvd:
		server_socket.close()
		exit()
	##################################################

if __name__ == '__main__':
	"""Main function, code begins here
	"""

	# Define constants for IP and Port address of the Server to connect to.
	# NOTE: DO NOT modify the values of these two constants
	HOST = '127.0.0.1'
	PORT = 24680

	# Start the connection to the Server
	server_socket = None
	try:
		server_socket = connectToServer(HOST, PORT)
	except ConnectionRefusedError:
		print("*** Start the server first! ***")
	
	# Receive the data sent by the Server and provide inputs when asked for.
	if server_socket != None:
		while True:
			data_recvd = server_socket.recv(1024).decode('utf-8')
			formatRecvdData(data_recvd)
			if '>>>' in data_recvd:
				data_to_send = input()
				server_socket.sendall(data_to_send.encode('utf-8'))
			
			if not data_recvd:
				server_socket.close()
				break
		
		server_socket.close()
