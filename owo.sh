#!/bin/sh
apt update
apt full-upgrade -y
apt install python -y
apt install python3 -y
apt install python-pip -y
apt install python3-pip -y
wget https://raw.githubusercontent.com/derkomai/alfred/master/alfred.py
apt install synaptic -y
apt install software-properties-common apt-transport-https wget -y
wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add -
add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main" -y
apt update
rm /etc/apt/preferences.d/nosnap.pref
apt install snapd -y
apt install code -y
apt install virtualbox -y
snap install slack --classic
snap install discord
apt update 
snap install vlc -y
apt install apt-transport-https curl gnupg -y
curl -s https://brave-browser-apt-release.s3.brave.com/brave-core.asc | sudo apt-key --keyring /etc/apt/trusted.gpg.d/brave-browser-release.gpg add -
echo "deb [arch=amd64] https://brave-browser-apt-release.s3.brave.com/ stable main" | sudo tee /etc/apt/sources.list.d/brave-browser-release.list
apt update
apt install brave-browser -y
curl https://packages.microsoft.com/keys/microsoft.asc | sudo apt-key add -
echo "deb [arch=amd64] https://packages.microsoft.com/repos/ms-teams stable main" > /etc/apt/sources.list.d/teams.list
apt update
apt install teams
apt install default-jre -y
apt install openjdk-11-jre-headless -y
apt install openjdk-8-jre-headless -y
apt full-upgrade
python3 alfred.py