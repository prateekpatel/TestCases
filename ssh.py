import sys, os

def ssh(hostname, usrname, key, command):
   os.system("ssh "+usrname+"@"+hostname+" -i "+key+" "+command.replace('"',''))

args = sys.argv
hosts = args[1].split(',')

#args[1] list of hosts with comma seprated
#args[2] common username for all host
#args[3] common key full path for all host
#args[4] command to execute

for host in hosts:
   ssh(host, args[2], args[3], args[4])

