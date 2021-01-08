import app


def showall(): #display all the data in table menu
    mydb = app.connection.connect()
    cursor = mydb.cursor()
    cursor.execute('select * from menu')
    data = cursor.fetchall()
    trec = cursor.rowcount #count row
    print(f'______________TOTAL {trec} RECORDS IN MENU____________\n')
    for i in data:
        print(i[0],'|   ',i[1],'  :  ',i[2])
    mydb.close()
#showall()

#----------------------SEARCH METHODS---------------------------#
def searchNo(): #search using item_no
    mydb = app.connection.connect()
    cursor = mydb.cursor()
    search = int(input('\nENTER Item_No - '))
    a = "select * from menu where item_no={}".format(search)
    cursor.execute(a)
    if cursor.fetchone() is None:
        print('.....WRONG Item_No !.....')
    else:
        cursor.execute(a)
        data = cursor.fetchall()
        for i in data:
            print('\n\tItem No => ',i[0])
            print('\tItem Name => ',i[1])
            print('\tAmount => ',i[2])
            
#searchNo()

def searchName(): #search using item_name
    mydb = app.connection.connect()
    cursor = mydb.cursor()
    search = input('\nENTER Item Name  - ')
    a = "select * from menu where item_name='{}'".format(search)
    cursor.execute(a)
    if cursor.fetchone() is None:
        print(f'...SORRY ! cannot find item_name {search}....')
    else:
        cursor.execute(a)
        data = cursor.fetchall()
        for i in data:
            print('\n\tItem No => ',i[0])
            print('\tItem Name => ',i[1])
            print('\tAmount => ',i[2])

#searchName()



