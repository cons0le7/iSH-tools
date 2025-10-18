cd $HOME/iSH-tools/tools
echo "Installing BlackBird..."
git clone https://github.com/cons0le7/blackbird-iSH
echo "Installing dependencies..."
cd blackbird-iSH 
chmod +x install.sh
bash install.sh 
cd .. 
echo "BlackBird Installed!"