import app
def insert():
    mydb = app.connection.connect()
    cursor = mydb.cursor()
    
    B_no = int(input('Item No: -> '))
    B_name = input('Item Name: -> ')
    B_address = input('Address: -> ')
    ph_No = input('Ph No: -> ')
    email = input('Email: -> ')
    B_date = input('Date(yyyy-mm-dd): -> ')
    cls = input('Class(eg:A CLASS)')
    
    cursor.execute("insert into booking values({},'{}','{}',{},'{}','{}','{}')".format(B_no,B_name,B_address,ph_No,email,B_date,cls))
    print('You have successfully inserted to menu !\n')
    mydb.commit()
    mydb.close()
#insert()
