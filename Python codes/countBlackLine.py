from roboid import *

hamster = Hamster()

hamster.wheels(30)

count = 0

while True:
    if hamster.right_floor() < 20 and hamster.left_floor() < 20:
        count += 1
        print(count)

        hamster.wheels(30)
        wait(100)

    wait(20)
