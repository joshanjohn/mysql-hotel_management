import app

#-------------------------------------------------TABLE----------------------------------------------------------#

def table():
    print("\n\n\n\t\t\t=========================================================")
    print("\t\t\t*\t\t\t\t\t\t\t*")
    print("\t\t\t*\t\t\t\t\t\t\t*")
    print("\t\t\t*\t S U C C E S S F U L L Y   L O G I N \t\t*")
    print("\t\t\t*\t\t\t\t\t\t\t*")
    print("\t\t\t*\t\t\t\t\t\t\t*")
    print("\t\t\t* \t\t [A] MENU\t\t\t\t*")
    print("\t\t\t*\t\t\t\t\t\t\t*")
    print("\t\t\t* \t\t [B] BOOKING\t\t\t\t*")
    print("\t\t\t*\t\t\t\t\t\t\t*")
    print("\t\t\t*\t\t\t\t\t\t\t*")
    ch = input("\t\t\t\t Enter table to access : ")
    print("\t\t\t=========================================================")
    if ch == 'a' or ch =='A':
        while True:
            app.layoutM.menu()
    elif ch == 'b' or ch == 'B':
        while True:
            app.layoutB.booking()
    else:
        error()
#-----------------------------------------------------ERROR BOX-------------------------------------------------#

def error():
    print("\n\n\t\t\t#########################################################")
    print("\t\t\t%\t\t\t\t\t\t\t%")
    print("\t\t\t%\t\t\t\t\t\t\t%")
    print("\t\t\t%\t    A C C E S S   D E N I E D \t\t\t%")
    print("\t\t\t%\t\t\t\t\t\t\t%")
    print("\t\t\t%\t\t\t\t\t\t\t%")
    print("\t\t\t#########################################################")


#-------------------------------------------------LOGIN PAGE---------------------------------------------------#
def main():
    print("\t\t\t=========================================================")
    print("\t\t\t|\t\t\t\t\t\t\t|")
    print("\t\t\t|\t\t\t\t\t\t\t|")
    print("\t\t\t|\t\t\tL O G I N \t\t\t|")
    print("\t\t\t|\t\t\t\t\t\t\t|")
    print("\t\t\t|\t\t\t\t\t\t\t|")
    b = input("\t\t\t\t\tUSERNAME : ")
    print("\t\t\t|\t\t\t\t\t\t\t|")
    print("\t\t\t|\t\t\t\t\t\t\t|")
    a = input("\t\t\t\t\tPASSWORD : ")
    print("\t\t\t|\t\t\t\t\t\t\t|")
    print("\t\t\t|\t\t\t\t\t\t\t|")
    print("\t\t\t|\t\t\t\t\t\t\t|")
    print("\t\t\t=========================================================")

    if b == 'user' and a == 'root':
        table()
    

    else:
        error()

main()
