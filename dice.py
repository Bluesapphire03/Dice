import random

def rolldice(min, max):
    print ("Rolling dice.....")
    number= random.randint(min,max)
    print(f"Your number : {number}")
    
rolldice(1, 6)