
import psutil
import collections


def main():
    pidlist =[]
    tcp_final =[]
    tcp_sockets = psutil.net_connections(kind='tcp')
# Header
    print "PID,Local address,Remote address,Status"

# All valid tcp connections 
    for a in tcp_sockets:
        if a.pid != None and str(a.laddr) not in ["()", "::"] and str(a.raddr)!= "()":
            pidlist += [a.pid]
            tcp_final += [a]
    counts= collections.Counter(pidlist)
    pidlist = sorted(set(pidlist) ,key=counts.get ,reverse =True) 
 
 # Printing Final Output 
    for e in pidlist:
        for c in tcp_final:
            if  c.pid == e:
                laddr = str(c.laddr[0])+"@"+str(c.laddr[1])
                raddr = str(c.raddr[0])+"@"+str(c.raddr[1])
                print  "\"{}\",\"{}\",\"{}\",\"{}\"".format(c.pid,laddr,raddr,c.status)

if __name__ == '__main__':
    main()

