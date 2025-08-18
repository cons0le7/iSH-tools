# iSH-tools
***Ethical hacking toolkit for iOS devices using [iSH Shell](https://apps.apple.com/us/app/id1436902243)***

## About
When I first downloaded iSH Shell, I searched everywhere for tools related to cybersecurity and ethical hacking but found very few that actually worked. I spent about a year learning iSH, familiarizing myself with Alpine, testing different tools and modifying their installs to work within iSH, as well as  writing some of my own iSH compatible scripts. I have decided to put together a neatly packaged and easy to use toolkit for others who may be looking for the same thing. I plan on updating this whenever I find more useful things. Recommendations and contributions are always welcome!

> [!Warning]
> These tools are intended to be used legally and ethically. Do not use them against anything that you do not own or do not have permission to use them against. I am not responsible for any use or misuse of these tools. 

![Image](https://github.com/user-attachments/assets/e54b1b62-d591-4fc6-bd4d-70f4071cfbc9)

>[!Tip]
> Set font size in iSH settings to 10 or lower for the best experience.

## Single-Paste Install: 
```
cd $HOME
apk add python3 py3-pip bash git
pip3 install pystyle 
git clone https://github.com/cons0le7/iSH-tools
cd $HOME/iSH-tools/tools
chmod +x *.sh
cd ..
chmod +x iSH-tools
./iSH-tools
```
To make the script callable from terminal:
```
ln -s $HOME/iSH-tools/iSH-tools /usr/bin/hack
```
By doing this you can call the script any time with the command: `hack`

If you want the script to be called from a different command: 
change "hack" at the end of the line above to whatever command you would like the script to be called from. Just make sure the name you choose does not conflict with any other installed package names. 

To remove the symlink: 
```
rm /usr/bin/hack
```
## Uninstall 
```
rm -r ~/iSH-tools
rm /usr/bin/hack
```
___
> [!Note]
> ___
> Some tools take a while to install. Keep iSH Shell open until complete. <br><br>
> Tools can take some time to load in the shell environment, wait for them to appear before using. Nikto can be used right away.
> <br> 

--- 
### Contact for help & suggestions: 
[Instagram](http://instagram.com/con5ole) 
[Discord](https://discordapp.com/users/413853735211761670)

## Credits: 

[Recon-ng](https://github.com/lanmaster53/recon-ng)
[Nikto](https://github.com/sullo/nikto)
[DNSrecon](https://github.com/darkoperator/dnsrecon) 
[UDPSCAN](https://github.com/cons0le7/UDPSCAN) 
[Infoga](https://github.com/The404Hacking/Infoga)
[NoSint](https://nosint.org)
[IntelBase](https://github.com/cons0le7/IntelBase-CLI) 
[XSStrike](https://github.com/s0md3v/XSStrike) 
[sqlmap](https://github.com/sqlmapproject/sqlmap) 
[ZipBrute](https://github.com/midwestcoder2020/FileBruteforcers)
[PDFbrute](https://github.com/midwestcoder2020/FileBruteforcers) 
[OpenSSL](http://openssl-library.org) 
[GnuPG](https://gnupg.org)
