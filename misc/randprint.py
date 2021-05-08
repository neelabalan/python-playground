from time import sleep
import random
import string
population = string.ascii_lowercase + string.ascii_uppercase + string.ascii_letters + string.digits

while True:
    sleep(0.5)
    print(random.choice(population).rjust(random.randint(0,100)))