
*********************************************
    Micropython
*********************************************

The following commands can be used to deploy micropyton.
esptool.py --port /dev/ttyUSB0 erase_flash
The last I tried and it worked is:
esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=detect 0 esp8266-1m-20200902-v1.13.bin

if you don't get REPL prompt despite of succesfull flashing try , try with --flash_mode=dout
esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_mode=dout --flash_size=detect 0 esp8266-1m-20200902-v1.13.bin

===================================
rshell - to connect to micropython
a lot of info can be found on https://github.com/dhylands/rshell

to connect to the pyboard use the following command
rshell -p /dev/ttyUSB0


Important files (only these should be changed, unless you know what you are doing):
/boot.py
/main.py

commands from rshell you can use to modify the files
edit /pyboard/boot.py
edit /pyboard/main.py

Editor used is by default vi, but I set it to nano, which is for you more user friendly
setting editor is possible via command line when start rshell, like:
rshell -p /dev/serial0 --editor nano
or by setting the environment variable EDITOR
export EDITOR=nano

to make the change permanent you can set ot in .bashrc
echo "export EDITOR=nano" >> ~/.bashrc

Example of session of editing of the main.py
----------------------------------------------
sladekm@bluesTwo:~/Install/ESP8266/Micropython$ rshell -p /dev/ttyUSB0 --editor nano
Using buffer-size of 32
Connecting to /dev/ttyUSB0 (buffer-size 32)...
Trying to connect to REPL  connected
Testing if ubinascii.unhexlify exists ... Y
Retrieving root directories ... /boot.py/ /main.py/
Setting time ... Jan 16, 2021 01:08:40
Evaluating board_name ... pyboard
Retrieving time epoch ... Jan 01, 2000
Welcome to rshell. Use Control-D (or the exit command) to exit rshell.
/home/sladekm/Install/ESP8266/Micropython> edit /pyboard/main.py
Retrieving /pyboard/main.py ...
Updating /pyboard/main.py ...

=================================================
Example of the session: (Reset the board to make sure that it is not in flash mode)
=================================================
sladekm@bluesTwo:~$ rshell -p /dev/ttyUSB0 
Using buffer-size of 32
Connecting to /dev/ttyUSB0 (buffer-size 32)...
Trying to connect to REPL  connected
Testing if ubinascii.unhexlify exists ... Y
Retrieving root directories ... /boot.py/
Setting time ... Jan 13, 2021 23:16:47
Evaluating board_name ... pyboard
Retrieving time epoch ... Jan 01, 2000
Welcome to rshell. Use Control-D (or the exit command) to exit rshell.
/home/sladekm> edit /pyboard/main.py
/home/sladekm> edit /pyboard/boot.py
Retrieving /boot.py ...
/home/sladekm> repl
Entering REPL. Use Control-X to exit.
>
MicroPython v1.13 on 2020-09-02; ESP module (1M) with ESP8266
Type "help()" for more information.
>>> 
>>> print("Hello world")
Hello world
>>>

=================================================
You can also connect directly to micrpython via miniterm. Hit multiple time ENTER and you should get the prompt.
~$ miniterm /dev/ttyUSB0 115200
--- Miniterm on /dev/ttyUSB0  115200,8,N,1 ---
--- Quit: Ctrl+] | Menu: Ctrl+T | Help: Ctrl+T followed by Ctrl+H ---

>>>
