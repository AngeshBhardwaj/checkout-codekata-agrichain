import time
from src.checkout import Checkout
from src.items import available_items
from src.offers import available_offers


def print_welcome_menu():
    print("\n*********************************\n Hey There! Welcome to the Shop.\n*********************************")
    print("\nProduct pricing for this week is as below:\n")
    print("\nItem\tUnit price\tSpecial Price\n------------------------------------------------")
    for item, price in available_items.items:
        offer_text = ''
        for offer_item, offer in available_offers.offers:
            if offer_item == item:
                for q, p in offer.items():
                    offer_text = '{0} for {1}'.format(q, p)
                break
        print('  {0}\t    {1}\t\t  {2}'.format(item, price, offer_text))


def get_valid_menu_selection(sel_option: str):
    valid_sel_option = 0
    try:
        valid_sel_option = int(sel_option)
    except:
            valid_sel_option = 0
    
    return valid_sel_option


if __name__ == '__main__':

    # print the welcome message and sales info
    print_welcome_menu()
    
    # print the interactive Menu to gauge action and perform it accordingly
    time.sleep(1)
    print("\nWhat would you like to do? Please select an option:\n\t1. Scan items for checkout.\n\t2. Exit the application.")
    main_menu_sel = 0
    while main_menu_sel != 1 or main_menu_sel != 2:
        main_menu_sel = get_valid_menu_selection(input())
            
        if main_menu_sel == 2:
            print("\nAre you sure you want to exit?. Enter Y to confirm.")
            exit_cnf = input()
            if exit_cnf.upper() == 'Y':
                exit(0)
            else:
                main_menu_sel = 0
                print("\nYou have been switched back to the main menu. Please select an option:\n\t1. Scan items for checkout.\n\t2. Exit the application.")
            
        elif main_menu_sel == 1:
            action_menu_sel = 0
            shopping_cart = Checkout()

            while action_menu_sel != 2:
                print("\nWhat would you like to do with your shopping cart?\n\t1. Scan an item and add it.\n\t2. Calculate the total amount and check-out.")
                action_menu_sel = get_valid_menu_selection(input())

                if action_menu_sel == 1:
                    new_cart_item = input()
                    shopping_cart.scan(new_cart_item)
                    print("The item has been added to your cart! Items in cart are: {}".format(shopping_cart.cart_items))
                elif action_menu_sel == 2:
                    total_price = shopping_cart.price
                    print("\nThe total price of items in your cart is: {}\nThanks for Shopping!".format(total_price))
                else:
                    print("You have selected an invalid option, please select a valid option.")
            
            # set the user back to main menu so he can use the app again.
            print("\nPlease select an option:\n\t1. Scan items for checkout.\n\t2. Exit the application.")
        else:
            print("You have selected an invalid option, please select a valid option.")
    

    # shopping_cart = Checkout()
    # shopping_cart.scan('A')
    # shopping_cart.scan('B')

    # total_price = shopping_cart.price
    # print(total_price)