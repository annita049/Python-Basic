# Welcome
print("Welcome to PyCafe!")

menu = {
    'Burger': 60,
    'Pizza': 150,
    'Pasta': 100,
    'Cola': 20,
    'Water': 15
}

order = input("Would you like to order anything? Yes/No ")
if order == "Yes":

    # menu
    for name,price in menu.items():
        print(name,":", price)

    total_bill = 0

    item1 = input("What would you like to order? ")

    if item1 in menu:
        total_bill+= menu[item1]
        print(f"{item1} has been added to your order.")

    else :
        print(f"{item1} is not available right now.")


    order_again = input("Do you want to order anything else? Yes/No ")

    if order_again == "Yes":

        item2 = input("What would you like to order? ")
        if item2 in menu:
            total_bill+= menu[item2]
            print(f"{item2} has been added to your order.")

        else:
            print(f"{item1} is not available right now.")

        print("Your total bill is", total_bill)
        print("Thank you for coming!")

    else:
        print("Your total bill is", total_bill)
        print("Thank you for coming!")

else:
    print("Please Come any other day!")

