from roboid import *

hamster = Hamster()

def changeDir():
    hamster.wheels(-30,30)
    wait(2000)
    hamster.wheels(30)


hamster.wheels(30)

while True:
    x = hamster.acceleration_x()

    if x < -2000:
        changeDir()
        
    wait(20)
    
    
