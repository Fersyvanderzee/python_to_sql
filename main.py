import mysql.connector

host = ""
user_name = ""
password = ""
database = ""

db = mysql.connector.connect(
    host=host,
    user=user_name,
    password=password,
    database=database
)


# Delete db from connector in order to use this.
def show_db(db):
    curs = db.cursor()
    curs.execute("SHOW DATABASES")

    for x in curs:
        return x


def show_tables(db):
    curs = db.cursor()
    curs.execute("SHOW TABLES")

    for x in curs:
        return(x)
