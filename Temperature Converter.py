def varAssigner():
    while True:
        choice = input("Do you want to: \n"
                        "A) Convert Units: Fahrenheit to Celsius \n"
                        "B) Covert Units: Celsius to Fahrenheit \n" 
                        "C) Quit \n").upper()

        if choice == "A":
            print("Ok, continuing to coversion rates from Fahrenheit to Celsius \n")
            return choice

        elif choice == "B":
            print("Ok, continuing to coversion rates from Celsius to Fahrenheit \n")
            return choice

        elif choice == "C":
            print("Quitting Program.... \n")
            quit()
        
        else:
            print("Not an option, pick A or B or C")
            pass



def toDo_F(choice):
    while choice == "A":
        quantity_A = input("What is the quantity you wish to convert, (for example: 24) \n")

        try:
            quantity_A = float(quantity_A)
            return quantity_A
        except:
            print("\nThis is not an integer or number... \nPlease Enter an integer or number ")
            pass

def toDo_C(choice):
    while choice == "B":
        quantity_A = input("What is the quantity you wish to convert, (for example: 24) \n")

        try:
            quantity_A = float(quantity_A)
            return quantity_A
        except:
            print("\nThis is not an integer or number... \nPlease Enter an integer or number ")
            pass



def Converter_F(quantity_A):

    print("Converting ", quantity_A, "Fahrenheits to Celsius....")

    quantity_B = (quantity_A - 32.0) * (5/9)

    return quantity_B


def Converter_C(quantity_A):

    print("Converting ", quantity_A, "Celsius to Fahrenheit....")

    quantity_B = ((quantity_A) * (9/5)) + 32.0

    return quantity_B

choice = varAssigner()

while choice != "C":

    if choice == "A":
        temp_quantity_A = toDo_F(choice)
        quantity_B = Converter_F(temp_quantity_A)
        print(round(quantity_B) , " Celsius")
        print("")
        choice = varAssigner()
    
    elif choice == "B":
        temp_quantity_A = toDo_C(choice)
        quantity_B = Converter_C(temp_quantity_A)
        print(round(quantity_B), "Fahrenheit")
        print("")
        choice = varAssigner()
