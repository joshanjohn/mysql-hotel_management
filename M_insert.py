import app

def insert():
    mydb = app.connection.connect()
    cursor = mydb.cursor()
    
    item_no = int(input('Item No: -> '))
    item_name = input('Item Name: -> ')
    amount = int(input('Amount: -> '))
    
    print('You have successfully inserted to menu !')
    
    cursor.execute("insert into menu values({},'{}',{})".format(item_no,item_name,amount))
    mydb.commit()
    mydb.close()
#insert()


    
        
