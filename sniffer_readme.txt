

A network sniffer is just as it sounds; a software tool that monitors, or sniffs out the data flowing over computer network links in real time. It can be a self-contained software program or a hardware device with the appropriate software or firmware.

Network sniffers can take snapshot copies of the data without redirecting or altering it. Some sniffers work only with TCP/IP packets, but the more sophisticated tools can work with many other network protocols and at lower levels, including Ethernet frames.

SCAPY:
    Scapy is a powerful interactive packet manipulation program. It is able to forge or decode packets of a wide number of protocols, send them on the wire, capture them, match requests and replies, and much more. It can easily handle most classical tasks like scanning, tracerouting, probing, unit tests, attacks or network discovery (it can replace hping, 85% of nmap, arpspoof, arp-sk, arping, tcpdump, tethereal, p0f, etc.). It also performs very well at a lot of other specific tasks that most other tools can’t handle, like sending invalid frames, injecting your own 802.11 frames, combining technics (VLAN hopping+ARP cache poisoning, VOIP decoding on WEP encrypted channel, …), etc. 

To install scapy on linux using pip use the following command:
    $ pip install scapy
    
For using scapy in any python code import scapy.all in the program





######################## INSTRUCTIONS FOR mysniffer.py ############################################################# 

In the attached Python script mysniffer:
Once You run the code will start sniffing the tcp protocol packets from your network traffic after 3 seconds of it running.
it will keep capturing packets till a keyboard interupt of 'ctrl +c' is given after that (max 500 packets)[i;
User have to choose whether he/she want to see any packets displayed above in detail (Packets are displayed in short with a serial number in square brackets([]) as and when they are captured).
This can be done by entering the serial number of the packet to be selected.
-1 can be used to exit.

###################################################################################################################


Detailed sample of a tcp packet

###[ Ethernet ]### 
  dst       = 78:44:76:53:94:34
  src       = b8:81:98:6a:b5:e4
  type      = 0x800
###[ IP ]### 
     version   = 4L
     ihl       = 5L
     tos       = 0x0
     len       = 52
     id        = 17708
     flags     = DF
     frag      = 0L
     ttl       = 64
     proto     = tcp
     chksum    = 0x679
     src       = 192.168.1.18
     dst       = 13.32.32.69
     \options   \
###[ TCP ]### 
        sport     = 54814
        dport     = https
        seq       = 1525624098
        ack       = 1283084141
        dataofs   = 8L
        reserved  = 0L
        flags     = A
        window    = 885
        chksum    = 0x29aa
        urgptr    = 0
        options   = [('NOP', None), ('NOP', None), ('Timestamp', (2670042395, 155064621))]

IF its an http or https request then it will also show the payload
