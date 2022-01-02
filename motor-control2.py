import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)

 # 规定zhuanpanGPIO引脚
IN1 = 36      # 接PUL-18
IN2 = 37      # 接PUL+16
IN3 = 40      # 接DIR-
IN4 = 38      # 接DIR+
#bopian
IN5=18
IN6=16
IN7=15
IN8=13
#n 正确位置
n=0
#识别模块的信号接收引脚
IN11=[7,11,12]
GPIO.setup(IN11,GPIO.IN)
def nn():
    while 1:
        if GPIO.input(7)==1:
            if GPIO.input(11)==0:
                if GPIO.input(12)==0:
                    return 1
                    print("metal")
                    break
                else:
                    return 4
                    print("glass")
                    break
            else:
                if GPIO.input(12)==0:
                    return 2
                    print("plastic")
                    break
                else:
                    return 3
                    print("paper")
                    break
        else :
            if GPIO.input(11)==0 and GPIO.input(12)==1:
                return 6
                print("others2 while 5 is full")
                break
            if GPIO.input(11)==1 and GPIO.input(12)==1:
                return 5
                print("others1")
                break
            if GPIO.input(11)==0 and GPIO.input(12)==0:
                return 0
                break

   
    
def setStepzp(w1, w2, w3, w4):
    GPIO.output(IN1, w1)
    GPIO.output(IN2, w2)
    GPIO.output(IN3, w3)
    GPIO.output(IN4, w4)
 
def stopzp():
    setStepzp(0, 0, 0, 0)
 
def forwardzp(delay, steps):  
    for i in range(0, steps):
        setStepzp(1, 0, 1, 0)
        time.sleep(delay)
        setStepzp(0, 1, 1, 0)
        time.sleep(delay)
        setStepzp(0, 1, 0, 1)
        time.sleep(delay)
        setStepzp(1, 0, 0, 1)
        time.sleep(delay)
 
def backwardzp(delay, steps):  
    for i in range(0, steps):
        setStepzp(1, 0, 0, 1)
        time.sleep(delay)
        setStepzp(0, 1, 0, 1)
        time.sleep(delay)
        setStepzp(0, 1, 1, 0)
        time.sleep(delay)
        setStepzp(1, 0, 1, 0)
        time.sleep(delay)
def setStepbp(w1, w2, w3, w4):
    GPIO.output(IN5, w1)
    GPIO.output(IN6, w2)
    GPIO.output(IN7, w3)
    GPIO.output(IN8, w4)
 
def stopbp():
    setStepbp(0, 0, 0, 0)
 
def backwardbp(delay, steps):  
    for i in range(0, steps):
        setStepbp(1, 0, 1, 0)
        time.sleep(delay)
        setStepbp(0, 1, 1, 0)
        time.sleep(delay)
        setStepbp(0, 1, 0, 1)
        time.sleep(delay)
        setStepbp(1, 0, 0, 1)
        time.sleep(delay)
def forwardbp(delay,steps):
    for i in range(0, steps):
        setStepbp(1, 0, 0, 1)
        time.sleep(delay)
        setStepbp(0, 1, 0, 1)
        time.sleep(delay)
        setStepbp(0, 1, 1, 0)
        time.sleep(delay)
        setStepbp(1, 0, 1, 0)
        time.sleep(delay)
def forwardbpzp(delay, steps):  
    for i in range(0, steps):
        setStepbp(1, 0, 0,1)
        setStepzp(1,0,1,0)
        time.sleep(delay)
        setStepbp(0, 1, 0,1)
        setStepzp(0, 1, 1, 0)
        time.sleep(delay)
        setStepbp(0, 1, 1,0)
        setStepzp(0, 1, 0,1)
        time.sleep(delay)
        setStepbp(1, 0, 1,0)
        setStepzp(1, 0, 0, 1)
        time.sleep(delay)
 
def forwardbp(delay, steps):  
    for i in range(0, steps):
        setStepbp(1, 0, 0, 1)
        time.sleep(delay)
        setStepbp(0, 1, 0, 1)
        time.sleep(delay)
        setStepbp(0, 1, 1, 0)
        time.sleep(delay)
        setStepbp(1, 0, 1, 0)
        time.sleep(delay)
def backwardbpzp(delay, steps):  
    for i in range(0, steps):
        setStepbp(1, 0, 1,0)
        setStepzp(1, 0, 0, 1)
        time.sleep(delay)
        setStepbp(0, 1, 1,0)
        setStepzp(0, 1, 0, 1)
        time.sleep(delay)
        setStepbp(0, 1,  0,1)
        setStepzp(0, 1, 1, 0)
        time.sleep(delay)
        setStepbp(1, 0, 0,1)
        setStepzp(1, 0, 1, 0)
        time.sleep(delay)
 
def setupbp():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    GPIO.setup(IN5, GPIO.OUT)      # Set pin's mode is output
    GPIO.setup(IN6, GPIO.OUT)
    GPIO.setup(IN7, GPIO.OUT)
    GPIO.setup(IN8, GPIO.OUT)
def setupzp():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
    GPIO.setup(IN1, GPIO.OUT)      # Set pin's mode is output
    GPIO.setup(IN2, GPIO.OUT)
    GPIO.setup(IN3, GPIO.OUT)
    GPIO.setup(IN4, GPIO.OUT) 
def backonegridzp():
        print ("zp turn 60 degrees counterclockwise...")
        backwardzp(0.001, 1067)   # 发射脉冲时间间隔0.0001（单位秒）   脉冲个数1067
def forwardonegridzp():      
        print ("zp turn 60 degrees clockwise...")
        forwardzp(0.001, 1067)
def backonegridbp():
        print ("bp turn 60 degrees counterclockwise...")
        backwardbp(0.001, 1067)   # 发射脉冲时间间隔0.0001（单位秒）   脉冲个数1067
def forwardonegridbp():
        print ("bp turn 60 degrees clockwise...")
        forwardbp(0.001, 1067)
def forwardonegridbpzp():
        print("bpzp turn 60 degrees clockwise together...")
        forwardbpzp(0.001,1067)
def backonegridbpzp():
        print("bpzp turn 60 degrees counterclockwise together...")
        backwardbpzp(0.001,1067)
#1号为压力传感器

def bpzpstep1(n):
    if n!=1 and n!=2:
        for i in range(0,n-2):
            forwardonegridbpzp()
        
    if n==1:
        backonegridbpzp()
        
def bpstep2():
    forwardonegridbp()
def fuwei(n):
    if n==1:
        forwardonegridzp()
    if n!=1 and n!=2:
        for i in range(0,n-2):
            backonegridzp()

def destroy():
    GPIO.cleanup()             # 释放数据

def goto(n):
    if n!=0:
        print("step1:")
        bpzpstep1(n)
        print("step2:")
        bpstep2()
        print("step3: back to original")
        fuwei(n)
        print("Success!")

if __name__ == '__main__':     # Program start from here
    setupzp()
    setupbp()
    try:
        while 1:
            while n==0:
                print(GPIO.input(7),GPIO.input(11),GPIO.input(12))
                n=nn()
                print(n)
        #读取识别系统的信号得到数值n
            print("step1:")
            bpzpstep1(n)
            print("step2:")
            bpstep2()
            print("fuwei")
            fuwei(n)
            n=0

    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child function destroy() will be  executed.
        des