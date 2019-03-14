
#!/usr/bin/python
from easysnmp import Session
from time import sleep
import sys,time
from math import ceil
k = 0
a=sys.argv
t = 1/float(a[2])
z = a[2]
b = range(0, int(a[3]))
a1 = a[4:]
a1.insert(0,".1.3.6.1.2.1.1.3.0")
cou = len(a1)
x=a[1].split(":")
t0=time.time()
session = Session(hostname=x[0], remote_port=x[1], community=x[2], version=2, 
timeout=2, retries=1)
if (a[3] == '-1'):
   while (True):
        t1=time.time()
        c= session.get(a1)
        i = 0
        while(i < cou):
            i = i+1
        if (k != 0):
            j = 1
            print int(time.time()),'|',
            while(j < cou) and c[j].value!="NOSUCHINSTANCE" and d[j].value!
="NOSUCHINSTANCE":
                    var1 = int(c[j].value)
                    var2 = int(d[j].value)
                    var3 = ((float(c[0].value)-float(d[0].value))/100)
                    rate = int((var1-var2)/var3)
                    if rate<0:
                            if c[j].snmp_type=='COUNTER':
                                print rate + 2**32,'|',
                            if c[j].snmp_type=='COUNTER64':
                                print rate + 2**64,'|',
                    elif rate>=0:
                            print rate,'|',
                    j = j + 1
            print ""
        d = c
        k = k+1
        t2=time.time()
        l=ceil((t2 - t0)/t)
        sleepTime = (t0+l*t) - t2
        if sleepTime<=0.0:
           sleepTime = (t0+(l+1)*t) - t2
           sleep(sleepTime)
        else:
          sleepTime = (t0+l*t) - t2
          sleep(sleepTime)
else:
    while (k < int(a[3])+1):
        t1=time.time()
        c= session.get(a1)
        i = 0
        while(i < cou):
            i = i+1
        if (k != 0):
            if t<1:
                newtime=float(c[0].value)/100
                oldtime=float(d[0].value)/100
            else:
                 newtime=int(c[0].value)/100
                 oldtime=int(d[0].value)/100
            if newtime < oldtime:
                print "snmp restart"
                del c[:]
                del d[:]
                k = k-1
            j = 1
            print int(time.time()),'|',
            while(j < cou) and c[j].value!="NOSUCHINSTANCE" and d[j].value!
="NOSUCHINSTANCE":
                    var1 = int(c[j].value)
                    var2 = int(d[j].value)
                    var3 = newtime - oldtime
                    rate = int((var1-var2)/var3)
                    if rate<0:
                            if c[j].snmp_type=='COUNTER':
                                print rate + 2**32,'|',
                            if c[j].snmp_type=='COUNTER64':
                                print rate + 2**64,'|',
                    elif rate>=0:
                            print rate,'|',
                    j = j + 1
            print ""
        d = c
        k = k+1
        t2=time.time()
        l=ceil((t2 - t0)/t)
        sleepTime = (t0+l*t) - t2
        if sleepTime<=0.0:
           sleepTime = (t0+(l+1)*t) - t2
           sleep(sleepTime)
        else:
          sleepTime = (t0+l*t) - t2
          sleep(sleepTime)
