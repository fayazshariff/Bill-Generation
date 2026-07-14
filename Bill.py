from datetime import datetime
name = input("Enter your name:")


# List of items
lists = '''
1. Rice - 40/kg
2. Wheat - 30/kg
3. Sugar - 50/kg
'''

# Declaration of prices
prices = 0
pricelist = []
totalprice = 0
finalprice = 0
ilist = []
qlist = []
plist = []

# Rate of items
items = {'rice': 40, 'wheat': 30, 'sugar': 50}

while True: #infinite loop
    option = input(" Please select an option: \n1. Buy Items\n2. Exit\n")
    if option == '2':
        print("Thank you for shopping with us!")
        break
    elif option == '1':
        print("Available items:\n", lists)




        while True:
            inp1 = input("t buy  press 1 or press 2 to exit): ")
            if inp1 == '2':
                break
            elif inp1 == '1':
                item = input("Enter the item name: ").lower()
                while True:
                    quantity = input("Enter the quantity: ")
                    if quantity.isdigit(): # check if the input is a digit
                        quantity = int(quantity)
                        break
                    else:
                        print("Invalid input. Please enter a valid quantity.")


                if item in items:
                    price = quantity * items[item]
                    pricelist.append((item, quantity, items[item], price))
                    totalprice += price
                    ilist.append(item)
                    qlist.append(quantity)
                    plist.append(price)
                else:
                    print("Selected item is not available.")

        if totalprice > 0:
            tax = (totalprice * 12) / 100
            finalprice = totalprice + tax
            print(25 * "-", "BILL", 25 * "-")
            print(28 * " ", "Visakhapatnam ")
            now = datetime.now()
            print("Date:", now.strftime("%d/%m/%Y %H:%M:%S"))
            print(75 * "-")
            print("sno", 10  * " ", 'items', 8* " ", "Quantity", 8 * " ", "Price")
            for i in range(len(pricelist)):
                print(i, 13 * " ", ilist[i], 8 * " ", qlist[i], 8 * " ", plist[i])
            print(75 * "-")
            print(50 * " ", "Total Price: ", totalprice)
            print(50 * " ", "Tax: ", tax)
            print(75 * "-")
            print(50 * " ", "Final Price: ", finalprice)
            print(75 * "-")
            print(50 * " ", "Thank you for shopping with us!")
            print(75 * "-")
