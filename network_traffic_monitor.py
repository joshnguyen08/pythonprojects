import pyshark
import socket
import whois


def print_packet_info(packet):
    try:
        #Get source IP from packet
        source_ip = packet.ip.src
        #Get destination IP from packet
        destination_ip = packet.ip.dst
        #Get transport protocol for packet
        protocol = packet.transport_layer
        #Get length of packet
        length = packet.length
        
        try:
            #Find hostname associated with source IP
            source_host = socket.gethostbyaddr(source_ip)[0]
        except socket.herror:
            #If not found, try WHOIS lookup
            try:
                source_host = whois.whois(source_ip).name
            except:
                #If not found with WHOIS loopup AND socket.gethost, source is unknown
                source_host = "Unknown"

        try:
            #Find hostname associated with destination IP
            destination_host = socket.gethostbyaddr(destination_ip)[0]
        except socket.herror:
            try:
                #If not found, try WHOIS lookup for destination IP
                destination_host = whois.whois(destination_ip).name
            except:
                #If not found or either, destination host = unknown
                destination_host = "Unknown"

        #Prints the packet contents in specific format below
        print(f"Source IP: {source_ip} ({source_host}) -> Destination IP: {destination_ip} ({destination_host})")
        print(f"Protocol: {protocol}, Length: {length} bytes")
        print("-" * 60)

     #Handle AttributeError incase of missing source, etc.    
    except AttributeError:
        pass

def main():
    capture = pyshark.LiveCapture(interface='Ethernet', display_filter='ip')
    capture.apply_on_packets(print_packet_info)

if __name__ == '__main__':
    main()
