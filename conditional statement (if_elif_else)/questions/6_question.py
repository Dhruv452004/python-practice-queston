'''
Transportation Mode Selection
Problem: Choose a mode of transportation based on the distance (e.g., 
3 km se kam: Walk, 
3 se 15 km  : Bike, 
15 km se jada: Car).
'''

kilometer = float(input("Kitna duri hai? (kilometer mein) "))

if(kilometer <3):
    print("paidal chle ja")
elif(kilometer <=15):
    print("bike se chle ja")
else:
    print("car se chle ja")