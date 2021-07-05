from roboid import *

hamster = Hamster()

while True:
    #왼쪽 근접 센서 값으로 양쪽 바퀴의 속도를 결정
    speed = hamster.left_proximity()

    hamster.wheels(speed, speed)

    wait(10)
