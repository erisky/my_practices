"""
 Create a Server Server and socket client between AP and Daemon
 > 1. Recording Packet, 
"""


import  wx
import  wx.grid as  Grid

import socket
import SocketServer
import threading


"""
TCP Forwarder and logger
This class Create the TCP Server and forward to assigned port 
but it writes to Database before 
"""

class MyTCPHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024)
        cur_thread = threading.current_thread()
        response = "TEST ONLY!!!!!!!"
        print "thread: <<<<{}>>>>".format(str(cur_thread))
        print "DATA:"+ data
        print "Context:{}".format(self.server.context)
        print repr(data)
        self.request.sendall(response)


class MyForwarder(SocketServer.BaseRequestHandler):
	def setup(self):
		# Create the socket to connect to AP
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.sock.connect((self.server.ipTarget, self.server.portTarget))
		self.sock.setblocking(0)
		self.request.settimeout(0.01)
		#self.server.ipTarget
		#self.server.portTarget
	def handle(self):

		while True:
			try:
				data = self.request.recv(1024)    
				# print "len Got = {}".format(len(data))
				if (len(data) <= 0):
					break
				self.sock.sendall(data)
			except socket.timeout:
				pass
			try:
				data_from_target = self.sock.recv(1024)
				self.request.sendall(data_from_target)
			except socket.error as msg:
				# print "{}".format(msg)
				continue

	def finish(self):
		self.sock.close()


class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    def setup(self, ipTarget, portTarget):
    	self.ipTarget = ipTarget
    	self.portTarget = portTarget
    pass

class tcpSocketSniffer:
	def __init__(self, portServer, ipTarget, portTartet):
		self.portServer = portServer
		self.ipTarget = ipTarget
		self.portTarget = portTartet
		self.SocketHandler = None
		self.server_thread = None
		self.theserver = None

	def setup_handler(self, handler):
		self.SocketHandler = handler
	
	def start_server(self):
		if (self.SocketHandler == None):
			print "Handler is not assigend yet"
		
		#server = SocketServer.TCPServer("localhost", self.portServer, self.SocketHandler)
		#self.theserver = ThreadedTCPServer(("localhost", self.portServer), self.SocketHandler)
		# Start a thread with the server -- that thread will then start one
		# more thread for each request

		self.theserver = ThreadedTCPServer(("localhost", self.portServer ), self.SocketHandler)
		self.theserver.setup(self.ipTarget,self.portTarget)
		self.server_thread = threading.Thread(target=self.theserver.serve_forever)
		# Exit the server thread when the main thread terminates
		self.server_thread.daemon = True
		self.server_thread.start()
		pass

 	 	
def client(ip, port, message):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ip, port))
    try:
        sock.sendall(message)
        response = sock.recv(1024)
        print "Received: {}".format(response)
    finally:
        sock.close()



if __name__ == "__main__":
	print "MyTcpForwarder Testing"
	#theserver = ThreadedTCPServer(("localhost", 7792), MyTCPHandler)
	#ip, port = theserver.server_address

	#server_thread = threading.Thread(target=theserver.serve_forever)
	# Exit the server thread when the main thread terminates
	#server_thread.daemon = True
	#server_thread.start()

	mySnifferServ = tcpSocketSniffer(7788, "172.16.20.12", 13579)
	mySnifferServ.setup_handler(MyForwarder)
	mySnifferServ.start_server()


	test = raw_input("Any Key to Exit")

