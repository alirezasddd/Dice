import random
import winsound


Sask = input(""" are you ready? 
     enter Y for yes and N for no
     >>>""")


if Sask.lower() == "y":
    Fask = input("""wanna play Snakes and Ladders or Backgammon? """)
    winsound.Beep(random.randint(50, 500), random.randint(100, 1000))

    if Fask == "Snakes and Ladders":
        print(random.randint(1, 6))
        winsound.Beep(1500, 250)

    elif Fask == "Backgammon":
        print(random.choices([1, 2, 3, 4, 5, 6], k=2))
        winsound.Beep(1000, 200)


elif Sask.lower() == "n":
    print("allright. goodluck")
    winsound.Beep(random.randint(50, 2000), random.randint(200, 800))
