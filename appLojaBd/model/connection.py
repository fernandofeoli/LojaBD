import psycopg2
from configparser import ConfigParser

class Connection():

    def __init__(self):
        self.conn = self.connect()
        self.conn.autocommit = False
        self.cur = self.conn.cursor()

    def config(self, filename='/home/gabriel/Desktop/LojaBD/appLojaBd/database.ini', section='postgresql'):
        parser = ConfigParser()
        # ler o arquivo config
        parser.read(filename)
     
        # pega sessão, padrão para postgresql
        db = {}
        if parser.has_section(section):
            params = parser.items(section)
            for param in params:
                db[param[0]] = param[1]
        else:
            raise Exception('Section {0} not found in the {1} file'.format(section, filename))
     
        return db
    
    def connect(self):
        """ Conectando ao servidor do banco PostgreSQL """
        try:
            params = self.config()
            return psycopg2.connect(**params)
        except (Exception, psycopg2.DatabaseError) as error:
            print(error)

    def query(self, query):
        self.cur.execute(query)
        
    def execute(self, query, values):
        self.cur.execute(query, values)
    
    def queryResult(self):
        self.result = self.cur.fetchall()
        for row in self.result:
            print(row)
            
    def callProCedure(self,procNome,procValores):
        self.cur.callproc(procNome, procValores)     
        
    def commit(self):
        self.conn.commit()
        
    def rollBack(self):
        self.conn.rollback()  
              
    def close(self):
        self.cur.close()
        self.conn.close()

# Test
#db = Connection()
#db.query('Select * from cliente')
#db.queryResult()
#db.close()