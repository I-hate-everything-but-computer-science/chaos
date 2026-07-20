def test():
    return 1

import f
import scapy.all as scapy

def sniff(pc):
    pkts = scapy.sniff(count = pc)
    counter = 0
    for packet in pkts:
        ask = str(input('The algorithm has captured a packet, would you like to know more information? [y/n]'))
        if ask in ['y','yes','Yes','Y','YES','YeS','YEs','yEs','yES','yeS']:
            try: 
                print(f"Source IP: {packet['IP'].src}\nDestination MAC: {packet['Ether'].dst}")
            except: 
                f.error_msg()
        counter += 1
