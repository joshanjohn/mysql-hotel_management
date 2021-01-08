import app

def changeName(): #change item_name
    mydb = app.connection.connect()
    cursor = mydb.cursor()
    no = int(input('Which Item_no is Updating :'))
    assgn = input('New Item Name = ')
    a = "update menu set item_name='{}' where item_no={}".format(assgn,no)
    cursor.execute(a)
    mydb.commit()
    mydb.close()
    print('Item Name Updated successfully ^_^\n\n')
    #app.M_display.showall()
    #display updates
    b = input('see Updates (y/n) ->')
    if b == 'y' or 'Y' or 'yes' or 'YES':
        app.M_display.showall()
    else:
        print('')
#changeName()


def changeAmount(): #update amount
    mydb = app.connection.connect()
    cursor = mydb.cursor()
    no = int(input('\nWhich Item_no is Updating :'))
    assgn = int(input('New Amount = '))
    a = "update menu set amount={} where item_no={}".format(assgn,no)
    cursor.execute(a)
    mydb.commit()
    mydb.close()
    print('Amount Updated successfully \n\n')
    #app.M_display.showall()
    #display updates
    b = input('see Updates (yes/no) ->')
    if b == 'y' or 'Y' or 'yes' or 'YES':
        app.M_display.showall()
    else:
        print('')
#changeAmount()

def changeNo(): #update item_no
    mydb = app.connection.connect()
    cursor = mydb.cursor()
    no = input('\nWhich Item_name is Updating :')
    assgn = int(input('New Item_no = '))
    a = "update menu set item_no={} where item_name='{}'".format(assgn,no)
    cursor.execute(a)
    mydb.commit()
    mydb.close()
    print('Item_no Updated successfully \n\n')
    #app.M_display.showall()
    #display updates
    b = input('see Updates (yes/no) ->')
    if b == 'y' or b == 'Y' or b == 'yes' or b == 'YES':
        app.M_display.showall()
    else:
        print('')
            
    
#changeNo()



