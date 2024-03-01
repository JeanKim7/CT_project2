#Shopping Cart List Program

def shopping_cart():
    shopping_cart_list = []
    total=0
    
    print("Welcome to Jean's Store!")
    while True:
        user_input=input("Enter an option below to use your shopping cart!\n"
              "Enter one of the following options (Add/Remove/Show/Clear/Quit): ").lower()
        
        #quit function
        if user_input == "quit":
            break
        
        #add items to the shopping cart
        elif user_input == "add":
            item = input("\nWhat item would you like to add to your shopping cart? ")
            #check if item is in the shopping cart already
            check_list = []
            for a in shopping_cart_list:
                check_list.append(a['item name'])
            #go back go start if item in shopping cart
            if item in check_list:
                print("This item is already in your shopping cart. Please enter 'Add' to add more of this item!\n")
                continue
            #add new item if not in shopping cart already
            else:
                try:
                    quantity = int(input("How many of your item would you like to add? "))
                except ValueError:
                    print("Please enter a number only!\n")
                    continue
                else:
                    try:
                        price = float(input("What is the price of your item? "))
                    except ValueError:
                        print("Please enter a number only!\n")
                        continue
                    else:
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
                            f"Price: ${price:.2f}\n"
                            f"Subtotal: ${subtotal:.2f}\n")
                        total+= subtotal
                        continue
        
        #remove items from shopping cart
        elif user_input == "remove":
            #show current shopping cart
            print("\nHere is your shopping cart:\n")
            for item in shopping_cart_list:
                print(f"Item: {item['item name']}\n"
                      f"Quantity: {item['quantity']}\n"
                      f"Price: ${item['price']:.2f}\n"
                      f"Subtotal: ${item['subtotal']:.2f}\n")
            print(f"Total: ${total:.2f}")
            remove_item = input("\nWhat item would you like to remove from your shopping cart? ")
            #check if item is in shopping cart
            check_list = []
            for a in shopping_cart_list:
                check_list.append(a['item name'])
            #remove item if it is in the shopping cart
            if remove_item in check_list:
                #give option to remove entire or some quantity of item
                completely_gone = input("Would you like to remove the item completely from your cart? (Yes/No)").lower()
                #remove all qunatities of item
                if completely_gone == "yes":
                    for a in shopping_cart_list:
                        if a['item name'] == remove_item:
                            total-=a['subtotal']
                            shopping_cart_list.remove(a)
                            
                    print(f"{remove_item.title()} has been removed from your shopping cart!\n")
                    continue
                #remove some quantity of item
                elif completely_gone == "no":
                    remove_item_quantity = int(input("How many of your item would you like to remove? "))
                    for a in shopping_cart_list:
                        if a['item name'] == remove_item:
                            a['quantity'] -= remove_item_quantity
                            a['subtotal'] -= (remove_item_quantity*a['price'])
                            total -= (remove_item_quantity*a['price'])
                            print("The items have been removed!\n")
                    continue
                else:
                    print("Please enter yes or no.")
            #go back to start if item not in shopping cart
            else:
                print("That item is not in your shopping cart!")
                continue
        
        #show current shopping cart
        elif user_input == "show":
            print("\nHere is your shopping cart:\n")
            for item in shopping_cart_list:
                print(f"Item: {item['item name']}\n"
                      f"Quantity: {item['quantity']}\n"
                      f"Price: ${item['price']:.2f}\n"
                      f"Subtotal: ${item['subtotal']:.2f}\n")
            print(f"Total: ${total:.2f}\n")
            continue
        
        #clear shopping cart
        elif user_input == "clear":
            #confirm message to clear
            confirm_clear=input("Are you sure you want to clear your shopping cart?(Yes/No) ").lower()
            if confirm_clear == 'yes':
                shopping_cart_list = []
                total = 0
                print("Your shopping cart has been cleared!\n")
                continue
            elif confirm_clear == 'no':
                print("")
                continue
            else: 
                print("Please enter yes or no.\n")
                continue

        #print message if they enter wrong input
        else:
            print("Please enter 'Add', 'Remove', 'Show', 'Clear' or 'Quit'!\n")
            continue



shopping_cart()