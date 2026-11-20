
from scapy.all import sniff, IP, TCP, UDP, ICMP
from datetime import datetime

log_file = "packet_log.txt"

# Packet counters
packet_count = {
    "TCP": 0,
    "UDP": 0,
    "ICMP": 0,
    "Other": 0
}


def analyze_packet(packet):

    if IP in packet:

        source_ip = packet[IP].src
        destination_ip = packet[IP].dst
        packet_size = len(packet)

        source_port = "N/A"
        destination_port = "N/A"

        if TCP in packet:
            protocol = "TCP"
            source_port = packet[TCP].sport
            destination_port = packet[TCP].dport

        elif UDP in packet:
            protocol = "UDP"
            source_port = packet[UDP].sport
            destination_port = packet[UDP].dport

        elif ICMP in packet:
            protocol = "ICMP"

        else:
            protocol = "Other"

        # Update packet counter
        packet_count[protocol] += 1

        timestamp = datetime.now().strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        packet_info = f"""
Date and Time   : {timestamp}
Source IP       : {source_ip}
Destination IP  : {destination_ip}
Protocol        : {protocol}
Source Port     : {source_port}
Destination Port: {destination_port}
Packet Size     : {packet_size} bytes
---------------------------------------
"""

        print(packet_info)

        with open(log_file, "a", encoding="utf-8") as file:
            file.write(packet_info)


def show_summary():

    total = sum(packet_count.values())

    print("\n========== NETWORK TRAFFIC SUMMARY ==========")
    print("Total Packets :", total)
    print("TCP Packets   :", packet_count["TCP"])
    print("UDP Packets   :", packet_count["UDP"])
    print("ICMP Packets  :", packet_count["ICMP"])
    print("Other Packets :", packet_count["Other"])
    print("==============================================")

    
print("===================================")
print("     NETWORK PACKET ANALYZER")
print("===================================")
print("Capturing packets...")
print("Press CTRL + C to stop.")

try:
    sniff(
        filter="ip",
        prn=analyze_packet,
        store=False
    )

except KeyboardInterrupt:
    print("\nPacket capturing stopped.")
    show_summary()
    print("Packet details saved in packet_log.txt")
