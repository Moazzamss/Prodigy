from scapy.all import sniff, IP, TCP, UDP, Raw

# Callback function to handle each captured packet
def packet_callback(packet):
    if IP in packet:
        ip_layer = packet[IP]
        print(f"\n📦 Packet:")
        print(f"From: {ip_layer.src}")
        print(f"To:   {ip_layer.dst}")
        print(f"Protocol: {packet.proto}")

        # Check for transport layer protocols
        if packet.haslayer(TCP):
            print("Protocol: TCP")
        elif packet.haslayer(UDP):
            print("Protocol: UDP")

        # If packet contains raw payload
        if packet.haslayer(Raw):
            payload = packet[Raw].load
            try:
                print(f"Payload: {payload.decode(errors='ignore')}")
            except:
                print(f"Payload (non-decodable): {payload}")
# Main sniffing function
def main():
    print("🛜 Packet sniffer started... Press CTRL+C to stop.\n")
    sniff(prn=packet_callback, store=False)

if __name__ == "__main__":
    main()
