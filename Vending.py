money = 100.00 
vending_machine = {"Biscuit":"01", "Chips":"02", "Coffee":"03", "Water":"04", "Soda":"05", "Chocolate":"06"} 
prices = {"Biscuits":"= 10.00", "Chips":"= 15.00", "Coffee":"= 35.00 ", "Water":"= 12.00", "Soda":"= 25.00", "Chocolate":"= 17.00"} 

def set_money(amount): 
	global money
	money = amount
	
def get_stock(): 
	stock = vending_machine.values()
	i = 0
	for amount in stock:
		i += amount
	print(i)
	
def purchase(needed_money): 
	global money
	if money >= needed_money:
		money -= needed_money
		print("Item Vended")
	else:
		print("Not enough money.")

def transaction(user_input): 
	global money
	if user_input == "01":
		purchase(10.00)
	elif user_input == "02":
		purchase(15.00)
	elif user_input == "03":
		purchase(35.00)
	elif user_input == "04":
		purchase(12.00)
	elif user_input == "05":
		purchase(25.00)	
	elif user_input == "06":
		purchase(17.00)
	else:
		print("Invalid Input")
	
def main(): 
	item_list = []
	switch = 1 
	while switch == 1:
		print("SCHOOL VENDING MACHINE\n") 
		print("Here are your selections!\n")
		for item, selection in vending_machine.items(): 
			item_list.append((item, selection))
		
		print(item_list[0:6])
		
		print()
		print("Price of the items")
		for item, price in prices.items(): 
			print(item, price)
		print()	
		
		user_switch = 1 
		while user_switch == 1:
			print("You currently have " + str(money))
			user_input = input("Please select you want to buy: ").upper()
			transaction(user_input)
			print()
			choice = 1
			while choice == 1: 
				user_input = input("Are you finished using vending machine?(yes/no): ").lower()
				if user_input == "yes":
					user_switch = 0
					choice = 0
					switch = 0
				elif user_input == "no":
					user_switch = 1
					choice = 0
				else:
					print("Invalid command")
					choice = 1		
		
main()
		
