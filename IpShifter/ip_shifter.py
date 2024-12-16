import os
import subprocess
import requests
import time
import sys

# ANSI color codes
RESET = "\033[0m"
BOLD = "\033[1m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"

# check if the user run as root or with sudo
def check_sudo():
    if os.geteuid() != 0:
        print(f"{YELLOW}Please run this tool as root or with sudo.{RESET}")
        sys.exit(1)
# Check and install dependencies
def install_dependencies():
    # Check and install Tor if not installed
    try:
        subprocess.run("which tor", shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"{GREEN}[+] Tor is already installed.{RESET}")
    except subprocess.CalledProcessError:
        print(f"{RED}[!] Tor is not installed. Installing Tor...{RESET}")
        os.system("sudo apt update && sudo apt install tor -y")
        print(f"{GREEN}[+] Tor installed successfully.{RESET}")
    
    # Check and install python3-pip if not installed
    try:
        subprocess.run("dpkg -s python3-pip", shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"{GREEN}[+] pip3 is already installed.{RESET}")
    except subprocess.CalledProcessError:
        print(f"{RED}[!] pip3 is not installed. Installing pip3...{RESET}")
        os.system("sudo apt install python3-pip -y")
        print(f"{GREEN}[+] pip3 installed successfully.{RESET}")
    
    # Install required Python packages
    try:
        import requests
    except ImportError:
        print(f"{RED}[!] 'requests' module not found. Installing...{RESET}")
        os.system("pip3 install requests")
        print(f"{GREEN}[+] 'requests' module installed successfully.{RESET}")

# Display banner
def display_banner():
    os.system("clear")
    print(f"{GREEN}{BOLD}" + r"""
         
        _____          _____ _     _  __ _            
       |_   _|        / ____| |   (_)/ _| |           
         | |  _ __   | (___ | |__  _| |_| |_ ___ _ __ 
         | | | '_ \   \___ \| '_ \| |  _| __/ _ \ '__|
        _| |_| |_) |  ____) | | | | | | | ||  __/ |   
       |_____| .__/  |_____/|_| |_|_|_|  \__\___|_|   
             | |                                      
             |_|                 Developer: Sreeraj        

            """ + RESET)
    print(f"{YELLOW}* Copyright © Sreeraj, 2024 ")           
    print(f"{YELLOW}* GitHub: https://github.com/s-r-e-e-r-a-j{RESET}")
    print("\n")
    print(f"{GREEN} change your SOCKS to 127.0.0.1:9050{RESET}")
    print("\n")
# Start Tor service
def initialize_tor():
    os.system("service tor start")
    print(f"{GREEN}[+] Tor service started.{RESET}")

# Change IP using Tor
def rotate_identity():
    os.system("service tor reload")
    print(f"{YELLOW}[~] Identity changed.{RESET}")

# Fetch external IP
def fetch_ip():
    try:
        proxy_settings = {
            "http": "socks5://127.0.0.1:9050",
            "https": "socks5://127.0.0.1:9050",
        }
        response = requests.get("http://httpbin.org/ip", proxies=proxy_settings)
        return response.json().get("origin", "Unknown IP")
    except requests.RequestException as e:
        return f"{RED}Error: Unable to fetch IP.{RESET}"

# Main function to manage IP changes
def execute_rotation():
    display_banner()
    initialize_tor()

    try:
        interval = int(input(f"{YELLOW}[+] Enter interval (seconds) between IP changes [default: 60]: {RESET}") or 60)
        cycles = int(input(f"{YELLOW}[+] Enter number of IP changes (0 for infinite): {RESET}") or 0)

        if cycles == 0:
            print(f"{GREEN}[+] Infinite mode activated. Press Ctrl+C to stop.{RESET}")
            while True:
                time.sleep(interval)
                rotate_identity()
                print(f"{GREEN}[+] New IP: {fetch_ip()}{RESET}")
        else:
            for _ in range(cycles):
                time.sleep(interval)
                rotate_identity()
                print(f"{GREEN}[+] New IP: {fetch_ip()}{RESET}")
    except KeyboardInterrupt:
        print(f"\n{RED}[!] Operation stopped by user.{RESET}")
    except ValueError:
        print(f"{RED}[!] Invalid input. Please provide a valid number.{RESET}")

if __name__ == "__main__":
    check_sudo()
    install_dependencies()  # Automatically installs dependencies
    execute_rotation()
