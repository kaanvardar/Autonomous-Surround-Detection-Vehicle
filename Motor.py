import RPi.GPIO as GPIO
import time
import pigpio

class Motor:
    def __init__(self):
        self.pwm1 = 24          #tum pwm1,2,3,4 degiskenlerine bu degerler uygulaniyor
        self.pwm2 = 23
        self.pwm3 = 5
        self.pwm4 = 6  
               
        self.motorInit = pigpio.pi()    #pipgio.pi() pipgio'nun kendi yarattigi pi objesi
        #motorinit pipgio instance
        
        
        self.motorInit.set_mode(self.pwm1,pigpio.OUTPUT)    #pwm'leri raspberry'nin outputlarina esitliyoruz
        self.motorInit.set_mode(self.pwm2,pigpio.OUTPUT) 
        self.motorInit.set_mode(self.pwm3,pigpio.OUTPUT) 
        self.motorInit.set_mode(self.pwm4,pigpio.OUTPUT)   
        
              
        self.motorInit.set_PWM_frequency(self.pwm1,50)      #frekans ayarlama pipgio'nun methodu
        self.motorInit.set_PWM_frequency(self.pwm2,50)
        self.motorInit.set_PWM_frequency(self.pwm3,50)
        self.motorInit.set_PWM_frequency(self.pwm4,50) 
        
               
        self.motorInit.set_PWM_range(self.pwm1, 4095)       #maksimum range ayarlama 4095 degistirme!
        self.motorInit.set_PWM_range(self.pwm2, 4095)
        self.motorInit.set_PWM_range(self.pwm3, 4095)
        self.motorInit.set_PWM_range(self.pwm4, 4095)
        
    #duty_range = list(range{-4095,4095}) seklinde ayarlanabilir
    
    def duty_range(self,duty1,duty2):
        if duty1>4095:
            duty1=4095
        elif duty1<-4095:
            duty1=-4095        
        if duty2>4095:
            duty2=4095
        elif duty2<-4095:
            duty2=-4095
        return duty1,duty2
    
    def left_Wheel(self,duty):                                     # 23 ve 24. pin sol paket icin pmw1,pmw2 
        if duty>0:                                                 # (self.pwm) -> pin numarasi, (0) -> pulse 
            self.motorInit.set_PWM_dutycycle(self.pwm1,0)
            self.motorInit.set_PWM_dutycycle(self.pwm2,duty)
        elif duty<0:
            self.motorInit.set_PWM_dutycycle(self.pwm1,abs(duty))
            self.motorInit.set_PWM_dutycycle(self.pwm2,0)
        else:
            self.motorInit.set_PWM_dutycycle(self.pwm1,0)
            self.motorInit.set_PWM_dutycycle(self.pwm2,0)

    def right_Wheel(self,duty):                                     # 5ve 6. pin sol palet icin pmw3 ve pmw4
        if duty>0:
            self.motorInit.set_PWM_dutycycle(self.pwm3,0)
            self.motorInit.set_PWM_dutycycle(self.pwm4,duty)
        elif duty<0:
            self.motorInit.set_PWM_dutycycle(self.pwm3,abs(duty))
            self.motorInit.set_PWM_dutycycle(self.pwm4,0)
        else:
            self.motorInit.set_PWM_dutycycle(self.pwm3,0)
            self.motorInit.set_PWM_dutycycle(self.pwm4,0)

    def setMotorModel(self,duty1,duty2):
        duty1,duty2=self.duty_range(duty1,duty2)
        self.left_Wheel(duty1)
        self.right_Wheel(duty2)
 
def destroy():
    PWM.setMotorModel(0,0)

if __name__=='__main__':
    print ('Program is starting ... \n')
    try:
        loop()
    except KeyboardInterrupt:  
        destroy()
