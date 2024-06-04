#!/usr/bin/env python3

import os

#copia não cara 👍

os.system('am start -a android.intent.action.VIEW -d "https://www.instagram.com/guest.hacking?igsh=MTB3ZzdvejM0bzNjMA=="')


RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"


def clear_screen():
    os.system('clear')


def show_banner():
    clear_screen()
    print(f"{GREEN}   ______       ________            __")
    print("  / ___/ |     / /_  __/___  ____  / /")
    print("  \__ \| | /| / / / / / __ \/ __ \/ /")
    print(" ___/ /| |/ |/ / / / / /_/ / /_/ / /")
    print("/____/ |__/|__/ /_/  \____/\____/_/")
    print(f"{RESET}")
    print(f"{RED}Selecione a Ferramenta{RESET}")
    print("")
    print(f"{YELLOW}TELEGRAM: @guesthacking")
    print(f"CANAL TELEGRAM: @webmetodos")
    print(f"INSTAGRAM: @guest.hacking{RESET}")
    print("")


def install_tool(option):
    clear_screen()
    if option == 1:
        print("Instalando Whois...")
        os.system('pkg install -y whois')
    elif option == 2:
        print("Instalando wget...")
        os.system('pkg install -y wget')
    elif option == 3:
        print("Instalando SQLmap...")
        os.system('pkg install -y git python')
        os.system('git clone https://github.com/sqlmapproject/sqlmap.git')
    elif option == 4:
        print("Instalando SocialFish (Phishing)...")
        os.system('pkg install -y git python2')
        os.system('git clone https://github.com/UndeadSec/SocialFish.git')
        os.chdir('SocialFish')
        os.system('pip2 install -r requirements.txt')
        os.chdir('..')
    elif option == 5:
        print("Instalando Hammer (DDoS)...")
        os.system('pkg install -y git python')
        os.system('git clone https://github.com/cyweb/hammer.git')
    elif option == 6:
        print("Instalando Dirb...")
        os.system('pkg install -y dirb')
    elif option == 7:
        print("Instalando Nmap...")
        os.system('pkg install -y nmap')
    elif option == 8:
        print("Instalando Hydra...")
        os.system('pkg install -y hydra')
    elif option == 9:
        print("Instalando Metasploit...")
        os.system('pkg install -y unstable-repo')
        os.system('pkg install -y metasploit')
    elif option == 10:
        print("Instalando Nikto...")
        os.system('pkg install -y nikto')
    elif option == 11:
        print("Instalando Aircrack-ng...")
        os.system('pkg install -y aircrack-ng')
    elif option == 12:
        print("Instalando John the Ripper...")
        os.system('pkg install -y john')
    elif option == 13:
        print("Instalando Wireshark...")
        os.system('pkg install -y wireshark')
    elif option == 14:
        print("Instalando WPScan...")
        os.system('pkg install -y ruby')
        os.system('gem install wpscan')
    elif option == 15:
        print("Instalando Netcat...")
        os.system('pkg install -y netcat')
    elif option == 16:
        print("Instalando Traceroute...")
        os.system('pkg install -y traceroute')
    elif option == 17:
        print("Instalando Netdiscover...")
        os.system('pkg install -y netdiscover')
    elif option == 18:
        print("Instalando XSStrike...")
        os.system('pkg install -y git python')
        os.system('git clone https://github.com/s0md3v/XSStrike.git')
        os.chdir('XSStrike')
        os.system('pip3 install -r requirements.txt')
        os.chdir('..')
    elif option == 19:
        print("Instalando SqlNinja...")
        os.system('pkg install -y git')
        os.system('git clone https://github.com/xxgrunge/sqlninja.git')
    elif option == 20:
        print("Instalando TheHarvester...")
        os.system('pkg install -y git python')
        os.system('git clone https://github.com/laramies/theHarvester.git')
        os.chdir('theHarvester')
        os.system('pip3 install -r requirements/base.txt')
        os.chdir('..')
    elif option == 21:
        print("Instalando Recon-ng...")
        os.system('pkg install -y git python')
        os.system('git clone https://github.com/lanmaster53/recon-ng.git')
        os.chdir('recon-ng')
        os.system('pip3 install -r REQUIREMENTS')
        os.chdir('..')
    elif option == 22:
        print("Instalando Nikto...")
        os.system('pkg install -y git perl')
        os.system('git clone https://github.com/sullo/nikto.git')
        os.chdir('nikto/program')
        os.system('perl nikto.pl -update')
        os.chdir('../..')
    elif option == 23:
        print("Instalando THC-Hydra...")
        os.system('pkg install -y hydra')
    elif option == 24:
        print("Instalando Wfuzz...")
        os.system('pkg install -y wfuzz')
    elif option == 25:
        print("Instalando Burp Suite...")
        os.system('pkg install -y wget')
        os.system('mkdir -p ~/burp-suite')
        os.system('wget https://portswigger.net/burp/releases/download?product=community&version=2021.8.4&type=linux -O ~/burp-suite/burp-suite-community.tar.gz')
        os.system('tar -xzvf ~/burp-suite/burp-suite-community.tar.gz -C ~/burp-suite/')
        os.system('rm ~/burp-suite/burp-suite-community.tar.gz')
    elif option == 26:
        print("Instalando ZAP (Zed Attack Proxy)...")
        os.system('pkg install -y wget')
        os.system('mkdir -p ~/zap')
        os.system('wget https://github.com/zaproxy/zaproxy/releases/download/v2.10.0/ZAP_2_10_0_unix.tar.gz -O ~/zap/zap.tar.gz')
        os.system('tar -xzvf ~/zap/zap.tar.gz -C ~/zap/')
        os.system('rm ~/zap/zap.tar.gz')
    elif option == 27:
        print("Instalando Hashcat...")
        os.system('pkg install -y hashcat')
    elif option == 28:
        print("Instalando Bettercap...")
        os.system('pkg install -y bettercap')
    elif option == 29:
        print("Instalando Ncat...")
        os.system('pkg install -y ncat')
    elif option == 30:
        print("InstaHack")
        os.system('am start -a android.intent.action.VIEW -d "https://www.instagram.com/guest.hacking?igsh=MTB3ZzdvejM0bzNjMA=="')
    elif option == 31:
        print("DDoS Master")
        os.system('am start -a android.intent.action.VIEW -d "https://t.me/guesthacking"')
    elif option == 32:
        print("Instalando BloodHound...")
        os.system('pkg install -y wget unzip')
        os.system('mkdir -p ~/bloodhound')
        os.system('wget https://github.com/BloodHoundAD/BloodHound/releases/download/4.0.2/BloodHound-linux-x64.zip -O ~/bloodhound/bloodhound.zip')
        os.system('unzip ~/bloodhound/bloodhound.zip -d ~/bloodhound/')
        os.system('rm ~/bloodhound/bloodhound.zip')
    elif option == 33:
        print("Instalando Veil...")
        os.system('pkg install -y veil')
    elif option == 34:
        print("Instalando Empire...")
        os.system('pkg install -y git')
        os.system('git clone https://github.com/EmpireProject/Empire.git ~/Empire')
    elif option == 35:
        print("Saindo...")
        exit()
    else:
        print("Opção inválida")

# Menu 
def main():
    while True:
        show_banner()
        options = [
            "Whois",
            "wget",
            "SQLmap",
            "SocialFish (Phishing)",
            "Hammer (DDoS)",
            "Dirb",
            "Nmap",
            "Hydra",
            "Metasploit",
            "Nikto",
            "Aircrack-ng",
            "John the Ripper",
            "Wireshark",
            "WPScan",
            "Netcat",
            "Traceroute",
            "Netdiscover",
            "XSStrike",
            "SqlNinja",
            "TheHarvester",
            "Recon-ng",
            "Nikto (GitHub)",
            "THC-Hydra",
            "Wfuzz",
            "Burp Suite",
            "ZAP (Zed Attack Proxy)",
            "Hashcat",
            "Bettercap",
            "Ncat",
            "InstaHack",
            "DDoS Master",
            "BloodHound",
            "Veil",
            "Empire",
            "Sair"
        ]
        for i, option in enumerate(options, start=1):
            print(f"{RED}[{i:02d}] {option}{RESET}")

        choice = input("Selecione uma opção: ")
        if choice.isdigit():
            choice = int(choice)
            if choice == len(options):
                break
            elif 1 <= choice <= len(options) - 1:
                install_tool(choice)
            else:
                print(f"{RED}More info: https://t.me/webmetodos{RESET}")
        else:
            print(f"{RED}More info: https://t.me/webmetodos{RESET}")

if __name__ == "__main__":
    main()
