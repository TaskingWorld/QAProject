preinstall:
	- sudo apt-get install python3 pip3
	- sudo apt-get update
	- sudo apt-get upgrade

install:
	- pip3 install -r requirements.txt