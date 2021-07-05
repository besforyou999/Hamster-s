from roboid import *

hamster = Hamster()

hamster.wheels(30)

while True:
    
    if hamster.acceleration_x() < -2000:
        print(hamster.acceleration_x(), hamster.acceleration_y(), hamster.acceleration_z())
    
    wait(20)
