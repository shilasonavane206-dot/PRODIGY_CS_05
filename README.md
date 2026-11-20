\# Project 5: Network Packet Analyzer



\## Objective

The objective of this project is to develop a Network Packet Analyzer using Python and Scapy. It captures network packets and displays important packet information for educational and network analysis purposes.



\## Features

\- Captures IP network packets.

\- Identifies TCP, UDP and ICMP protocols.

\- Displays Source IP and Destination IP.

\- Displays Source Port and Destination Port.

\- Shows packet size in bytes.

\- Records date and time of captured packets.

\- Saves packet details in a log file.

\- Displays a network traffic summary.



\## Technologies Used

\- Python

\- Scapy

\- Npcap

\- Datetime Module



\## Project Structure



```text

project5-network\_packet\_analyzer/

│

├── network\_analyzer.py

├── packet\_log.txt

└── README.md

```



\## Installation



Install Scapy:



```bash

python -m pip install scapy

```



Install Npcap on Windows from:



https://npcap.com/#download



\## How to Run



1\. Open PowerShell as Administrator.

2\. Navigate to the project folder.

3\. Run the following command:



```bash

python network\_analyzer.py

```



4\. Generate network traffic using a permitted test connection.

5\. Press CTRL + C to stop packet capturing.

6\. View the packet details and traffic summary.

7\. Check packet\_log.txt for saved packet information.



\## Learning Outcomes

\- Understanding network packets.

\- Learning IP addresses and port numbers.

\- Understanding TCP, UDP and ICMP protocols.

\- Using Python Scapy for packet analysis.

\- Learning network traffic monitoring.

\- Practicing Python file handling.



\## Ethical Use

This project is developed for educational purposes. Packet capture should only be performed on networks and devices that you own or have explicit permission to monitor. The project displays packet metadata and does not attempt to decrypt network traffic or collect passwords.

