import random
from roboid import *

hamster = Hamster()


hamster.wheels(-30, 30)

wait(random.randint(1000,10000))

hamster.stop()
