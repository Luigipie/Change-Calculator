qt = float (0.25) #value of quarters
dm = float (0.10) #value of dime
nk = float (0.05) #value of nickels
pn = float (0.01) #value of pennies
#qt = quarter dm = dime nk = nickels pn = penny
print ("Do you want calculate the change?")
loop = input()
if loop == "no":
    end()
if loop == "yes":
    print("What is the price?")
    price = input()
    print ("How much money gave you?")
    money_received = input()

    calc_change = (float(price) - float (money_received)) #use this to calculate how much change must give

    def calc_qt (calc_change,qt):  #This function will calculate how much quarter is needed
        return (int((float(calc_change) / qt)))
    result_qt = calc_qt (calc_change,qt) #just to recall the function
    modulo_qt = float(calc_change) % float (qt)   #this is needed to calculate the remain of the change

    def calc_dm (modulo_qt,dm): #This function will calculate how much dime is needed
        return (int((float(modulo_qt) / dm)))
    result_dm = calc_dm (modulo_qt, dm) #just to recall the function
    modulo_dm = float (modulo_qt) % float (dm)

    def calc_nk (modulo_dm , nk):
        return (int(float(modulo_dm) / nk))
    result_nk = calc_nk (modulo_dm , nk)
    modulo_nk = float (result_nk) % float (nk)

    def calc_pn (modulo_dm , pn):
        return (round(float(modulo_dm) / pn ))
    result_pn = round(calc_pn(modulo_dm, pn))

    print ("The change is " ,calc_change , "\nYou must give: ", result_qt , "quarters", result_dm , "dime" , result_nk , "nickels and" , result_pn , "penny" )
    print ("do you want calculate another change?")
    exit_sw = input()
    if exit_sw == 'no':  #this to exit the loop
        exit()