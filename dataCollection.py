import serial





if __name__ == '__main__':
    #connect to serial channel on default baud rate
    ser = serial.Serial('COM3')
    #open file used to store data
    f = open("data.txt", 'w')
    while True:
        #read line from serial port
        ser_bytes = ser.readline()
        #print line to make sure it is still collecting data
        print(float(ser_bytes))
        #write data from serial port to file then flush to update file
        f.write(str(float(ser_bytes)) + "\n")
        f.flush()


