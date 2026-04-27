print("Select a ride:")
print("1 for Bike")
print("2 for Car")
choice = int(input("Enter your choice: "))
if choice == 1:
    print("\nBike Options:")
    print("1 for Scooty")
    print("2 for Scooter")
    choice2 = int(input("Enter bike type: "))
    if choice2 == 1:
        print("you have selected scooty")
    else:
        print("you have selected scooter")
elif choice == 2:
    print("\nCar Options:")
    print("1 for Sedan")
    print("2 for XUV")
    choice3 = int(input("Enter car type: "))
    if choice3 == 1:
        print("you have selected sedan")
    else:
        print("you have selected XUV")
else:
    print("Wrong choice!")