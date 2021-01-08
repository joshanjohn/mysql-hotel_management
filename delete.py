import app
def M_deleteNo(): #delete using item_no
    mydb = app.connection.connect()
    cursor = mydb.cursor()
    delete = input('\nEnter Item_no to delete : ')
    cursor.execute('delete from menu where item_no={}'.format(delete))
    print('successfully Deleted item_no {}')
    mydb.commit()
    mydb.close()
    
#M_deleteNo()

def M_deleteName(): #delete using item_name
    mydb = app.connection.connect()
    cursor = mydb.cursor()
    delete = input('\nEnter Item_name to delete : ')
    cursor.execute("delete from menu where item_name='{}'".format(delete))
    print('successfully Deleted item_name {}')
    mydb.commit()
    mydb.close()
    
#M_deleteName()



