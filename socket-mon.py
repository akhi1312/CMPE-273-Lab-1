import psutil
import collections


def main():
    pidlist =[]
    tcp_final =[]
    tcp_sockets = psutil.net_connections(kind='tcp')

    print "PID,Local address,Remote address,Status"
    for a in tcp_sockets:
        if a.pid not in [] and str(a.laddr) not in ["()","::"] and str(a.raddr)!= "()":
            pidlist += [a.pid]
            tcp_final += [a]
    counts= collections.Counter(pidlist)
    pidlist = sorted(pidlist ,key=counts.get ,reverse =True)
    pidlist = set(pidlist)
    for e in pidlist:
        for c in tcp_final:
            if  c.pid == e:
                laddr = str(c.laddr[0])+"@"+str(c.laddr[1])
                raddr = str(c.raddr[0])+"@"+str(c.raddr[1])
                print  "\"{}\",\"{}\",\"{}\",\"{}\"".format(c.pid,laddr,raddr,c.status)

if __name__ == '__main__':
    main()
