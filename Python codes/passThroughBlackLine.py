from roboid import *

hamster = Hamster();

speed = 100

while True:
    hamster.wheels(speed)

    if hamster.left_floor() < 20:
        hamster.wheels(30,-30)
        wait(500)
    elif hamster.right_floor() < 20:
        hamster.wheels(-30,30)
        wait(500)

    wait(20)
    
        
    
