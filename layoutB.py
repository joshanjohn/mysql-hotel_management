import app

def booking():

    print('\n\t===================== B O O K I N G ========================')

    print('\n\t\t[a]  DISPLAY BOOKING')
    print('\t\t[b]  SEARCH BOOKINGS')
    print('\t\t[c]  INSERT BOOKINGS')
    print('\t\t[d]  UPDATE BOOKINGS')
    print('\t\t[e]  DELETE BOOKINGS')

    ch = input('\nSelect Your Choice =>')

    if ch == 'a'or ch == 'A':
        print('\n\t\t------======D I S P L A Y======------\n\n')
        app.B_display.showall()

    elif ch == 'b' or ch == 'B':
        print('\n\t\t------======S E A R C H======------\n\n')
        print('\n\t |1| search using Booking No(B_no) ')
        print('\t |2| search using Booking name(B_name) ')
        print('\t |3| search booking phone number(Ph_No) ')
        print('\t |4| search using Booking Email ')
        print('\t |5| search using Booking room Class \n')
        
        opt = input('Select Method to Search : ')

        if opt == '1':
            app.B_display.searchNo()

        elif opt == '2':
            app.B_display.searchStartName()

        elif opt == '3':
            app.B_display.searchPh()

        elif opt == '4':
            app.B_display.searchStartEmail()

        elif opt == '5':
            app.B_display.searchClass()
            
        else:
            app.B_display.searchNo()

    elif ch == 'c'or ch == 'C':
        print('\n\t\t------======I N S E R T======------\n\n')
        app.B_insert.insert()

    elif ch == 'd'or ch == 'D':
        print('\n\t\t------======U P D A T E======------\n\n')
        print('\n\t= A = Change Booking number')
        print('\t= B = Change Booking Name')
        print('\t= C = Change booking address')
        print('\t= D = Change Booking phone number')
        print('\t= E = Change Booking Email')
        print('\t= F = Change Booking Date')
        print('\t= G = Change Booking room Class')

        opt = input('\nChoose an Option : ')

        if opt == 'a' or opt =='A':
            app.B_update.changeNo()
        elif opt == 'b' or opt == 'B':
            app.B_update.changeName()
        elif opt == 'c' or opt == 'C':
            app.B_update.changeAddress()
        elif opt == 'd' or opt == 'D':
            app.B_update.changePhno()
        elif opt == 'e' or opt == 'E':
            app.B_update.changeEmail()
        elif opt == 'f' or opt == 'F':
            app.B_update.changeDate()
        elif opt == 'g' or opt == 'G':
            app.B_update.changeClass()
        else:
            print('Invalid Option, sorry')

    elif ch == 'e' or ch == 'E':
        print('\n\t\t------======D E L E T E======------\n\n')
        print('\n\t(1) Delete Using Booking number(B_no)')
        print('\t(2) Delete Using Booking Name(B_name)')
        print('\t(3) Delete Using Booking Date(B_date)')
        
        opt = input('\nSelect an option : ')

        if opt == '1':
            app.B_delete.deleteNo()
        elif opt == '2':
            app.B_delete.deleteName()
        elif opt == '3':
            app.B_delete.deleteDate()    
        else:
            app.B_delete.deleteNo()

    else:
        print('Invalid option')

        
        
        

#booking()
