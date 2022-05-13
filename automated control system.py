#importing the libraries
import serial, subprocess, time, pyfirmata 

#defining pins
in1 = 12
in2 = 11
enA = 10

#uploading compilled binaries for firmata
subprocess.Popen(R'%SYSTEMROOT%\System32\WindowsPowerShell\v1.0\powershell.exe -Command "cd C:\Users\mazen.afify.16096124-ETNT\Desktop\avr\bin"; ./avrdude -C C:\Users\mazen.afify.16096124-ETNT\Desktop\avr\etc\avrdude.conf -v -p atmega328p -c arduino -P COM5 -b 57600 -D -U flash:w:C:\Users\mazen.afify.16096124-ETNT\Desktop\arduino\main/StandardFirmata.hex:i', shell = True)

#pausing until the previus command catches up
time.sleep(15)
#function for the belt
def belt():
    if __name__ == '__main__':
        board = pyfirmata.Arduino('COM5')   #specifying which the arduino is connected to
    while True:   #running the motors to deliver product to color sensor
        board.digital[enA].write(1)
        board.digital[in1].write(1)
        board.digital[in2].write(0)
        time.sleep(0.85)
        board.digital[in1].write(0)
        board.digital[in2].write(0)
        pyfirmata.Board.exit(board)   #exiting firmata
        break

belt()   #calling the function
time.sleep(2)

#uploading compilled script for the rgb sensor script
subprocess.Popen(R'%SYSTEMROOT%\System32\WindowsPowerShell\v1.0\powershell.exe -Command "cd C:\Users\mazen.afify.16096124-ETNT\Desktop\avr\bin"; ./avrdude -C C:\Users\mazen.afify.16096124-ETNT\Desktop\avr\etc\avrdude.conf -v -p atmega328p -c arduino -P COM5 -b 57600 -D -U flash:w:C:\Users\mazen.afify.16096124-ETNT\Desktop\arduino\main/grayscale_sensing.hex:i', shell = True)

time.sleep(5)

#introducng global variables
colreading = 0
wereading = 0
x = 1

#opening serial connection
serialcon = serial.Serial()
serialcon.baudrate = 57600
serialcon.port = 'COM5'

#reading serial output
while x == 1:
    serialcon.open()
    packet = serialcon.readline() #reading output
    colreading = float(packet.decode('utf'))  #decoding output
    time.sleep(0.5)
    x = 5 #tick system explained below

if colreading > 127:     #compairing results 
    print("Add more carbon")

elif colreading < 127:
    serialcon.close()
    #loading weight sensor script
    subprocess.Popen(R'%SYSTEMROOT%\System32\WindowsPowerShell\v1.0\powershell.exe -Command "cd C:\Users\mazen.afify.16096124-ETNT\Desktop\avr\bin"; ./avrdude -C C:\Users\mazen.afify.16096124-ETNT\Desktop\avr\etc\avrdude.conf -v -p atmega328p -c arduino -P COM5 -b 57600 -D -U flash:w:C:\Users\mazen.afify.16096124-ETNT\Desktop\arduino\main/loadcell.hex:i', shell = True)
    time.sleep(10)
    serialcon.open()
    x = 1
    
    while x < 30:
        if serialcon.inWaiting:
            packet2 = serialcon.readline()
            wereading = float(packet2.decode('utf')) - 12
            x = x + 1 #tick system

#compairing results
if wereading > 65:
    print("add more water")
elif wereading < 63:
    print("add more glue")
else:
    print("Good Product!")

#the tick system is basically introducing a variable such as x, and making the while loop add 1 to it each time the code is executed
#this is more preferable than using a time.sleep() command and exiting the loop afterwards because it sets a certain number of times for code execution instead of depending on a set amount of time
#ticks are different because they do not depend on a certain unit or a clock and instead depend on the internal clock speed of the computer and how fast the code is going
