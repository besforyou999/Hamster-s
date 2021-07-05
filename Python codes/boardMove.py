from roboid import *

hamster = Hamster()

for num in range(0, 4):
    print(num)
    hamster.board_forward()

hamster.board_right()

for num in range(0, 4):
    hamster.board_forward()


for num in range(0,4):
    print(num)
