import sqlite3
from datetime import date
from datetime import datetime



def aktualsieren():
    date_format = "%Y/%m/%d"
    conn = sqlite3.connect('Anki.db')
    cursor = conn.cursor()
    sql_skript = """SELECT DaysRevision,Date FROM Flashcards"""
    cursor.execute(sql_skript)
    days = cursor.fetchall()


    for i in range(len(days)):
        a = datetime.strptime(days[i][1], date_format)
        b = days[i][0]
        result = (a + b) - datetime.today()
        sql = """UPDATE Flashcards SET DaysRevision = ? WHERE Days_Revision= ?"""
        cursor.execute(sql, (result, i + 1))






def get_cardarray(cardnumber):
    conn = sqlite3.connect('Anki.db')
    cursor = conn.cursor()
    get_card = """ SELECT * FROM Flashcards WHERE ID = ?"""
    cursor.execute(get_card, (cardnumber, ))
    card = cursor.fetchone()
    return card

def cal_score():
    pass

def return_card(DaysRevesion,Date,):
    conn = sqlite3.connect('Anki.db')
    cursor = conn.cursor()
    sql_returncard = """Insert into Flashcards (DaysRevesion) VALUES (?)""","""Insert into Flashcards (Date) VALUES (?)"""
    cursor.execute(sql_returncard, (DaysRevesion,Date))


