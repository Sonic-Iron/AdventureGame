import sqlite3 as sql
import os

class serv():
    def __init__(self, address):
        if os.path.isfile(address):
            setup = False
        else:
            setup = True
        self.db = sql.connect(address)
        self.address = address
        if setup:
            self.db.execute('CREATE TABLE chat(username STRING, text STRING, timestamp REAL)')
    def say(serv, message):
        serv.db.execute('')
        serv.db.commit()

c = serv('multiplayer.db')

c.db.commit()
c.db.close()
