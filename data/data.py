import sqlite3 as sq

class CallDb():

    def __init__(self) -> None:
        self.base = sq.connect('data.db')
        self.cur = self.base.cursor()

    def sql_start(self):
            if self.base:
                print("Data successfully connect!")
                
                self.cur.execute("CREATE TABLE IF NOT EXISTS "
                "income (id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "value INTEGER NOT NULL, date DATE NOT NULL, "
                "telegram_id INTEGER)")
                
                self.cur.execute("CREATE TABLE IF NOT EXISTS "
                "expenses (id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "name VARCHAR(255) NOT NULL, value INTEGER NOT NULL, "
                "date DATE NOT NULL, telegram_id INTEGER)")
            
                self.cur.execute("CREATE TABLE IF NOT EXISTS "
                "do (id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "name VARCHAR(255) NOT NULL, date DATE NOT NULL, "
                "time VARCHAR(5) NULL, telegram_id INTEGER NOT NULL, "
                "state VARCHAR(6) NOT NULL)")
            
            self.base.commit()

    def add_income(self, income, date, id):
        self.cur.execute("INSERT INTO income (value, date, telegram_id)"
        "VALUES (?, ?, ?)", (income, date, id))
        self.base.commit()

    def add_expenses(self, name, expenses, date, id):
        self.cur.execute("INSERT INTO expenses (name, value, date, telegram_id)"
        "VALUES (?, ?, ?, ?)", (name, expenses, date, id))
        self.base.commit()

    def select_income(self, date_to, date_from, id):
        self.cur.execute("SELECT value FROM income "
        "WHERE (date BETWEEN ? AND ?) AND telegram_id = ?", (date_to, date_from, id))
        date = []
        res = self.cur.fetchall()
        for r in res:
            date.append(r[0])
        return sum(date)

    def select_expenses(self, date_to, date_from, id):
        self.cur.execute("SELECT name, value FROM expenses "
        "WHERE (date BETWEEN ? AND ?) AND telegram_id = ?", (date_to, date_from, id))
        name = []
        value = []
        res = self.cur.fetchall()
        for r in res:
            name.append(r[0])
            value.append(r[1])
        res = list(zip(name, value))
        return {"value" : res, "sum" : sum(value)}
    
    def add_do(self, name, date, id):
        self.cur.execute("INSERT INTO do (name, date, telegram_id, state) "
        "VALUES (?, ?, ?, 'ACTIVE')", (name, date, id))
        self.base.commit()
    
    def add_do_time(self, time, name):
        self.cur.execute("UPDATE do SET time = ? WHERE name = ?",
        (time, name))

        self.base.commit()

    def get_do_names(self, date, id, state):
        self.cur.execute("SELECT name FROM do "
        "WHERE (date = ?) "
        "AND (telegram_id = ?) "
        "AND (state =  ?)",
        (date, id, state))
        names = []
        res = self.cur.fetchall()
        for r in res:
            names.append(r[0])
        return names
    
    def get_do_info(self, name):
        self.cur.execute("SELECT * FROM do WHERE name = ?", (name,))
        res = self.cur.fetchone()
        print(res)
        return res
    
    def del_do(self, name):
        self.cur.execute("DELETE do WHERE name = ?", (name,))
        self.base.commit()
    
    def set_state(self, state, name):
        self.cur.execute("UPDATE do SET state = ? WHERE name = ?",
        (state, name))
        self.base.commit()