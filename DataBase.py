import sqlite3







class Database:

    def __init__(self):
        self.db=sqlite3.connect('user')
        self.command=self.db.cursor()

        self.command.execute('CREATE Database if not exists user ')
        self.db.commit()


    def inter_database(self,name,f_name,m_number,age,gender):
        self.command.execute('INSERT INTO user VALUES (?,?,?,?,?)',(name,f_name,m_number,age,gender))
        self.db.commit()
        return 'Successfully'
    
    
    
    def show_data(self,name,m_number):
        self.command.execute('SELECT * FROM user WHERE name=? AND m_number=?',(name,m_number))
        return self.command.fetchall()
    
    
    
    def dele_data(self,name,f_name,m_number,age,gender):
        self.command.execute('DELETE FROM user WHERE name=? AND f_name=? AND m_number=? AND age=? AND gender=?',(name,f_name,m_number,age,gender))
        self.db.commit()
        return 'Successfully'


        

   






