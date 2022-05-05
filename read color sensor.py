#importing the libraries
import serial, subprocess, time, pyfirmata 
#uploading compilled binaries for firmata
subprocess.Popen(R'%SYSTEMROOT%\System32\WindowsPowerShell\v1.0\powershell.exe -Command "cd C:\Users\mazen.afify.16096124-ETNT\Desktop\avr\bin"; ./avrdude -C C:\Users\mazen.afify.16096124-ETNT\Desktop\avr\etc\avrdude.conf -v -p atmega328p -c arduino -P COM5 -b 57600 -D -U flash:w:C:\Users\mazen.afify.16096124-ETNT\Desktop\arduino\main/StandardFirmata.hex:i', shell = True)
#sleeping so commands dont intrupt eachother
time.sleep(10)
#function for the belt

def weightsen():
    print("lorem ipsum")

def belt():
    if __name__ == '__main__':
        board = pyfirmata.Arduino('COM5')   #specifying where the arduino is connected
    
    while True:
        board.digital[11].write(1)    #running the motors to deliver product to color sensor
        board.digital[12].write(0)
        board.digital[10].write(1)
        board.digital[9].write(0)
        time.sleep(1.1)
        board.digital[11].write(1)
        board.digital[12].write(1)
        board.digital[10].write(1)
        board.digital[9].write(1)
        pyfirmata.Board.exit(board)   #exiting firmata
        break

belt()   #calling the function

time.sleep(2)
#uploading compilled for the rgb sensor script
subprocess.Popen(R'%SYSTEMROOT%\System32\WindowsPowerShell\v1.0\powershell.exe -Command "cd C:\Users\mazen.afify.16096124-ETNT\Desktop\avr\bin"; ./avrdude -C C:\Users\mazen.afify.16096124-ETNT\Desktop\avr\etc\avrdude.conf -v -p atmega328p -c arduino -P COM5 -b 57600 -D -U flash:w:C:\Users\mazen.afify.16096124-ETNT\Desktop\arduino\main/grayscale_sensing.hex:i', shell = True)

time.sleep(5)


#opening serial connection
serialcon = serial.Serial()
serialcon.baudrate = 57600
serialcon.port = 'COM5'
serialcon.open()
#reading serial connection
while True:
    if serialcon.in_waiting:
        packet = serialcon.readline()
        reading = int(packet.decode('utf'))
        time.sleep(0.5)
        if reading > 127:     #compairing results 
            print("Add more carbon")
            break
        elif reading < 127:
            belt()


