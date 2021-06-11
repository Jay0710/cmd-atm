import numpy as np
import os
import time
from datetime import datetime

account_details=np.array([[1,5000000,'Current'],[2,25000,'Saving'],[3,2600000,'Saving'],[4,90000000,'Current']]) 				#(number,amount,type)
username=['jay','vasant','vriti','varsha']
pin=[2000,1972,1973,1996]

def withdraw(my_acc):
	file=open((Username+'.txt'),'w')
	while True:
		os.system('cls')
		amount=(input('Enter Amount (or press c to cancel) : '))
		if amount=='c' or amount=='C':
			os.system('cls')
			break
		amount=int(amount)
		cash_status=0
		if int(account_details[my_acc][1])-amount<0:
			print("Insufficient Balance")
			time.sleep(2)
			os.system('cls')
			return 0
		#code for machine giving out the cash
		status=input('Did You receive Cash ?? y/n \n')
		status=status.lower()
		if status=='y':
			cash_status=1
		else : 
			cash_status=0
			continue

		if cash_status==1:
			account_details[my_acc][1]=int(account_details[my_acc][1])-amount
			os.system('cls')
			print('Cash Withdrawn ',amount)
			
			now=datetime.now()
			dt=now.strftime("%d/%m/%Y %H:%M:%S")
			file.write('\n'+str(dt)+' '+str(amount)+'\n')
		file.close()
		time.sleep(1)
		os.system('cls')
		break

def check_bal(acc_no):
	os.system('cls')
	print(account_details[acc_no][1])
	time.sleep(5)
	os.system('cls')

def deposit(acc_no):
	file=open((Username+'.txt'),'w')
	while True:
		os.system('cls')

		#code for sensor getting the actual amount inserted
		
		amount=(input('Confirm the amount deposited : '))
		
		#code if sensor data is equal to confirmed data continue else break

		amount=int(amount)
		
		account_details[my_acc][1]=int(account_details[my_acc][1])+amount
		os.system('cls')
		print('Cash Deposited ',amount)
			
		now=datetime.now()
		dt=now.strftime("%d/%m/%Y %H:%M:%S")
		file.write('\n'+str(dt)+' '+str(amount)+'\n')
		file.close()
		time.sleep(1)
		os.system('cls')
		break

def change_pin(acc_no,account_details,pin):
	os.system('cls')
	confirm_acc=(input('Enter your account number : '))
	
	if confirm_acc==account_details[acc_no][0]:
		os.system('cls')
		confirm_pin=int(input('Enter your previous pin : '))
	
		if confirm_pin in pin:
			os.system('cls')
	
			for i in pin:
	
				if confirm_pin==i:
					loc=pin.index(i)
					pin[loc]=int(input('Enter new pin : '))
					break

				
				
	
		else: 
			print('Incorrect Pin !')
			time.sleep(2)
			os.system('cls')
			return 0
	
	else: 
		print('Incorrect Account Number !')
		time.sleep(2)
		os.system('cls')
		return 0

	print('New pin set')
	time.sleep(2)
	os.system('cls')

	


chances=3
while True:
	
	os.system('cls')
	Username=input('Username : ')
	os.system('cls')

	if Username in username:
		Pin=int(input('Pin : '))
		os.system('cls')

		if Pin in pin:

			if Username=='jay':
				my_acc=0 
	
			if Username=='vasant':
				my_acc=1
	
			if Username=='vriti':
				my_acc=2 
	
			if Username=='varsha':
				my_acc=3 

			while True:

				choice=int(input('Enter what you want to do \n1.Withdraw\n2.Deposit amount\n3.Check Balance\n4.Change pin\n5.Logout\n'))

				if Username=="" or Pin==0:
					break

				if choice==1:
					withdraw(my_acc)

				elif choice==2:
					deposit(my_acc)
				
				elif choice==3:
					check_bal(my_acc)
					

				elif choice==4:
					change_pin(my_acc,account_details,pin)
					

				elif choice==5:
					os.system('cls')
					confirm=input('Confirm logging out (y/n) ')
					os.system('cls')
					confirm=confirm.lower()
					if confirm=='y':
						Username=""
						Pin=0
						break

	
				else: 
					print('Wrong Option')
					time.sleep(1)
					os.system('cls')
				
				choice=0
			
			if Username!="" or Pin!=0:
				break

			else:
				continue

		else: 
			print('Incorrect Pin')
			chances-=1
			if chances<=0:
				for i in range(29):
					os.system('cls')
					print('You are logged out Try again in',30-i)
					time.sleep(1)
				chances=3
				continue
			print(chances,' chances left')
			time.sleep(2)
			os.system('cls')
			continue

	else: 
		print('Incorrect Username')
		chances-=1
		if chances<=0:
			for i in range(29):
				os.system('cls')
				print('You are logged out Try again in',30-i)
				time.sleep(1)
			chances=3
			continue
		print(chances,' chances left')
		time.sleep(2)
		os.system('cls')
		continue
