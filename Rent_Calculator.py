#inputs we need from user
#total rent
#electric unit cost
#charge per unit 
#person living in the flat

#outputs
#total amount you will pay

rent = int(input("Enter your flat / hostel rent = "))
food = int(input ("Enter the total food cost ="))
electricity_spend = int(input("Enter the total electricity spend = "))
charge_per_unit = int(input("Enter the charge per unit = "))
person = int(input("Enter the number of person living in the flat / hostel = "))

total_electricity_cost = electricity_spend * charge_per_unit
total_cost = rent + food + total_electricity_cost
amount_per_person = total_cost / person

print("Each person will pay = ", amount_per_person)