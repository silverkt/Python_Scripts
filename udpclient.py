from socket import *
BUFSIZE = 1024
client = socket(AF_INET,SOCK_DGRAM)
#创建udp套接字
while True:
	buf = input('please input something to client:')
	if buf == 'quit':
		print('connection shutdown...')
		break
#腾讯云主机 ：123.206.41.84
	client.sendto(buf.encode('utf-8'),('123.206.41.84',8000))
	data,addr = client.recvfrom(BUFSIZE)
	print('message from server:',data.decode('utf-8'))
client.close()