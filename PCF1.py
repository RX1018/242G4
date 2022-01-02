import smbus
import time

bus = smbus.SMBus(1)

def setup(Addr):
    global address
    address = Addr
    
def read(chn):
    if chn == 0:
        bus.write_byte(address,0x40)
    bus.read_byte(address)
    return bus.read_byte(address)

def write(val):
    temp = val
    temp = int(temp)
    bus.write_byte_data(address, 0x40, temp)
    
if __name__ == "__name__":
    setup(0x48)

    while True:
        tmp = read(0)
        tmp = tmp*(255-12)/255
        
        write(tmp)
        time.sleep(2)