
import random
rooms = 20 

print('***** Hotel Managment *****')
booking = input('Do you wanna book a room if yes thn type Y or y if no then n or N : ')
while True:
    if booking == 'y' or booking == 'Y':
        rooms = random.randint(1, 21)
        print('Your room is booked')
        
    elif booking == 'n' or booking == 'N':
        OR = input(' do u want to exit if yes then type y or Y if no thn type n or N : ')
        if OR == 'y' or OR =='Y':
            print('Good Bye')
        elif OR == 'n' or OR =='N':
            print('****Going back to booking****')
    continue
    


