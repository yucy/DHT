# -*- coding:utf-8 -*-
import hashlib,time
import socket

		
# 用于答复客户端请求，相当于是server
def dong():
	m_server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
	m_server.bind(('',6881))
	print '正在等待介入'
	while  True:
		# 接受数据
		data,addr = m_server.recvfrom(1024)
		print 'from ',addr,' receive : ',data


def send_find_node(self, address, nid=None):
	nid = get_neighbor(nid, self.nid) if nid else self.nid
	tid = entropy(TID_LENGTH)
	msg = {
	"t": tid,
	"y": "q",
	"q": "find_node",
	"a": {
		"id": nid,
		"target": random_id()
		}
	}
	self.send_krpc(msg, address)


if __name__ == '__main__':
	dong()