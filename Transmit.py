import serial
from time import sleep

ser = serial.Serial('/dev/ttyS0', 19200)
data = [[0xFE,0x07,0x90,0x21,0x00,0x00,0x11,0x01,0x00,0xFF],  #Set address as 0x0001
        [0xFE,0x07,0x90,0x21,0x00,0x00,0x12,0x91,0x19,0xFF],  #Set network ID 0x1991
        [0xFE,0x06,0x90,0x21,0x00,0x00,0x13,0x12,0xFF],       #Set channel as 12
        [0xFE,0x06,0x90,0x21,0x00,0x00,0x14,0x04,0xFF],       #Set baud rate as 115200
        [0xFE,0x05,0x90,0x21,0x00,0x00,0x10,0xFF],            #Operate with new parameters
        ]
R_Data = []
write_sucessful = 0
received = bytes(0)

def Config():
    global write_sucessful
    global received
    
    for i in range(5):
        ser.write(data[i])
        while ((ser.in_waiting > 0) and (int.from_bytes(received, byteorder='big') != 255) ):
            received = ser.read()
            R_Data.append(hex(int.from_bytes(received, byteorder='big')))
            write_sucessful = 1
        
        if (write_sucessful == 1):
            print(','.join(R_Data))
            write_sucessful = 0
            received = bytes(0)
            del R_Data[:]
            
        sleep(1)
      
Config()      
while True:
    sleep(1)
    #print("great")
    #ser.write(bytes(data[0]))
    while ((ser.in_waiting > 0) and (int.from_bytes(received, byteorder='big') != 255) ):
        received = ser.read()
        R_Data.append(hex(int.from_bytes(received, byteorder='big')))
        write_sucessful = 1
        
    if (write_sucessful == 1):
        print(','.join(R_Data))
        write_sucessful = 0
        received = bytes(0)
        del R_Data[:]
        
