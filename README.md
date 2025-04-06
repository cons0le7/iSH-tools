# iSH-tools
**Security toolkit for iSH Shell.**

When I first downloaded iSH Shell, I searched everywhere for tools related to cybersecurity and ethical hacking but found very few that actually worked. I spent about a year learning iSH, familiarizing myself with Alpine, testing different tools and modifying their installs to work within iSH, as well as  writing some of my own iSH compatible scripts. I have decided to put together a neatly packaged and easy to use toolkit for others who may be looking for the same thing. I plan on updating this whenever I find more useful things. Recommendations and contributions are always welcome!

![Image](https://github.com/user-attachments/assets/cd5c653c-e553-4ae8-941a-a7705195edf1) 

## Single-Paste Install: 
```
apk add python3 
apk add py3-pip 
apk add bash
apk add git 
pip3 install pystyle 
git clone https://github.com/cons0le7/iSH-tools
cd ./iSH-tools/tools
chmod +x *.sh
cd ./.. 
python3 main.py
```
## Credits: 

[Recon-ng](https://github.com/lanmaster53/recon-ng)
[Nikto](https://github.com/sullo/nikto)
[DNSrecon](https://github.com/darkoperator/dnsrecon) 
[UDPSCAN](https://github.com/cons0le7/UDPSCAN) 
[Infoga](https://github.com/The404Hacking/Infoga)
[Peepler](https://github.com/scarlmao/peepler)
[IntelBase](https://github.com/cons0le7/IntelBase-CLI) 
[XSStrike](https://github.com/s0md3v/XSStrike) 
[sqlmap](https://github.com/sqlmapproject/sqlmap) 
[ZipBrute](https://github.com/midwestcoder2020/FileBruteforcers)
[PDFbrute](https://github.com/midwestcoder2020/FileBruteforcers) 
[OpenSSL](http://openssl-library.org) 
[GnuPG](https://gnupg.org)

## Additional Notes:
- Works best with font size set to 10 or lower.
- Tools can take some time to load in the shell environment, wait for them to appear before using. Nikto can be used right away.
- There is currently 1 known issue with the install all option, I will be fixing this ASAP! For now, installing the tools from their options in menu still works!
- If you have already ran install all and get errors, you can reset the install by editing `check.json` and setting the values to the corresponding tools numbers to `false` and it will prompt for install when attempting to load the tool from menu the next time. 

## Disclaimer: 
These tools are intended to be used legally and ethically. Do not use them against anything that you do not own or do not have permission to use them against. I am not responsible for any use or misuse of these tools. 
