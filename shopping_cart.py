#Shopping Cart List Program

def shopping_cart():
    shopping_cart_list = []
    total=0
    
    while True:
        user_input=input("Welcome to Jean's Store! Enter an option below to use your shopping cart!\n"
              "Enter one of the following options (Add/Remove/Show/Clear/Quit): ").lower()
        
        if user_input == "quit":
            break
        
        elif user_input == "add":
            item = input("\nWhat item would you like to add to your shopping cart? ")
            check_list = []
            for a in shopping_cart_list:
                check_list.append(a['item'])
            if item in check_list:
                print("This item is already in your shopping cart. Please enter 'Add' to add more of this item!\n")
                continue
            else:
                quantity = int(input("How many of your item would you like to add? "))
                price = float(input("What is the price of your item? "))
                subtotal = (quantity*price)
                item_dict = {
                        'item name': item,
                        'quantity':quantity,
                        'price': price,
                        'subtotal' : subtotal 
                        }
                shopping_cart_list.append(item_dict)

                print(f"\nHere is what you added:\n"
                      f"Item: {item}\n"
                      f"Quantity: {quantity}\n"
                      f"Price: {price}\n"
                      f"Subtotal: ${subtotal:.2f}\n")
                total+= subtotal
                continue
        
        elif user_input == "remove":
            print("\nHere is your shopping cart:\n")
            for item in shopping_cart_list:
                print(f"Item: {item['item name']}\n"
                      f"Quantity: {item['quantity']}\n"
                      f"Price: ${item['price']:.2f}\n"
                      f"Subtotal: {item['subtotal']:.2f}\n")
            print(f"Total: {total:.2f}")
            remove_item = input("\nWhat item would you like to remove from your shopping cart? ")
            check_list = []
            for a in shopping_cart_list:
                check_list.append(a['item name'])
            if remove_item in check_list:
                completely_gone = input("Would you like to remove the item completely from your cart? (Yes/No)").lower()
                if completely_gone == "yes":
                    for a in shopping_cart_list:
                        if a['item name']==remove_item:
                            shopping_cart_list.pop(a)
                elif completely_gone == "no":
                    remove_item_quantity = int(input("How many of your item would you like to remove? "))
                    for a in shopping_cart_list:
                        if a['item name'] == remove_item:
                            a['quantity'] -= remove_item_quantity
                            a['subtotal'] -= (remove_item_quantity*a['price'])
                            total -= (remove_item_quantity*a['price'])
                            print("The items have been removed!")
                    continue
                else:
                    print("Please enter yes or no.")
            else:
                print("That item is not in your shopping cart!")
                continue

        elif user_input == "show":
            print("\nHere is your shopping cart:\n")
            for item in shopping_cart_list:
                print(f"Item: {item['item name']}\n"
                      f"Quantity: {item['quantity']}\n"
                      f"Price: ${item['price']:.2f}\n"
                      f"Subtotal: {item['subtotal']:.2f}\n")
            print(f"Total: {total:.2f}")
            continue

        elif user_input == "clear":
            confirm_clear=input("Are you sure you want to clear your shopping cart?(Yes/No) ").lower()
            if confirm_clear == 'yes':
                shopping_cart_list = []
            elif confirm_clear == 'no':
                continue
            else: 
                print("Please enter yes or no.")



shopping_cart()