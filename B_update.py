import app

def changeNo(): #update B_no
    mydb = app.connection.connect()
    cursor = mydb.cursor()
    no = input('\nWhich B_name is Updating :')
    assgn = int(input('New B_no = '))
    a = "update booking set B_no={} where B_name='{}'".format(assgn,no)
    cursor.execute(a)
    mydb.commit()
    mydb.close()
    print('B_no Updated successfully \n\n')
    #app.B_display.showall()
    #display updates
    b = input('see Updates (yes/no) ->')
    if b == 'y' or b == 'Y' or b == 'yes' or b == 'YES':
        app.B_display.showall()
    else:
        print('')
            
    
#changeNo()
def changeName(): #change B_name
    mydb = app.connection.connect()
    cursor = mydb.cursor()
    no = int(input('Which B_no is Updating :'))
    assgn = input('New B_Name = ')
    a = "update booking set B_name='{}' where B_no={}".format(assgn,no)
    cursor.execute(a)
    mydb.commit()
    mydb.close()
    print('B_Name Updated successfully ^_^\n\n')
    #app.B_display.showall()
    #display updates
    b = input('see Updates (y/n) ->')
    if b == 'y' or 'Y' or 'yes' or 'YES':
        app.B_display.showall()
    else:
        print('')
#changeName()


def changeAddress(): #change B_address
    mydb = app.connection.connect()
    cursor = mydb.cursor()
    no = int(input('Which B_no is Updating :'))
    assgn = input('New B_address = ')
    a = "update booking set B_address='{}' where B_no={}".format(assgn,no)
    cursor.execute(a)
    mydb.commit()
    mydb.close()
    print('B_address  Updated successfully ^_^\n\n')
    #app.B_display.showall()
    #display updates
    b = input('see Updates (y/n) ->')
    if b == 'y' or 'Y' or 'yes' or 'YES':
        app.B_display.showall()
    else:
        print('')
#changeAddress()

def changePhno(): #update Ph_No
    mydb = app.connection.connect()
    cursor = mydb.cursor()
    no = int(input('\nWhich B_no is Updating :'))
    assgn = int(input('New Ph_no = '))
    a = "update booking set Ph_No={} where B_no={}".format(assgn,no)
    cursor.execute(a)
    mydb.commit()
    mydb.close()
    print('Phone No Updated successfully \n\n')
    #app.M_display.showall()
    #display updates
    b = input('see Updates (yes/no) ->')
    if b == 'y' or 'Y' or 'yes' or 'YES':
        app.B_display.showall()
    else:
        print('')
#changePhno()


def changeEmail(): #change Email
    mydb = app.connection.connect()
    cursor = mydb.cursor()
    no = int(input('Which B_no is Updating :'))
    assgn = input('New Email = ')
    a = "update booking set Email='{}' where B_no={}".format(assgn,no)
    cursor.execute(a)
    mydb.commit()
    mydb.close()
    print('Email Updated successfully ^_^\n\n')
    #app.M_display.showall()
    #display updates
    b = input('see Updates (y/n) ->')
    if b == 'y' or 'Y' or 'yes' or 'YES':
        app.B_display.showall()
    else:
        print('')
#changeEmail()


def changeDate(): #change date
    mydb = app.connection.connect()
    cursor = mydb.cursor()
    no = int(input('Which B_no is Updating :'))
    assgn = input('New Date (yyyy-mm-dd) = ')
    a = "update booking set B_date='{}' where B_no={}".format(assgn,no)
    cursor.execute(a)
    mydb.commit()
    mydb.close()
    print('Date Updated successfully ^_^\n\n')
    #app.M_display.showall()
    #display updates
    b = input('see Updates (y/n) ->')
    if b == 'y' or 'Y' or 'yes' or 'YES':
        app.B_display.showall()
    else:
        print('')
#changeDate()

def changeClass(): #change date
    mydb = app.connection.connect()
    cursor = mydb.cursor()
    no = int(input('Which B_no is Updating :'))
    assgn = input('New Class = ')
    a = "update booking set Class='{}' where B_no={}".format(assgn,no)
    cursor.execute(a)
    mydb.commit()
    mydb.close()
    print('Class Updated successfully ^_^\n\n')
    #app.M_display.showall()
    #display updates
    b = input('see Updates (y/n) ->')
    if b == 'y' or 'Y' or 'yes' or 'YES':
        app.B_display.showall()
    else:
        print('')
#changeClass()

