import random


ask = input("""are you ready? 
     enter Y for yes and N for no
     >>>""")

if ask.lower() == "y":
     print(random.randint(1, 6))

elif ask.lower() == "n":
     print("allright. goodluck")

