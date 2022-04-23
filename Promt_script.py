# Promt script made by sade5000 !bin 
################################################################
#headers
import requests
import os
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
print( '2.second option')
print( '3.third option' )
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
list_option = ['hiden','Scanning ip' , ' second ' , ' third ' , ' forth ']
for opt in list_option :
	opt = list_option[chose]
print('You chose: ' + opt )

########## Condition for first menu #######################
if chose == 1:
	print("Enter host adress: ")
	adress_u = input()
	ping_times = input("Enter maximu of times: \n")
#1.########################################################		
def ping_scan():
	response = os.system(" ping -c " + ping_times + " " + adress_u)
	if x <= int(ping_times):
		print(response)
ping_scan()
	

################################################################

