import time
      
from Motor import *            
run=Motor() 

r = 2000   #800'un altina sakin deger koyma r=5000
l = 2000   #left side sikintiliß            l=4000

  
def test_Motor(): 
            try:
                while True:
                    run.setMotorModel(l,r)        #Forward (1,2) 1. value oturunca sol 2. sag palet
                    print ("The car is moving forward")
                    time.sleep(10)   
                    
                    run.setMotorModel(-l,-r)      #Back
                    print ("The car is going backwards")
                    time.sleep(10)
                    
                    run.setMotorModel(-l,r)       # turn left 
                    print ("The car is turning left")
                    time.sleep(2)
                    
                    run.setMotorModel(l,-r)       #turn right 
                    print ("The car is turning right") 
                    time.sleep(2)
                    
                    run.setMotorModel(0,0)              #Stop
                    print ("\nEnd of program")
                    
            except KeyboardInterrupt:
                run.setMotorModel(0,0)              #keyboard interrupt
                print ("\nEnd of program")
                
from Ultrasonic import *
ultrasonic=Ultrasonic()                
def test_Ultrasonic():
    try:
        while True:
            data=ultrasonic.get_distance()   #Get the value

            distance=int(data)
            if distance < 10:
                print("Uzaklik 10cm'den düsük ya da 3metreden buyuk LİDARA DİKKAT!! distance is"+str(distance)+"CM")
            else:
                print ("Obstacle distance is "+str(distance)+"CM") 
            time.sleep(1)
    except KeyboardInterrupt:
        print ("\nEnd of program")
        
        
# Main
if __name__ == '__main__':

    print ('Program is starting ... ')
    import sys
    if len(sys.argv)<2:
        print ("Parameter error: Please assign the device")
        exit() 
    elif sys.argv[1] == 'Motor':
        test_Motor()
    elif sys.argv[1] == 'Ultrasonic':
        test_Ultrasonic()
#sadece forward,left,right,back fonksiyonlari eklenecek
