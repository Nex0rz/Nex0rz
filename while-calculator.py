#============================================================================================================#
#                                             [   QUEST   ]                                                  #
#       Calculator with 'while', all errors handled, can be used repeatedly without closing the program.     #                   
#                                       Operators: *, /, -, +, **, //                                        #                       
#                                          Use F string                                                      #
#         Add comments and stick to the rule: don't comment on what it is, but why it's here.                #
#                                                                                                            #
#============================================================================================================#





























import time

print(f"===============[ Welcome in calculator ]===============")
time.sleep(1)
print(f"  Created by = Nex0rz                      01.09.2026  ")
time.sleep(1)
print(f"=======================================================")



# - Replay is on start, beacuse we need restart aplication from the start.
replay = "yes"
while replay == "yes":

    a = float(input(f" [ Number (1) ] "))
    b = float(input(f" [ Number (2) ] "))

    operation = (input(f"Choose a math operation :  "))
    if operation == "+":
        result = a + b


    elif operation == "-":
        result = a - b


    elif operation == "*":
        result = a * b


    elif operation == "/":
        result = a / b 


    elif operation == "**":
     result = a ** b


    elif operation == "//":
        result = a // b

    print(f" \n Your result is: {result}")


# If you type 'yes' in the terminal, you'll meet our initial condition, and because of that, the whole code can repeat.
   
    replay = input(("If u want try this again, type 'yes' ")).lower()

# We have .lower() there so that we have a safeguard when typing and everything gets sent back in lowercase even if the user has a capital letter.