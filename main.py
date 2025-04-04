
from pystyle import Colors, Colorate, Center, Box
import json
import subprocess
import os
import sys 

def install_true(key_to_update):
    with open('check.json', 'r') as file:
        data = json.load(file)
    if key_to_update in data.get('tools', {}) and data['tools'][key_to_update] is False:
        data['tools'][key_to_update] = True
    with open('check.json', 'w') as file:
        json.dump(data, file, indent=4)

def check_install(filename='check.json'):
    with open(filename, 'r') as f:
        return json.load(f)

def tool_installed(tool_id):
    tools_status = check_install()
    return tools_status['tools'].get(tool_id, False)

def install_tool(tool_sh):
    script_path = os.path.join(os.getcwd(), 'tools', tool_sh)
    try:
        with subprocess.Popen(['bash', script_path], stdout=subprocess.PIPE, text=True) as process:
            while True:
                output = process.stdout.readline()
                if output == '' and process.poll() is not None:
                    break
                if output:
                    print(output.strip())
    except FileNotFoundError:
        print(f" The script '{script_path}' was not found.")
    except Exception as e:
        print(f" An unexpected error occurred: {e}")

def recon_ng():
    if tool_installed("1"):
        try:
            print(Colors.yellow + "Executing Recon-ng...")
            print(Colors.cyan + "Type 'exit' to exit.")
            subprocess.run(['recon-ng']) 
            sys.exit() 
        except Exception as e:
            print(f"An error occurred while running the script: {e}")
    else:
        install_option = input(Colors.green + " Recon-ng is not installed. Install now? (y/n):\n >>> ")
        install_option = install_option.strip().lower()
        if install_option == 'y':
            tool_sh = 'recon-ng.sh'
            install_tool(tool_sh)
            install_true("1")
            input(Colors.green + " Press Enter to run script.\n >>> ")
            recon_ng()
        elif install_option == 'n':
            main()
        else:
            print(Colors.green + " Invalid choice. Enter 'y' or 'n'.\n >>> ")
            recon_ng()


def nikto():
    if tool_installed("2"):
        try:
            print(Colors.yellow + "Starting shell in ./tools/nikto/program \nCtrl+C once to stop operations within shell and again to exit.")
            print(Colors.cyan + "Example Usage: perl nikto.pl -h http://www.example.com")
            os.chdir('./tools/nikto/program')
            subprocess.call(['bash']) 
            sys.exit() 
        except Exception as e:
            print(f"An error occurred while running the script: {e}")
    else:
        install_option = input(Colors.green + " Nikto is not installed. Install now? (y/n):\n >>> ")
        install_option = install_option.strip().lower()
        if install_option == 'y':
            tool_sh = 'nikto.sh'
            install_tool(tool_sh)
            install_true("2")
            input(Colors.green + " Press Enter to run script.\n >>> ")
            nikto()
        elif install_option == 'n':
            main()
        else:
            print(Colors.green + " Invalid choice. Enter 'y' or 'n'.\n >>> ")
            nikto()
                    
def dns_recon():
    if tool_installed("3"):
        try:
            print(Colors.yellow + "Executing DNSrecon... ")
            print(Colors.cyan + "Example Usage: dnsrecon -d website.com")
            subprocess.run(['dnsrecon']) 
            sys.exit() 
        except Exception as e:
            print(f"An error occurred while running the script: {e}")
    else:
        install_option = input(Colors.green + " DNSrecon is not installed. Install now? (y/n):\n >>> ")
        install_option = install_option.strip().lower()
        if install_option == 'y':
            tool_sh = 'dnsrecon.sh'
            install_tool(tool_sh)
            install_true("3")
            input(Colors.green + " Press Enter to run script.\n >>> ")
            dns_recon()
        elif install_option == 'n':
            main()
        else:
            print(Colors.green + " Invalid choice. Enter 'y' or 'n'.\n >>> ")
            dns_recon()

def udpscan():
    if tool_installed("4"):
        print(Colors.cyan + "Make a selection: ")
        udpscan_choice = input(Colors.cyan + "\n[1] Prompt mode \n[2] CLI mode \n   >>>   ")
        if udpscan_choice == '1':             
            try:
                print(Colors.yellow + "Executing UDPSCAN... ")
                print(Colors.cyan + "Ctrl+C to exit.")
                os.chdir('./tools/UDPSCAN')
                subprocess.run(['python3','UDPSCAN.py']) 
                sys.exit() 
            except Exception as e:
                print(f"An error occurred while running the script: {e}")
        elif udpscan_choice == '2':
            try:
                print(Colors.yellow + "Starting shell in ./tools/UDPSCAN ")
                print(Colors.yellow + "Type 'exit' to exit. ")
                os.chdir('./tools/UDPSCAN')
                subprocess.run(['python3','UDPSCAN.py','-h']) 
                subprocess.call(['bash'])
                sys.exit() 
            except Exception as e:
                print(f"An error occurred while running the script: {e}")
        else: 
            print(Colors.red + "Invalid choice. Enter 1 or 2.")
            udpscan()
    else:
        install_option = input(Colors.green + " UDPSCAN is not installed. Install now? (y/n):\n >>> ")
        install_option = install_option.strip().lower()
        if install_option == 'y':
            tool_sh = 'UDPSCAN.sh'
            install_tool(tool_sh)
            install_true("4")
            input(Colors.green + " Press Enter to run script.\n >>> ")
            udpscan()
        elif install_option == 'n':
            main()
        else:
            print(Colors.green + " Invalid choice. Enter 'y' or 'n'.\n >>> ")
            udpscan()
            
def infoga():
    if tool_installed("5"):
        print("Running Infoga...")
    else:
        print("Infoga is not installed. Please install it.")

def infoga():
    if tool_installed("5"):
        try:
            print(Colors.yellow + "Starting shell in ./tools/Infoga-py3 \nType 'exit' to exit.")
            print(Colors.cyan + "Example Usage: python3 infoga.py --target website.com --source all")
            os.chdir('./tools/Infoga-py3')
            subprocess.run(['python3','infoga.py']) 
            subprocess.call(['bash']) 
            sys.exit() 
        except Exception as e:
            print(f"An error occurred while running the script: {e}")
    else:
        install_option = input(Colors.green + " Infoga is not installed. Install now? (y/n):\n >>> ")
        install_option = install_option.strip().lower()
        if install_option == 'y':
            tool_sh = 'infoga.sh'
            install_tool(tool_sh)
            install_true("5")
            input(Colors.green + " Press Enter to run script.\n >>> ")
            infoga()
        elif install_option == 'n':
            main()
        else:
            print(Colors.green + " Invalid choice. Enter 'y' or 'n'.\n >>> ")
            infoga()

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
        option = input(Colors.green + " └──> ")
        if option in options:
            options[option]()
        else:
            print("Invalid option, please try again.")

main()