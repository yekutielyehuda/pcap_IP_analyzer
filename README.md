# Scapy PCAP Analyzer

This script is designed to analyze a pcap file using Scapy, extracting information about a specific address provided by the user.

## Requirements

- Python 3.x
- Scapy library (`pip install scapy`)

## Usage

1. Clone or download the script to your local machine.
2. Ensure you have Python 3.x installed.
3. Install Scapy library if not already installed: `pip install scapy`.
4. Run the script from the command line.

```
python pcap_analyzer.py
```

5. Follow the prompts:
   - Enter the path to the pcap file when prompted.
   - Enter the target address you want to analyze when prompted.

## Functionality

- The script loads the specified pcap file.
- It filters packets to only those involving the target address provided by the user.
- For each packet involving the target address, it prints a summary and detailed information extracted by Scapy.

## Example

Suppose you have a pcap file named `example.pcap` and you want to analyze packets involving the address `192.168.0.1`. You would run the script and input the path to the pcap file and the target address accordingly.

```
Enter the path to the pcap file: example.pcap
Enter the target address to analyze: 192.168.0.1
```

The script will then output information about each packet involving the specified address in the pcap file.

## Note

- Ensure you have the necessary permissions to access the pcap file.
- This script provides basic functionality. You may extend it to suit your specific needs, such as additional filtering criteria or output formatting.
