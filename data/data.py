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
                "value INTEGER NOT NULL, date DATE NOT NULL, telegram_id INTEGER)")
                
                self.cur.execute("CREATE TABLE IF NOT EXISTS "
                "expenses (id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "name VARCHAR(255) NOT NULL, "
                "value INTEGER NOT NULL, date DATE NOT NULL, telegram_id INTEGER)")
            
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