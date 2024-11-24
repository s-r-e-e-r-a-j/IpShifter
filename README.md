## IP Shifter
IP Shifter is a Python-based tool that automatically rotates your IP address using the Tor network. By leveraging Tor's anonymity features, it allows you to change your IP at specified intervals, providing enhanced privacy and security while browsing.

## Features
- **Automated IP Change:** Change your IP address at a specified time interval.
- **Tor Network Integration:** Uses the Tor network for IP Address Change, ensuring anonymity.
- **Infinite or Fixed Ip Address Change:** Changing your IP either infinitely or for a fixed number of times.
- **Automatic Dependency Installation:** The tool automatically installs Tor, Python packages, and other required software if they are missing.
- **Simple Setup:** The tool is easy to use and requires minimal configuration.
## Installation
IP Shifter will automatically install the required dependencies (`Tor`, `pip3`, and the `requests` module) if they are not already installed on your system.


Follow these steps to use the tool:

### Step 1: Clone the Repository
1. **Clone the IpShifter repository to your local machine:**

```bash
git clone https://github.com/s-r-e-e-r-a-j/IpShifter.git
```
2. **Navigate into the project directory:**

```bash
cd IpShifter
```
```bash
cd IpShifter
```
3. **Install The Tool**
```bash
sudo python3 install.py
  ```
 **Then Enter `y` for install**   
### Step 2: Run the Tool
3. Run the Tool with `sudo` to ensure the necessary permissions for installing dependencies:
```bash
sudo ipshifter
```
The Tool will check if the required software (`Tor`, `pip3`, and `requests` Python package) is installed. If any of these dependencies are missing, the Tool will automatically install them for you.


If the requests module is not installed automatically then you can install it by manually 

```bash
 pip3 install requests
  ```


## Usage
### Configuring the Proxy
For the tool to work properly, your browser or application must be configured to use the Tor network. Follow these steps:

1. **Set SOCKS Proxy:**

- Set the SOCKS proxy for your browser or application to `127.0.0.1:9050.`
- This ensures that all traffic is routed through the Tor network, which IP Shifter uses for IP Changing.

  
2 **Browser Proxy Settings:**

- Open your browser settings.
- Locate the network or proxy settings.
- Change the SOCKS proxy to:
- **Proxy Address:** `127.0.0.1`
- **Port:** `9050`
## Running the Tool
When you run the Tool, it will prompt you for the following inputs:

- **Interval in seconds:** Enter the time interval (in seconds) between each IP change. The default is 60 seconds.
- **Number of Ip Address Change:** Enter the number of IP change. Enter 0 for infinite change.
Example:

```bash
[+] Enter interval (seconds) between IP changes [default: 60]: 120
[+] Enter number of IP change (0 for infinite): 5
```
This will change the IP address every 120 seconds and will stop after 5 IP Address Change. If you enter`0`for infinite IP Address Change, the tool will continue running indefinitely.

## Stopping the Tool
To stop the tool after starting it, simply press`Ctrl+C` in the terminal. If you are running  for infinite IP Address Change, this will halt the execution.
## Uninstallation

 ```bash
cd IpShifter
```
```bash
cd IpShifter
```
 ```bash
 sudo python3 install.py
 ```
**Then Enter `n` for uninstall**

## How It Works
1. **Install Dependencies:** When the Tool is executed, it checks whether the required dependencies (`Tor`, `pip3`, and `requests`) are installed. If they are missing, it automatically installs them.

2. **Start Tor:** The Tool will start the Tor service to begin routing your traffic through the Tor network.

3. **IP Address Changing:** The Tool reloads the Tor service at the specified interval to obtain a new IP address.

4. **Fetch New IP:** The Tool fetches and displays your new IP address every time the Tor identity is changed.

## Important Notes
- **Tor Network:** The speed of your connection may be slower when using Tor, as it routes traffic through multiple relays for anonymity. Expect slower speeds than a normal internet connection.

- **Browser Proxy:** Make sure that your browser or application is configured to use `127.0.0.1:9050` as the SOCKS proxy so that the traffic is routed through the Tor network.

- **Infinite Mode:** If you set the number of Ip Change to `0`, the Tool will run indefinitely and continuously Change your IP.

- **System Permissions:** The Tool will require `sudo` privileges to install Tor and other dependencies. You may need to provide your password when prompted.


## License
This project is licensed under the MIT License - see the LICENSE file for details.


## Disclaimer
IP Shifter is for educational purposes only. Misuse of the tool could violate the terms of service of websites, services, or networks you access. Always use the tool responsibly and in accordance with applicable laws and regulations.

