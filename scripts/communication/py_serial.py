import serial

class SerialPort():


    def init_serial(self):
        # Init serial port
        try:
            self.serial_port = serial.Serial(port = self.port, baudrate = self.baud, parity = 'N', stopbits = 1, bytesize = 8, timeout = 0.1)
            if self.serial_port.isOpen():
                print("Connected to port: {}".format(self.serial_port.portstr))
        except:
            print("Serial connect fail")
        self.serial_port.read_until(expected='\r')