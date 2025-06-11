# iSH-tools
***Security toolkit for iSH Shell.***

## About
When I first downloaded iSH Shell, I searched everywhere for tools related to cybersecurity and ethical hacking but found very few that actually worked. I spent about a year learning iSH, familiarizing myself with Alpine, testing different tools and modifying their installs to work within iSH, as well as  writing some of my own iSH compatible scripts. I have decided to put together a neatly packaged and easy to use toolkit for others who may be looking for the same thing. I plan on updating this whenever I find more useful things. Recommendations and contributions are always welcome!

> [!Warning]
> These tools are intended to be used legally and ethically. Do not use them against anything that you do not own or do not have permission to use them against. I am not responsible for any use or misuse of these tools. 

![Image](https://github.com/user-attachments/assets/cd5c653c-e553-4ae8-941a-a7705195edf1) 

## Single-Paste Install: 
```
cd $HOME
apk add python3 
apk add py3-pip 
apk add bash
apk add git 
pip3 install pystyle 
git clone https://github.com/cons0le7/iSH-tools
cd $HOME/iSH-tools/tools
chmod +x *.sh
cd ..
python3 main.py
```
To make the script callable from terminal:
```
cd $HOME/iSH-tools
chmod +x hack
cp $HOME/iSH-tools/hack /usr/bin/hack
```
By doing this you can call the script any time with the command: `hack`

If you want the script to be called from a different command: 
change "hack" at the end of the last line above to whatever command you would like the script to be called from. It should look like: 

`
cp $HOME/iSH-tools/hack /usr/bin/COMMANDNAMEHERE
`

Just make sure the name you choose does not conflict with any other installed package names.

> [!Note]
> ___
> Works best with font size set to 10 or lower. <br><br>
> Tools can take some time to load in the shell environment, wait for them to appear before using. Nikto can be used right away.
> <br>

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
