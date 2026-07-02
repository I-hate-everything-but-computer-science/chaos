def test():
    return 1

import nmap
#PING SWEEPER?????????????????????????????????????????????????????????????
#I REMEMBER TRYING TO MAKE THIS AFTER FAILING PCAP (BEFORE PASSING)
#I GAVE UP SO QUICKLY BAHAHHAHAHAHAHHAHA AND I WASTED LIKE 4 DAYS ON KALI LINUX BEING SO CONFUSED BAHAHAHHAHAHAHHAHA

def PiNgSwEePeR(SUBNET):#okay 192.168.50.1/24 is my range i hope....   im kinda cooked if its not my LAN
    nm = nmap.PortScanner()#update i called my father and he said it is
    print(f'Please wait. Pinging devices on subnet {SUBNET}.')
    output = []
    try:
        result = nm.scan(hosts=SUBNET, arguments='-sn')
        for host in nm.all_hosts():
            stateofTHING = nm[host].state()
            if stateofTHING == 'up':
                output.append(f'The device with the IPv4 address {host} is on and connected to the internet.')
        for i in range(len(output)): print(output[i])
    except BaseException as aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa:
        print(f'Error:{aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa}')
    #that only took about 10 mins wtf wtf wtf wtf wtf
