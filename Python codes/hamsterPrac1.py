from roboid import *

hamster = Hamster()

def func1():
    hamster.wheels(-30,-30)
    wait(1000)    
    hamster.wheels(-60,60)
    wait(1000)

while True:
    if hamster.left_proximity() < 60 and hamster.right_proximity() < 60:
        hamster.wheels(100)
    else:
        func1()
        
    wait(20)

   
