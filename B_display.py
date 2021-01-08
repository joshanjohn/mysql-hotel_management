import app

def showall(): #display all the data in table booking
    mydb = app.connection.connect()
    cursor = mydb.cursor()
    cursor.execute(f'select * from booking')
    data = cursor.fetchall()
    trec = cursor.rowcount #count row
    print(f'\t\t______________TOTAL {trec} RECORDS IN BOOKING____________\n')
    for i in data:
        print(i[0],' | ',i[1],' | ',i[2],' | ',i[3],' | ',i[4],' | ',i[5],' | ',i[6])
    mydb.close()
#showall()

#==========================================SEARCH=============================================================#

def searchNo(): #search using B_no
    mydb = app.connection.connect()
    cursor = mydb.cursor()
    search = int(input('\nENTER B_No -> '))
    a = "select * from booking where B_no={}".format(search)
    cursor.execute(a)
    if cursor.fetchone() is None:
        print('.....WRONG Item_No !.....')
    else:
        cursor.execute(a)
        data = cursor.fetchall()
        for i in data:
            print('\n\tB_No => ',i[0])
            print('\tB_Name => ',i[1])
            print('\tB_Address => ',i[2])
            print('\tph_No => ',i[3])
            print('\temail => ',i[4])
            print('\tB_Date => ',i[5])
            print('\tClass => ',i[6],'\n')
            
#searchNo()




def searchPh(): #search using Ph_No
    mydb = app.connection.connect()
    cursor = mydb.cursor()
    search = int(input('\nENTER ph_No -> '))
    a = "select * from booking where ph_No={}".format(search)
    cursor.execute(a)
    if cursor.fetchone() is None:
        print('.....WRONG Item_No !.....')
    else:
        cursor.execute(a)
        data = cursor.fetchall()
        for i in data:
            print('\n\tB_No => ',i[0])
            print('\tB_Name => ',i[1])
            print('\tB_Address => ',i[2])
            print('\tph_No => ',i[3])
            print('\temail => ',i[4])
            print('\tB_Date => ',i[5])
            print('\tClass => ',i[6],'\n')
            
#searchPh()




def searchClass(): #search by Class
    mydb = app.connection.connect()
    cursor = mydb.cursor()
    search = input('\nENTER Class (eg:A CLASS) -> ')
    a = "select * from booking where Class like '{}'".format(search)
    cursor.execute(a)
    if cursor.fetchone() is None:
        print('.....WRONG Item_No !.....')
    else:
        cursor.execute(a)
        data = cursor.fetchall()
        for i in data:
            print('\n\tB_No => ',i[0])
            print('\tB_Name => ',i[1])
            print('\tB_Address => ',i[2])
            print('\tph_No => ',i[3])
            print('\temail => ',i[4])
            print('\tB_Date => ',i[5])
            print('\tClass => ',i[6],'\n')
            
#searchClass()


def searchStartName(): #search using B_name characters(start with)
    mydb = app.connection.connect()
    cursor = mydb.cursor()
    search = input('\nEnter starting B_Name characters => ')
    a = "select * from booking where B_name like '{}%'".format(search)
    cursor.execute(a)
    if cursor.fetchone() is None:
        print('....No RESULT FOUND....')
    else:
        cursor.execute(a)
        data = cursor.fetchall()
        for i in data:
            print('\n\tB_No => ',i[0])
            print('\tB_Name => ',i[1])
            print('\tB_Address => ',i[2])
            print('\tph_No => ',i[3])
            print('\temail => ',i[4])
            print('\tB_Date => ',i[5])
            print('\tClass => ',i[6],'\n')



#searchStartName()

def searchStartEmail(): #search using Email characters(start with)
    mydb = app.connection.connect()
    cursor = mydb.cursor()
    search = input('\nEnter starting Email characters => ')
    a = "select * from booking where Email like '{}%'".format(search)
    cursor.execute(a)
    if cursor.fetchone() is None:
        print('....No RESULT FOUND....')
    else:
        cursor.execute(a)
        data = cursor.fetchall()
        for i in data:
            print('\n\tB_No => ',i[0])
            print('\tB_Name => ',i[1])
            print('\tB_Address => ',i[2])
            print('\tph_No => ',i[3])
            print('\temail => ',i[4])
            print('\tB_Date => ',i[5])
            print('\tClass => ',i[6],'\n')

#searchStartEmail()




