
import socket


sock= socket.socket(socket.AF_INET,socket.SOCK_STREAM)

ipaddress= input('enter the address:')
port = int(input('enter port number:'))

def portScanner(port):
    if sock.connect_ex((ipaddress,port)):
        print(f'PORT {port} is closed:( ')
        
    else:
        print(f'PORT {port} is open :) ')
        
portScanner(port)
