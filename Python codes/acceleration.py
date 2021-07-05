from roboid import *

hamster = Hamster()

for speed in range(100):
    hamster.wheels(speed, speed * 3 / 4)
    print(speed)
    wait(20)

    

