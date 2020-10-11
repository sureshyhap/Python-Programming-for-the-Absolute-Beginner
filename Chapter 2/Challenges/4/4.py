car_base = int(input("Enter base price of the car: "))

tax = car_base * .15
license = car_base * .05
dealer_prep = 1000
destination_charges = 500

car_total = car_base + tax + license + dealer_prep + destination_charges

print("The total price of the car is", car_total)
