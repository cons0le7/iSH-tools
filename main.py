
from pystyle import Colors, Colorate, Center, Box

def recon_ng():
    pass

def nikto():
    pass

def dns_recon():
    pass

def udpscan():
    pass

def infoga():
    pass

def peepler():
    pass

def intel_base():
    pass

def xsstrike():
    pass

def openssl():
    pass

def gnupg():
    pass

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
    option = input(Colors.green + " >>> ")

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
        option = input(" >>> ")
        if option in options:
            options[option]()
        else:
            print("Invalid option, please try again.")

main()