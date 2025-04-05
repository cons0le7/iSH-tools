echo "Installing Nikto..."
echo ""
echo "Installing Perl..." 
apk add perl 
git clone https://github.com/sullo/nikto
echo "Nikto Installed!"

echo "Installing Recon-ng..."
apk add recon-ng
echo "Recon-ng Installed!"

echo "Installing DNSrecon..."
apk add dnsrecon
echo "DNSrecon Installed!"

echo "Installing UDPSCAN..."
git clone https://github.com/cons0le7/UDPSCAN
echo "UDPSCAN Installed!"

echo "Installing Infoga..."
git clone https://github.com/cons0le7/Infoga-py3
echo "Installing dependencies..."
pip3 install requests
echo "Infoga Installed!"

echo "Installing Peepler"
git clone https://github.com/cons0le7/peepler-iSH.git
cd peepler-iSH
echo "Installing Dependencies... "
pip3 install bs4 requests 
echo "Peepler Installed!"

echo "Installing IntelBase..."
git clone https://github.com/cons0le7/IntelBase-CLI
echo "IntelBase Installed!" 

echo "Installing XSStrike..."
git clone https://github.com/s0md3v/XSStrike
echo "Installing Dependencies..."
pip3 install tld
pip3 install fuzzywuzzy
pip3 install requests
echo "XSStrike Installed!" 

echo "Installing OpenSSL..."
apk add openssl
echo "OpenSSL Installed!"

echo "Installing GnuPG..." 
apk add gnupg
echo "GnuPG Installed!" 

echo ""
echo "-ALL TOOLS INSTALLED-"
