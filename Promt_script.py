# Promt script made by sade5000 !bin 
################################################################
#headers
import requests
import os
import sys
import socket
import ftplib
from datetime import datetime



x = 0
################################################################LOGO
print('=========================================================')
print(' ****   **   **     ****   ****   **    **    **' )
print(' *     *  *  *  *   *      *     *  *  *  *  *  *')
print(' ****  ****  *  *   ****   ****  *  *  *  *  *  *')
print('    *  *  *  *  *   *         *  *  *  *  *  *  *')
print(' ****  *  *  * *    ****   ****   **    **    ** ')
print('=========================================================')
###############################################################
#Main Meniu
print( '\n' +'Chose your option from menu!')
print( '1.Scanning')
print( '2.Port scan')
print( '3.FTP connection' )
print( '4.forth option' )
chose = input("your chose is: \n")
chose = int(chose)
################################################################
# Condition of using main menu
if chose > 4:
	print('you have to chose a valid option!')
	quit()
if chose < 1:
	print('you have to chose a valid option!')
	quit()
################################################################
#Meniu Functions 
list_option = ['hiden','Find IP' , ' Scan for open PORTS ' , ' FTP BF-Atack' , ' forth ']
for opt in list_option :
	opt = list_option[chose]
print('Your option is: ' + opt )

########## Condition for first menu #######################
if chose == 1:
	print("Host URL: ")
	adress_u = input()
	ping_times = input("Enter max of pings: \n")
	ping_scan()
#1.########################################################		
	def ping_scan():
		response = os.system(" ping -c " + ping_times + " " + adress_u)
		if x <= int(ping_times):
			print(response)
	ping_scan()
#1.1########################################################
elif chose == 2:
	print("Host ip or URL: ")
	adress_us = input()
	def port_scan():
		target = socket.gethostbyname(adress_us)
		print("We are scanning target: "+target)
		print("Add maximum port range from 1 to max: ")
		max_port = input()
		for port in range (1 , int(max_port)):
			s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
			socket.setdefaulttimeout(1)
			result = s.connect_ex((target,port))
			if result == 0:
				print("Port: {}  is open".format(port))
			s.close()
	port_scan()

		
#1.2###########################################################
elif chose == 3:
	print("Host IP: ")
	adress_uss = input()
	def FTP_connect():
		print("we are connecting to: " + adress_uss + " host")
		
	FTP_connect()
	

