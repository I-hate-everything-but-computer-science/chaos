def test():
    return 1

def help():

    file = open('documentation.md','r')
    content = file.read()
    
    print(' There are currently three main tools from this toolkit.\n1: Port scanner\n2: Ping sweeper\n3: Packet sniffer\nHere is the documentation of this toolkit.\n', content)    
