
from pystyle import Colors, Colorate, Center, Box
import json

def check_install(filename='check.json'):
    with open(filename, 'r') as f:
        return json.load(f)

def tool_installed(tool_id):
    tools_status = check_install()
    return tools_status['tools'].get(tool_id, False)

def recon_ng():
    if tool_installed("1"):
        print("Running recon-ng...")
    else:
        print("Recon-ng is not installed. Please install it.")

def nikto():
    if tool_installed("2"):
        print("Running Nikto...")
    else:
        print("Nikto is not installed. Please install it.")

def dns_recon():
    if tool_installed("3"):
        print("Running DNSrecon...")
    else:
        print("DNS Recon is not installed. Please install it.")

def udpscan():
    if tool_installed("4"):
        print("Running UDP Scan...")
    else:
        print("UDP Scan is not installed. Please install it.")

def infoga():
    if tool_installed("5"):
        print("Running Infoga...")
    else:
        print("Infoga is not installed. Please install it.")

def peepler():
    if tool_installed("6"):
        print("Running Peepler...")
    else:
        print("Peepler is not installed. Please install it.")

def intel_base():
    if tool_installed("7"):
        print("Running IntelBase...")
    else:
        print("IntelBase is not installed. Please install it.")

def xsstrike():
    if tool_installed("8"):
        print("Running XSStrike...")
    else:
        print("XSStrike is not installed. Please install it.")

def openssl():
    if tool_installed("12"):
        print("Running OpenSSL...")
    else:
        print("OpenSSL is not installed. Please install it.")

def gnupg():
    if tool_installed("13"):
        print("Running GnuPG...")
    else:
        print("GnuPG is not installed. Please install it.")



def help_menu():
    pass

def report_issue():
    pass

def main():
    banner = r"""
██╗███████╗██╗  ██╗   ████████╗ ██████╗  ██████╗ ██╗     ███████╗
╚═╝██╔════╝██║  ██║   ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
██║███████╗███████║█████╗██║   ██║   ██║██║   ██║██║     ███████╗
██║╚════██║██╔══██║╚════╝██║   ██║   ██║██║   ██║██║     ╚════██║
██║███████║██║  ██║      ██║   ╚██████╔╝╚██████╔╝███████╗███████║
╚═╝╚══════╝╚═╝  ╚═╝      ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝
                                                  v1.0.1
╔══════════════════════════════════════════════════════════════╗                                                                                                                                 
║                https://github.com/cons0le7                   ║   
╠═════════════════════════════╦════════════════════════════════╣
║  Reconnaissance             ║  Password Cracking             ║
║      ├── [1] Recon-ng       ║      ├── [9]                   ║
║      ├── [2] Nikto          ║      ├── [10]                  ║
║      ├── [3] DNSrecon       ║      └── [11]                  ║
║      └── [4] UDPSCAN        ║                                ║
║                             ║  Cryptography                  ║
║  OSINT                      ║      ├── [12] OpenSSL          ║
║      ├── [5] Infoga         ║      └── [13] GnuPG            ║
║      ├── [6] Peepler        ║                                ║
║      └── [7] IntelBase *    ║                                ║
║                             ║  Options                       ║
║  Web-App Testing            ║      ├── [?] Help              ║
║      └── [8] xsstrike       ║      └── [!] Report an Issue   ║
╠═════════════════════════════╩════════════════════════════════╣
║ * = API token required [$]                                   ║
╚══════════════════════════════════════════════════════════════╝
"""
    print((Colorate.Vertical(Colors.rainbow, banner,1)))

    options = {
        "1": recon_ng,
        "2": nikto,
        "3": dns_recon,
        "4": udpscan,
        "5": infoga,
        "6": peepler,
        "7": intel_base,
        "8": xsstrike,
        "12": openssl,
        "13": gnupg,
        "?": help_menu,
        "!": report_issue
    }

    while True:
        option = input(Colors.green + " >>> ")
        if option in options:
            options[option]()
        else:
            print("Invalid option, please try again.")

main()