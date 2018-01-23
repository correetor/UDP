import socket

UDP_IP = "127.0.0.1"
UDP_PORT = 5002
MESSAGE = raw_input("Number fact:")

print "UDP target IP:", UDP_IP
print "UDP target port:", UDP_PORT
print "Number:", MESSAGE

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP

try:
    sock.sendto(MESSAGE, (UDP_IP, UDP_PORT))
    data, server = sock.recvfrom(1024)
    print("received data:"+data)
    
finally:
    sock.close()
