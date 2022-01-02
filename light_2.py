import time
import wiringpi as wipi
import PCF1 as ADC
import RPi.GPIO as GPIO
import motor-control2 as th

def Lux_Detect():
    TSL2561I2C_ADDR = 0x39
    POWER_UP        = 0x03
    POWER_DOWN      = 0x00
    CONTROL_REG     = 0x80
    DATA0LOW        = 0x8c
    DATA0HIGH       = 0x8d
    DATA1LOW        = 0x8e
    DATA1HIGH       = 0x8f

    #initial I2C device
    fd = wipi.wiringPiI2CSetup(TSL2561I2C_ADDR)

    #collect data
    wipi.wiringPiI2CWrite(fd,CONTROL_REG)
    wipi.wiringPiI2CWrite(fd,POWER_UP)

    time.sleep(0.5)\

    #read data
    wipi.wiringPiI2CWrite(fd,DATA0LOW)
    data0low = wipi.wiringPiI2CRead(fd)

    wipi.wiringPiI2CWrite(fd,DATA0HIGH)
    data0high = wipi.wiringPiI2CRead(fd)

    wipi.wiringPiI2CWrite(fd,DATA1LOW)
    data1low = wipi.wiringPiI2CRead(fd)

    wipi.wiringPiI2CWrite(fd,DATA1HIGH)
    data1high = wipi.wiringPiI2CRead(fd)

    #data processing
    CH0 = 256*data0high + data0low
    CH1 = 256*data1high + data1low

    ratio = float(CH1)/float(CH0)

    #calculate lux
    if (ratio <= 0):
                Lux = 0

    elif ratio <= 0.50:
                Lux = 0.0304*float(CH0)-0.062*float(CH0)*(ratio**1.4)

    elif (ratio > 0.5 and ratio <= 0.61):
                Lux = 0.0224*float(CH0)-0.031*CH1

    elif (ratio > 0.61 and ratio <= 0.80):
                Lux = 0.0128*float(CH0)-0.0153*CH1

    elif (ratio > 0.80 and ratio <= 1.30):
                Lux = 0.00146*float(CH0)-0.00112*CH1

    elif ratio > 1.30:
                Lux = 0

    return Lux
def Metal_Detect():
    if GPIO.input(11):
        return True
    else:
        return False

def GPIO_Setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11,GPIO.IN)

def Weight_Detect():
    ADC.setup(0x48)
    return ADC.read(0)
def Weight_mean():
    total = 0
    for i in range(5):
        temp = Weight_Detect()
        total = total + temp
    return total // 5

def Lux_mean():
    total = 0
    for i in range(5):
        temp = Lux_Detect()
        print(temp)
        total = total + temp
    return total // 5

GPIO_Setup()
th.setupbp()
th.setupzp()
while True:
    GPIO.setup(32,GPIO.OUT)
    GPIO.setup(33,GPIO.IN)
    GPIO.setup(35,GPIO.OUT)
    GPIO.output(32,1)
    #print(GPIO.input(33))
    if GPIO.input(33):
        GPIO.output(35,1)
        time.sleep(0.1)
        a = 0
        Lux = Lux_mean()
        Weight = Weight_mean()
        print(Weight)
        print(Lux)
        if Metal_Detect() and a == 0:
            print("Metal Garbage")
            GPIO.output(35,0)
            th.goto(1)
            a = 1
        if Weight >=185  and Weight <= 225 and Lux > 50 and Lux<135 and a == 0:
            print("Glass")
            GPIO.output(35,0)
            th.goto(4)
            a = 1
        if Weight >= 225 and Weight <= 250 and Lux > 10 and Lux < 30 and a == 0:
            print("Paper Garbage")
            #18~25
            GPIO.output(35,0)
            th.goto(4)
            a = 1
        if Weight >=225 and Weight <= 240 and Lux >= 0 and Lux <= 55 and a == 0:
            print("Plastic Bag")
            a = 1
            GPIO.output(35,0)
            th.goto(3) 
        if Weight > 225 and Weight <= 240 and Lux >= 120 and Lux <= 150 and a == 0:
            print("Plastic Bottle")
            #231,132~144
            GPIO.output(35,0)
            th.goto(6)
            a = 1
        if a == 0 and Weight < 135:
            print("other Garbage")
            GPIO.output(35,0)
            th.goto(2)
        if Weight >= 225 and Lux >= 135 and a == 0:
            print("No Garbage")
            #229,140~161
            GPIO.output(35,0)
            th.goto(0)
            a = 1
