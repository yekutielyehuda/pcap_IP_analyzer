from scapy.all import *

def analyze_pcap(pcap_path, target_address):
    # Load the pcap file
    packets = rdpcap(pcap_path)
    
    # Filter packets to only those involving the target address
    target_packets = [pkt for pkt in packets if IP in pkt and (pkt[IP].src == target_address or pkt[IP].dst == target_address)]

    if not target_packets:
        print("No packets found involving the target address.")
        return
    
    print(f"Found {len(target_packets)} packets involving the target address {target_address}:")
    
    # Extract and print information about each packet involving the target address
    for i, pkt in enumerate(target_packets, 1):
        print(f"\nPacket {i}:")
        print(pkt.summary())
        print(pkt.show())

if __name__ == "__main__":
    # Get pcap file path and target address from user input
    pcap_path = input("Enter the path to the pcap file: ")
    target_address = input("Enter the target address to analyze: ")
    
    # Analyze the pcap file
    analyze_pcap(pcap_path, target_address)
