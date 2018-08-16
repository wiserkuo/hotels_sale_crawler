## Install pip3

sudo apt-get update && sudo apt-get -y upgrade

sudo apt-get install python3-pip

pip3 install selenium

alias python=python3

## Install firefox webdriver geckodriver python binding

wget https://github.com/mozilla/geckodriver/releases/download/v0.21.0/geckodriver-v0.21.0-win64.zip

tar -zxvf geckodriver-v0.21.0-win64.zip 

chmod +x geckodriver

sudo cp geckodriver /usr/bin/

## Install jre

sudo apt install default-jre

## Install selenium server

wget https://goo.gl/FCSwwD

java -jar selenium-server-standalone-3.14.0.jar

## Execute crawler script

python web_crawler.py