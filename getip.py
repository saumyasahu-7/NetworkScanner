from scapy.all import sniff, IP

# Set to store unique IP addresses
ip_set =set()

def getip():
    def packet_callback(packet):
        if IP in packet:
            # Add source and destination IPs to the set
            ip_set.add(packet[IP].src)
            ip_set.add(packet[IP].dst)
    # Capture packets on the network interface
    packets=sniff(prn=packet_callback, timeout=60)
    # Print captured IPs
    print("Captured IPs:", ip_set)
    return list(ip_set)

if(__name__=="__main__"):
    getip()
    