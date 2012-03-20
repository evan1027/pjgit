"""
import httplib

conn = httplib.HTTPConnection("www.baidu.com")
conn.request('get', '/')
data = conn.getresponse().read()
if data:
    f = open("get.html", 'w')
    f.write(data)
    f.close()
    print data.strip()
else:
    print "receive nothing"
conn.close() 
"""
import socket

httpSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
httpSock.connect(("www.baidu.com", 80)) # here
httpSock.send("GET /\n")
data = httpSock.recv(1024)
httpSock.close()

if data:
    f = open("get.html", 'w')
    f.write(data)
    f.close()
    print data.strip()
else:
    print "receive nothing"





