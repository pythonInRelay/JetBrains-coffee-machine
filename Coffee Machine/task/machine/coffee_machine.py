# These are the values for the ingredients we have in the machine
money_available = 550
water_available = 400
milk_available = 540
beans_available = 120
cups_available = 9


# Store the ingredients and money required for an espresso
def drink_espresso():
    global cups_available, water_available, beans_available, money_available
    if water_available <= 250:
        print("Sorry, not enough water!")
        if beans_available <= 16:
            print("Sorry, not enough beans!")
    else:
        print("I have enough resources, making you a coffee!")
        water_available -= 250
        beans_available -= 16
        money_available += 4
        cups_available -= 1


# Store the ingredients and money required for a latte
def drink_latte():
    global cups_available, water_available, milk_available, beans_available, money_available
    if water_available <= 350:
        print("Sorry, not enough water!")
        if milk_available <= 75:
            print("Sorry, not enough milk!")
            if beans_available <= 20:
                print("Sorry, not enough beans!")
    else:
        print("I have enough resources, making you a coffee!")
        water_available -= 350
        milk_available -= 75
        beans_available -= 20
        money_available += 7
        cups_available -= 1


# Store the ingredients and money required for a cappuccino
def drink_cappuccino():
    global cups_available, water_available, milk_available, beans_available, money_available
    if water_available <= 200:
        print("Sorry, not enough water!")
        if milk_available <= 100:
            print("Sorry, not enough milk!")
            if beans_available <= 12:
                print("Sorry, not enough beans!")
    else:
        print("I have enough resources, making you a coffee!")
        water_available -= 200
        milk_available -= 100
        beans_available -= 12
        money_available += 6
        cups_available -= 1


# Allow the user to buy a cup of coffee
def buy_coffee():
    global cups_available
    drink = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
    if drink == "back":
        return
    elif cups_available >= 1:
        if drink == "1":
            drink_espresso()
        elif drink == "2":
            drink_latte()
        elif drink == "3":
            drink_cappuccino()


# Allow the user to add ingredients to the machine
def fill_machine():
    global water_available, milk_available, beans_available, cups_available
    water_available += abs(int(input("Write how many ml of water do you want to add:\n")))
    milk_available += abs(int(input("Write how many ml of milk do you want to add:\n")))
    beans_available += abs(int(input("Write how many grams of coffee beans do you want to add:\n")))
    cups_available += abs(int(input("Write how many disposable cups of coffee do you want to add:\n")))


# Allow the user to withdraw the money in the machine
def withdraw_money():
    global money_available
    money_before = money_available
    money_available -= money_available
    print(f"\nI gave you ${money_before}")


# Allow the user to check the ingredients and money remaining
def remaining():
    print(f"""The coffee machine has:
    {water_available} of water
    {milk_available} of milk
    {beans_available} of coffee beans
    {cups_available} of disposable cups
    ${money_available} of money""")


# Allow the user to buy coffee, fill machine, check remaining ingredients, withdraw money or exit
def main_menu():
    while True:
        selection = input("\nWrite action (buy, fill, take, remaining, exit):\n")
        if selection == "exit":
            return
        elif selection == "buy":
            buy_coffee()
        elif selection == "fill":
            fill_machine()
        elif selection == "take":
            withdraw_money()
        elif selection == "remaining":
            remaining()
        else:
            break


# Run the coffee machine program


main_menu()
