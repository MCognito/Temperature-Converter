# imports all methods from the module easygui
from easygui import *


# Function that returns Fahrenheit Value to Celsius Value using the parameter of the initial quantity input
def Converter_F(quantity_A):

    print("Converting ", quantity_A, "Fahrenheits to Celsius....")

    quantity_B = (quantity_A - 32.0) * (5/9)
    quantity_B = round(quantity_B)
    
    return quantity_B

# Function that returns Celsius Value to Fahrenheit Value using the parameter of the initial quantity input
def Converter_C(quantity_A):

    print("Converting ", quantity_A, "Celsius to Fahrenheit....")
    
    quantity_B = ((quantity_A) * (9/5)) + 32.0
    quantity_B = round(quantity_B)

    return quantity_B

while True:  
    # Main Pop Up Window
    title = "Temperature Converter"

    # Hello Message box
    a = msgbox("Hello and welcome to the temperature converter", title)

    if a is None:
        quit()

    # choices for user to pick  
    message = "What would you like to do? "
    options = ["Fahrenheit to Celsius", "Celsius to Fahrenheit"]
    user_option = choicebox(message,title, options)

    if user_option is None:
        quit()

    # if statement to filter user options for correct output
    if user_option == options[0]:
        question = "Enter Temperture in Numbers"
        quantity_A = enterbox(question)


        # loop in case of user inputting incorrect type
        while True:         
            if quantity_A is None:
                quit()
            try: # if tries to do instruction and if it can then it breaks out of loop and follows data flow
                quantity_A = float(quantity_A)
                break
            except: # otherwise restarts the window
                title = "Incorrect Input"
                message = "Please enter a number"
                msgbox(message, title)
                quantity_A = enterbox(question)

                if quantity_A is None:
                    quit()

                pass

        quantity_B = Converter_F(quantity_A)
        title = "Fahrenheit to Celsius"
        message = "Enterted Temperature in Fahrenhiets: " + str(quantity_A) + " is " + str(quantity_B) + " in Celsius"
        msg = msgbox(message, title)



    elif user_option == options[1]:
        question = "Enter Temperture"
        quantity_A = enterbox(question)
        
        while True:
            if quantity_A is None:
                quit()

            try:
                quantity_A = float(quantity_A)
                break
            except:
                title = "Incorrect Input"
                message = "Please enter a number"
                msgbox(message, title)
                quantity_A = enterbox(question)
                if quantity_A is None:
                    quit()
                pass

        quantity_B = Converter_C(quantity_A)
        title = "Celsius to Fahrenheit"
        message = "Enterted Temperature in Celsius: " + str(quantity_A) + " is " + str(quantity_B) + " in Fahrenheits"
        msg = msgbox(message, title)



