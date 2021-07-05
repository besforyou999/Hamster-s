from roboid import *

hamster = Hamster()

while True:
    #print( hamster.acceleration_x(), hamster.acceleration_y(), hamster.acceleration_z() )
    if  hamster.acceleration_x() > 2000 or hamster.acceleration_x() < -2000 or hamster.acceleration_y() > 2500 or hamster.acceleration_y() < -3500  :
        hamster.wheels(30)
        wait(1500)
        hamster.stop()

    wait(20)

    
