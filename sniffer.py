
#!/usr/bin/env python3

"""
CodeAlpha Task 1: Basic Network Sniffer

Captures IP packet metadata on an authorised network.
"""

import argparse
from datetime import datetime

from scapy.all import sniff, IP, TCP, UDP, ICMP


def display_packet(packet):
    """Display useful information about a captured IP packet."""

    if IP not in packet:
        return

    ip_layer = packet[IP]

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

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
        source_port = "-"
        destination_port = "-"

    else:
        protocol = f"IP protocol {ip_layer.proto}"
        source_port = "-"
        destination_port = "-"

    print("\n" + "=" * 55)
    print(f"Time:             {timestamp}")
    print(f"Protocol:         {protocol}")
    print(f"Source IP:        {ip_layer.src}")
    print(f"Destination IP:   {ip_layer.dst}")
    print(f"Source Port:      {source_port}")
    print(f"Destination Port: {destination_port}")
    print(f"Packet Length:    {len(packet)} bytes")
    print("=" * 55)


def main():
    parser = argparse.ArgumentParser(
        description="Basic Python Network Sniffer using Scapy"
    )

    parser.add_argument(
        "--iface",
        help="Network interface to capture from"
    )

    parser.add_argument(
        "--count",
        type=int,
        default=30,
        help="Number of packets to capture (default: 30)"
    )

    parser.add_argument(
        "--filter",
        default="ip",
        help="BPF capture filter (default: ip)"
    )

    args = parser.parse_args()

    print("CodeAlpha Basic Network Sniffer")
    print("Starting packet capture...")
    print("Press Ctrl+C to stop.\n")

    try:
        sniff(
            iface=args.iface,
            filter=args.filter,
            prn=display_packet,
            count=args.count,
            store=False
        )

        print("\nPacket capture completed.")

    except PermissionError:
        print("\nPermission denied. Run the terminal as Administrator.")

    except OSError as error:
        print(f"\nCapture error: {error}")
        print("Check that Npcap is installed and your interface is valid.")

    except KeyboardInterrupt:
        print("\nCapture stopped by user.")


if __name__ == "__main__":
    main()
