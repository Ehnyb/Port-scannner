# Port-scannner
## 1. Overview
This project is a simple Python-based network port scanner that scans open ports on a given IP address and saves the results to a file. It helps to identify which ports are open on a system for security analysis.

## 2. How It Works
- The script uses Python's `socket` library to attempt connections to each port in the specified range.
- If a connection is successful, the port is considered open.
- The open ports are displayed in the terminal and saved to `port_scan_results.txt`.

## 3. How to Run:
1. **Install Python:** Make sure Python 3 is installed on your system:
   ```bash
   sudo apt install python3
2. **Run the Script:** Navigate to the folder where the script is saved and run:
   python3 port_scanner.py
3 **Enter Details:**
   ### **How to Customize:**
- Replace `192.168.1.1` with an example IP you scanned.
- In the "Future Improvements" section, list any features you plan to add later.

## Files:
	•	port_scanner.py: The main Python script.
	•	port_scan_results.txt: The saved results of a sample scan.
