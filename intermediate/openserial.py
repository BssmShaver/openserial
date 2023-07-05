import serial
import time
import pymysql

# mysql connect
con = pymysql.connect(host='localhost', user='root', password='1234',
                      db='userDB', charset='utf8')
cur = con.cursor()

sql = "SELECT * from test"
cur.execute(sql)

rows = cur.fetchall()
print(rows)

con.close()

ser = serial.Serial(port = 'COM1', baudrate = 9600)

for row in rows:
    data = ','.join(str(value) for value in row)
    ser.write(data.encode())
    time.sleep(1)
    
    ser.close()

def openSerial(port, baudrate= 9600, bytesize=serial.EIGHTBITS, parity = serial.PARITY_NONE, stoobits=serial.STOPBITS_ONE, timeout=None, xonxoff=False, rtscts=False, dsrdtr=False):
    ser = serial.Serial()
    
    ser.port = ser.baudrate = baudrate
    ser.bytesize = bytesize
    ser.parity = parity
    ser.stoobits = stoobits
    ser.timeout = timeout
    ser.xonxoff = xonxoff
    ser.rtscts = rtscts
    ser.dsrdtr = dsrdtr
    
    ser.open()
    

    def writePort(ser, data):
        ser.write(data)
    
    def writePortUnicode(ser, data):
        writePort(ser, data.encode())
    
    def read(ser, size=1, timeout = None):
        ser.timeout = timeout
        readed = ser.read(size)
        return readed
    
    def readUntilExitCode(ser, exitcode=b'\x03'):
        readed = b''
        while True:
            data = ser.read()
            print(data)
            readed += data
            if exitcode in data:
                return readed[:1]    
            
    def readEOf(ser):
        readed = ser.readline()
        return readed[:-1]
    
    return ser
    

