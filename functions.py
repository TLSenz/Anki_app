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

def cal_score(previous_interval_days, response_quality):
    multipliers = {
            'easy': 2.5,
            'good': 2.0,
            'difficult': 1.5,
            'didnt_know': 0.5
        }
    if response_quality == 'didnt_know':
        return 1

    if previous_interval_days < 1:
        previous_interval_days = 1

    next_interval = int(previous_interval_days * multipliers.get(response_quality, 1.5))

    return next_interval


def return_card(DaysRevesion,Date,):
    conn = sqlite3.connect('Anki.db')
    cursor = conn.cursor()
    sql_returncard = """Insert into Flashcards (DaysRevesion) VALUES (?)""","""Insert into Flashcards (Date) VALUES (?)"""
    cursor.execute(sql_returncard, (DaysRevesion,Date))


def checkcards():
    conn = sqlite3.connect('Anki.db')
    cursor = conn.cursor()
    sql_skript = """SELECT DaysRevision FROM Flashcards WHERE ID <= 0"""
    cards = cursor.fetchall()
    return cards
