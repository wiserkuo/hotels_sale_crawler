sudo apt-get update && sudo apt-get -y upgrade
sudo apt-get install python-pip
pip install selenium

wget https://github.com/mozilla/geckodriver/releases/download/v0.21.0/geckodriver-v0.21.0-win64.zip
tar -zxvf geckodriver-v0.21.0-win64.zip 
chmod +x geckodriver
sudo cp geckodriver /usr/bin/

sudo apt install default-jre

wget https://goo.gl/FCSwwD
java -jar selenium-server-standalone-3.14.0.jar

sudo apt-get install python3-pip
pip3 install selenium
alias python=python3

python web_crawler.py