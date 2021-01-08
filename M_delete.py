import app
def deleteNo(): #delete using item_no
    mydb = app.connection.connect()
    cursor = mydb.cursor()
    delete = input('\nEnter Item_no to delete : ')
    cursor.execute('delete from menu where item_no={}'.format(delete))
    print('successfully Deleted item_no {}'.format(delete))
    mydb.commit()
    mydb.close()
    
#deleteNo()

def deleteName(): #delete using item_name
    mydb = app.connection.connect()
    cursor = mydb.cursor()
    delete = input('\nEnter Item_name to delete : ')
    cursor.execute("delete from menu where item_name='{}'".format(delete))
    print('successfully Deleted item_name {}'.format(delete))
    mydb.commit()
    mydb.close()
    
#deleteName()





