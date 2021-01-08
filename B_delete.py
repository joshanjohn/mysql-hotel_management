import app

def deleteNo(): #delete using B_no
    mydb = app.connection.connect()
    cursor = mydb.cursor()
    delete = int(input('\nEnter B_no to delete : '))
    cursor.execute('delete from booking where B_no={}'.format(delete))
    print('successfully Deleted B_no {}'.format(delete))
    mydb.commit()
    mydb.close()
    
#deleteNo()

def deleteName(): #delete using B_name
    mydb = app.connection.connect()
    cursor = mydb.cursor()
    delete = input('\nEnter B_name to delete : ')
    cursor.execute("delete from booking where B_name='{}'".format(delete))
    print('successfully Deleted B_name {}'.format(delete))
    mydb.commit()
    mydb.close()
    
#deleteName()
    
def deleteDate(): #delete using B_date
    mydb = app.connection.connect()
    cursor = mydb.cursor()
    delete = input('\nEnter B_Date to delete : ')
    cursor.execute("delete from booking where B_date='{}'".format(delete))
    print('successfully Deleted B_Date {}'.format(delete))
    mydb.commit()
    mydb.close()
    
#deleteDate()
