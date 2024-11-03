#!/usr/bin/python3
import time
from pexpect import pxssh
import socket
pause = 5

session = pxssh.pxssh()
while True:
	if not session.login('172.28.0.5','john','KZS{y0U_4r3_3v1L_:0}',port=22):
		print("[*] SSH server is not up ?")
		break
	else:
		print("[*] Sucessfull login")
		
		print("[*] Direct logout && wait 30s for new connexion")
		session.logout()
		time.sleep(pause)
		
		session = pxssh.pxssh()

print("[*] Logout")
s.logout()

