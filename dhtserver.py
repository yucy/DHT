# -*- coding:utf-8 -*-

import hashlib,time
import socket


# 初始化公网节点
BOOTSTRAP_NODES = (
	("67.215.246.10", 6881),
	("82.221.103.244", 6881),
	("23.21.224.150", 6881),
	("localhost", 6881),
)

# 使用sha1算法，返回key加密后的字符串
def str_encrypt(key):
	sha = hashlib.sha1(key)
	encrypts = sha.hexdigest()
	print encrypts
	return encrypts

# socket 使用方法介绍：http://blog.csdn.net/rebelqsp/article/details/22109925
# 用于发出请求，相当于是client
def ping():
	m_client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	m_client.sendto(b'this is a test',BOOTSTRAP_NODES[3])
	m_client.close()


# 用于答复客户端请求，相当于是server
def dong():
	m_server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	m_server.bind('',68810)
	print '正在等待介入'
	while  True:
		time.sleep(5)
		# 接受数据
		data,addr = m_server.recvfrom(1024)
		print addr
		print data

if __name__ == '__main__':
	# str_encrypt('lamda')
	ping()


'''
DHT协议，共4条：
    ping
    find_node
    get_peers (在edonkey kad中这叫find_value)
    announce_peer

'''