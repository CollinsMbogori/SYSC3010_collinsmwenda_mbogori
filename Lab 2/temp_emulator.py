import random

def get_temperature():
    temp = random.randint(-1,41)
    if temp >= 0 or temp <= 40:
        print("Temperature within range", temp)
    else:
        print("Temperature out of range", temp)
