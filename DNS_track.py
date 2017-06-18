#!/user/bin/python
import socket
import sys
import os
import DNS
import re
import threading
import string
import datetime
import time
fw_track_yes=open(sys.argv[2],'a')
def mywork(ip=''):
	domain=['www.baidu.com','www.qq.com','www.taobao.com','www.Tmall.com','www.souhu.com']
	for dname in domain:
		dname=dname.strip()
		r=DNS.Request(dname,qtype=DNS.Type.A,server=ip,timeout=1)
		newnow=""
		new=str(datetime.datetime.now())[:19]
		newnow=''.join(new)
		try:
			res=r.req()
			qr=res.header['qr']
			ra=res.header['ra']
			state=res.header['status']
			if qr==1 and ra==1 and state=="NOERROR":
				fw_track_yes.write(ip+"\n")
				break
			else:
				pass
		except:
			pass
def main():
    fp=open(sys.argv[1],'r')
    ips=fp.readlines()
    for ip in ips:
        ip=ip.strip()
        t=threading.Thread(target=mywork,args=(ip,))
        t.start()
        while threading.activeCount() > 10:
            time.sleep(0.1)
    while threading.activeCount() > 1:
        time.sleep(0.1)
    fp.close()
    fw_track_yes.close()

if __name__ == '__main__':
	main()
