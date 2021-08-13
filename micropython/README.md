
#    Micropython 

The following commands can be used to deploy micropyton.
<br/>esptool.py --port /dev/ttyUSB0 erase_flash
<br/>The last I tried and it worked is:
<br/>esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-1m-20200902-v1.13.bin

if you don't get REPL prompt despite of succesfull flashing try , try with --flash_mode=dout
<br/>esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_mode=dout --flash_size=detect 0 esp8266-1m-20200902-v1.13.bin

------------------------------------
rshell - to connect to micropython
<br/>a lot of info can be found on https://github.com/dhylands/rshell
<br/>
<br/>to connect to the pyboard use the following command
<br/>rshell -p /dev/ttyUSB0


<br/>Important files (only these should be changed, unless you know what you are doing):
<br/>/boot.py
<br/>/main.py

<br/>commands from rshell you can use to modify the files
<br/>edit /pyboard/boot.py
<br/>edit /pyboard/main.py

<br/>Editor used is by default vi, but I set it to nano, which is for you more user friendly 
<br/>Setting of the editor editor is possible via command line when start rshell, like:rshell -p /dev/serial0 --editor nano or by setting the environment variable EDITOR
<br/>export EDITOR=nano

<br/>To make the change permanent you can set ot in .bashrc
<br/>echo "export EDITOR=nano" >> ~/.bashrc

## Example of session of editing of the main.py

<br/>sladekm@bluesTwo:~/Install/ESP8266/Micropython$ rshell -p /dev/ttyUSB0 --editor nano
<br/>Using buffer-size of 32
<br/>Connecting to /dev/ttyUSB0 (buffer-size 32)...
<br/>Trying to connect to REPL  connected
<br/>Testing if ubinascii.unhexlify exists ... Y
<br/>Retrieving root directories ... /boot.py/ /main.py/
<br/>Setting time ... Jan 16, 2021 01:08:40
<br/>Evaluating board_name ... pyboard
<br/>Retrieving time epoch ... Jan 01, 2000
<br/>Welcome to rshell. Use Control-D (or the exit command) to exit rshell.
<br/>/home/sladekm/Install/ESP8266/Micropython> edit /pyboard/main.py
<br/>Retrieving /pyboard/main.py ...
<br/>Updating /pyboard/main.py ...

## Example of the session: (Reset the board to make sure that it is not in flash mode)

sladekm@bluesTwo:~$ rshell -p /dev/ttyUSB0 
<br/>Using buffer-size of 32
<br/>Connecting to /dev/ttyUSB0 (buffer-size 32)...
<br/>Trying to connect to REPL  connected
<br/>Testing if ubinascii.unhexlify exists ... Y
<br/>Retrieving root directories ... /boot.py/
<br/>Setting time ... Jan 13, 2021 23:16:47
<br/>Evaluating board_name ... pyboard
<br/>Retrieving time epoch ... Jan 01, 2000
<br/>Welcome to rshell. Use Control-D (or the exit command) to exit rshell.
<br/>/home/sladekm> edit /pyboard/main.py
<br/>/home/sladekm> edit /pyboard/boot.py
<br/>Retrieving /boot.py ...
<br/>/home/sladekm> repl
<br/>Entering REPL. Use Control-X to exit.
<br/>>
<br/>MicroPython v1.13 on 2020-09-02; ESP module (1M) with ESP8266
<br/>Type "help()" for more information.
<br/>>>> 
<br/>>>> print("Hello world")
<br/>Hello world
<br/>>>>

----------------------------------------------
You can also connect directly to micrpython via miniterm. Hit multiple time ENTER and you should get the prompt.
<br/>~$ miniterm /dev/ttyUSB0 115200
<br/>--- Miniterm on /dev/ttyUSB0  115200,8,N,1 ---
<br/>--- Quit: Ctrl+] | Menu: Ctrl+T | Help: Ctrl+T followed by Ctrl+H ---

<br/>>>>

# Enable webrepl:

<br/>go to python prompt end insert import webrepl_setup
<br/>>>>import webrepl_setup
<br/>and follow the instructions.
<br/>then connect to a WiFi network advertised as MicroPython-*:
<br/>password is micropythoN
<br/>(N capitalized)
<br/>You can download local webrepl from 
<br/>https://github.com/micropython/webrepl
<br/>then from the browser call
<br/>webrepl.html
<br/>password is the password you defined during webrepl_setup (polypocke)
<br/>NOTE: You have to stop an application on ESP8266 otherwise keyboard input doesn't work. You can even stop it from webrepl by CTRL-C
<br/>You can connect ESP8266 to your wifi network:
<br/>-----
<br/>import network
<br/>wlan = network.WLAN(network.STA_IF)
<br/>wlan.active(True)
<br/>wlan.connect('o2-WLAN19', '5577325077316577')
<br/>-----
<br/>One important thing to note is that the ESP8266 will always remember the last WiFi network it used and attempt to connect automatically on reboot.  This is handy since it means when the ESP8266 boots up it will automatically connect to the last network without you having to run the commands above again.  The board will only remember the last network though and not an entire history of older networks.
<br/>-----
<br/>Disable os debug
<br/>To disable debug output connect to the board's serial REPL and run the following commands:
<br/>import esp
<br/>esp.osdebug(None)
<br/>it can be done in boot.py
